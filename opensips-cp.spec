%define webroot /var/www/%{name}
%define webuser apache
%define webgroup apache
%define debug_package %{nil}

Name:		opensips-cp		
Version:	9.3.2
Release:	1%{?dist}
Summary:	OpenSIPS Control Panel

Group:		Applications/Communications
License:	GPLv2
URL:		http://controlpanel.opensips.org
Source0:	https://github.com/OpenSIPS/opensips-cp/archive/%{name}-%{version}.zip
#Patch0:		opensips-cp.patch

Requires:	httpd	
Requires:	php	
Requires:	php-gd
Requires:	php-mysqlnd
#Requires:	php-xmlrpc
Requires:	php-pear
Requires:	php-pecl-apcu
#Requires:	php-pear-MDB2-Driver-mysql
#Requires:	php-pear-MDB2
#Requires:	mariadb-server	

%description
OpenSIPS Control Panel is a PHP Web Portal for provisioning OpenSIPS SIP server. A single instance of OpenSIPS Control Panel may be used to provision, operate and monitor multiple instances of OpenSIPS servers, in different locations, with different purposes.


%prep

%setup -q -n %{name}-%{version}
%{__cat} <<EOF >opensips-cp.httpd
# Author Trevor Steyn <trevor@webon.co.za>
# Sample config
	<Directory %{webroot}/web>
		Options Indexes FollowSymLinks MultiViews
		AllowOverride None
		Order allow,deny
		allow from all
	</Directory>
	<Directory  %{webroot}>
		Options Indexes FollowSymLinks MultiViews
		AllowOverride None
		Order deny,allow
		deny from all
	</Directory>
	Alias /cp %{webroot}/web
EOF

#%patch0 -p1

%build

%install
%{__mkdir} -p %{buildroot}%{webroot}
%{__cp} -r config %{buildroot}%{webroot}
%{__cp} -r web %{buildroot}%{webroot}
%{__install} -Dp -m0644 opensips-cp.httpd %{buildroot}%{_sysconfdir}/httpd/conf.d/opensips-cp.conf



%files
%{webroot}/*
%config(noreplace) %attr(-,root,root)  %{_sysconfdir}/httpd/conf.d/opensips-cp.conf

%doc



%changelog
* Tue Sep 5 2023 Trevor Steyn <trevor@webon.co.za> - 9.3.2
- New version and removed patch
* Tue Dec 11 2018 Trevor Steyn <trevor@webon.co.za> - 8.2.4-1
- New version
* Tue Dec 11 2018 Trevor Steyn <trevor@webon.co.za> - 7.2.3-2
- Added patch for Domain Attributes
* Mon Oct 29 2018 Trevor Steyn <trevor@webon.co.za> - 7.2.3-1
- First Release.

