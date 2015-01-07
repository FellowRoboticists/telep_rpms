Name:		telep-credentials
Version:	0.1.0
Release:	2%{?dist}
Summary:	Provides the secure credentials for the telep server.

Group:		Application
License:	Proprietary
URL:		https://daneel.com
Source0:	%{name}-%{version}.tar.bz2
BuildRoot:	%(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
BuildArch:	noarch

# BuildRequires:	
# Requires:	

%description
Deploys the credentials required to operate the telep application.

%prep
%setup -q


%build

# There's nothing to build for this guy

%install
rm -rf %{buildroot}
# make install DESTDIR=%{buildroot}

%{__install} -m 644 -Dp user.lst %{buildroot}/%{_sysconfdir}/telep/user.lst
%{__install} -m 644 -Dp group.lst %{buildroot}/%{_sysconfdir}/telep/group.lst
%{__install} -m 644 -Dp minion_public.pem %{buildroot}/%{_sysconfdir}/telep/minion_public.pem
%{__install} -m 644 -Dp telep_private.pem %{buildroot}/%{_sysconfdir}/telep/telep_private.pem
%{__install} -m 644 -Dp giskard-telep.crt %{buildroot}/%{_sysconfdir}/pki/tls/certs/giskard-telep.crt
%{__install} -m 644 -Dp giskard-telep.key %{buildroot}/%{_sysconfdir}/pki/tls/private/giskard-telep.key

%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
%doc

%{_sysconfdir}/telep/user.lst
%{_sysconfdir}/telep/group.lst
%{_sysconfdir}/telep/minion_public.pem
%{_sysconfdir}/telep/telep_private.pem
%{_sysconfdir}/pki/tls/certs/giskard-telep.crt
%{_sysconfdir}/pki/tls/private/giskard-telep.key


%changelog
* Mon Jan 05 2015 Dave Sieh <dj0hnve@gmail.com> - 0.1.0-2
- Added web server CRT and private key
* Mon Jan 05 2015 Dave Sieh <dj0hnve@gmail.com> - 0.1.0-1
- Initial package creation.
