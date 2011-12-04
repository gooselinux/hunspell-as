Name: hunspell-as
Summary: Assamese hunspell dictionaries
Version: 1.0.3
Release: 3.1%{?dist}
Group: Applications/Text
Source: http://extensions.services.openoffice.org/files/2318/4/as_IN.oxt
URL: http://extensions.services.openoffice.org/project/AssameseDict
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
License: GPLv2+ or LGPLv2+ or MPLv1.1
BuildArch: noarch

Requires: hunspell

%description
Assamese hunspell dictionaries.

%prep
%setup -q -c -n hunspell-as

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/myspell
cp -p as_IN.* $RPM_BUILD_ROOT/%{_datadir}/myspell/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc README_as_IN.txt COPYING COPYING.MPL COPYING.GPL COPYING.LGPL

%{_datadir}/myspell/*

%changelog
* Mon Nov 30 2009 Dennis Gregorovic <dgregor@redhat.com> - 1.0.3-3.1
- Rebuilt for RHEL 6

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Apr 29 2009 Parag <pnemade@redhat.com> - 1.0.3-2
- Fix source issue in cvs

* Tue Apr 28 2009 Caolan McNamara <caolanm@redhat.com> - 1.0.3-1
- initial version
