Name:		ws_server
Version:	0.1.2
Release:	5%{?dist}
Summary:	Provides the telep ws_server.

Group:		Application
License:	Proprietary
URL:		https://github.com/FellowRoboticists/ws_server
Source0:	%{name}-%{version}.tar.bz2
BuildRoot:	%(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
BuildArch:	noarch

# BuildRequires:	
# Requires:	/usr/local/bin/node

%description
Deploys the ws_server NPM package. This provides a WebSocket
server for the telep environment.


%prep
%setup -q


%build

# There's nothing to build for this guy


%install
rm -rf %{buildroot}
# make install DESTDIR=%{buildroot}
%{__install} -m 644 -Dp ws_server.tar.gz %{buildroot}/opt/ws_server/ws_server.tar.gz
%{__install} -m 755 -Dp init/ws_server %{buildroot}/%{_initrddir}/ws_server
%{__install} -m 755 -Dp conf/ws_server %{buildroot}/%{_sysconfdir}/sysconfig/ws_server
%{__install} -m 0755 -d %{buildroot}/var/log/ws_server


%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
%doc

%{_initrddir}/ws_server
%config(noreplace) %{_sysconfdir}/sysconfig/ws_server
/opt/ws_server/ws_server.tar.gz
%attr(-,telep,telep) /var/log/ws_server

%post
# Attempt to have NPM install the package
/usr/local/bin/npm install -g /opt/ws_server/ws_server.tar.gz

%preun
# Attempt to uninstall the package
/usr/local/bin/npm uninstall -g ws_server

%changelog
* Tue Jan 06 2015 Dave Sieh <dj0hnve@gmail.com> - 0.1.2-5
- Corrected the command name - needed quotes.
* Sun Jan 04 2015 Dave Sieh <dj0hnve@gmail.com> - 0.1.2-4
- Updates to the init script and sysconfig.
* Sun Jan 04 2015 Dave Sieh <dj0hnve@gmail.com> - 0.1.2-3
- Creating the /var/log directory for ws_server
* Sun Jan 04 2015 Dave Sieh <dj0hnve@gmail.com> - 0.1.2-2
- Added the sysconfig file for ws_server
* Sun Jan 04 2015 Dave Sieh <dj0hnve@gmail.com> - 0.1.2-1
- Fixed bad json in package definition
* Sun Jan 04 2015 Dave Sieh <dj0hnve@gmail.com> - 0.1.1-1
- Fixed dependencies on the package
* Sat Jan 03 2015 Dave Sieh <dj0hnve@gmail.com> - 0.1.0-1
- Initial version
