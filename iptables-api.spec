Name:           iptables-api
Version:        1.17
Release:        1%{?dist}
Summary:        HTTP REST API for iptables (golang)

License:        MIT
URL:            https://github.com/jeremmfr/iptables-api
Source0:        https://github.com/jeremmfr/iptables-api/archive/refs/tags/v%{version}.tar.gz

BuildRequires:  golang
Requires:       iptables

%description
iptables-api is a REST HTTP service to control iptables firewall rules using an API.
It allows GET, POST, PUT, DELETE operations for firewall manipulation.

%prep
%setup -q

%build
export GO111MODULE=on
go build -o iptables-api

%install
rm -rf %{buildroot}

# Binary
install -d %{buildroot}%{_bindir}
install -m 0755 iptables-api %{buildroot}%{_bindir}/iptables-api

# Config directory
install -d %{buildroot}%{_sysconfdir}/default
cat > %{buildroot}%{_sysconfdir}/default/iptables-api << 'EOF'
IPTABLES_API_OPTS='-ip 127.0.0.1 -port 8080'
EOF

# Systemd service
install -d %{buildroot}%{_unitdir}
cat > %{buildroot}%{_unitdir}/iptables-api.service << 'EOF'
[Unit]
Description=iptables API service
After=network-online.target
Wants=network-online.target

[Service]
EnvironmentFile=-/etc/default/iptables-api
ExecStart=/usr/bin/iptables-api $IPTABLES_API_OPTS
Restart=always
RestartSec=2
User=root
Group=root

[Install]
WantedBy=multi-user.target
EOF

%pre
# If upgrading, preserve existing config
if [ -f %{_sysconfdir}/iptables-api/config.yml.rpmnew ]; then
    mv -f %{_sysconfdir}/iptables-api/config.yml.rpmnew %{_sysconfdir}/iptables-api/config.yml
fi

%post
# Enable and start service
systemctl daemon-reload >/dev/null 2>&1 || :
systemctl enable iptables-api.service >/dev/null 2>&1 || :
systemctl restart iptables-api.service >/dev/null 2>&1 || :

%preun
if [ $1 -eq 0 ]; then
    systemctl stop iptables-api.service >/dev/null 2>&1 || :
    systemctl disable iptables-api.service >/dev/null 2>&1 || :
fi

%postun
systemctl daemon-reload >/dev/null 2>&1 || :

%files
%license LICENSE
%doc README.md

%config(noreplace) %{_sysconfdir}/default/iptables-api
%{_bindir}/iptables-api
%{_unitdir}/iptables-api.service

%changelog
* Tue Dec 09 2025 Trevor Steyn <trevor@webon.co.za> - 1.17-1
- Initial RPM with systemd service and default config

