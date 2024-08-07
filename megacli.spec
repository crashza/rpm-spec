Name:           megacli
Version:        8.7.14
Release:        1%{?dist}
Summary:        LSI Logic MegaCLI

Group:          Applications/Communications
License:        Proprietary
URL:            http://www.lsilogic.com/

Source0: https://github.com/crashza/rpm-spec/raw/main/src/megacli-8.7.14.tar.gz

Requires:       bash
BuildArch:      x86_64


%description
Utility to manage and control LSI/megaraid controllers

%prep

%setup -q -n %{name}-%{version}
%{__mkdir} -p %{buildroot}/usr/sbin
%{__mkdir} -p %{buildroot}/usr/lib64
%{__install} -m 0755 %{name} %{buildroot}/usr/sbin/
%{__install} -m 0755 libstorelibir-2.so.14.07-0 %{buildroot}/usr/lib64/

%files
/usr/sbin/%{name}
/usr/lib64/libstorelibir-2.so.14.07-0

%doc

%changelog
* Fri Jun 28 2024 Trevor Steyn <trevor@webon.co.za> - 8.7.14
- First Release on Copr

