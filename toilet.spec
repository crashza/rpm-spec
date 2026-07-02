Summary:    The TOIlet project attempts to create a free replacement for the FIGlet utility.
Name:       toilet
Version:    0.3
Release:    1
License:    Artistic
URL:        http://caca.zoy.org/toilet.html
Source:     http://caca.zoy.org/files/toilet/%{name}-%{version}.tar.gz
Group:      Applications/Text
Buildroot:  %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Requires:   figlet libcaca
BuildRequires:  libcaca-devel gcc

%description
TOIlet stands for “The Other Implementation’s letters”, coined after
FIGlet’s “Frank, Ian and Glen’s letters”.

TOIlet is in its very early development phase. It uses the powerful
libcucul library to achieve various text-based effects. TOIlet implements
or plans to implement the following features:

    * The ability to load FIGlet fonts
    * Support for Unicode input and output
    * Support for colour output
    * Support for various output formats: HTML, IRC, ANSI...

TOIlet also aims for full FIGlet compatibility. It is currently able to
load FIGlet fonts and perform horizontal smushing. 

%prep
%setup -q

%build
%{configure}
%{__make}

%clean
rm -rf $RPM_BUILD_ROOT

%install
%{makeinstall}

%files
%defattr(-,root,root)
%doc ChangeLog COPYING NEWS README TODO
%attr(755,root,root) %{_bindir}/*
%attr(644,root,root) %{_mandir}/man?/*
%attr(644,root,root) %{_datadir}/figlet/*

%changelog
* Wed Nov 03 2010 Greg Wildman <greg@techno.co.za> 0.2-1
- Update to 0.2 release.

* Tue Sep 22 2009 Greg Wildman <greg@techno.co.za> 0.1-1
- Initial spec.
