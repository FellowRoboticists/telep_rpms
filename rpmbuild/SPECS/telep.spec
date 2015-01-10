Name:		telep
Version:	0.1.1c
Release:	1%{?dist}
Summary:	The Erlang-based telep server application.

Group:		Robotics Application
License:	Proprietary
URL:		https://giskard.com
Source0:	%{name}-%{version}.tar.bz2
BuildRoot:	%(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
BuildArch:	i386

#BuildRequires:	
#Requires:	

%description
The Erlang-based Telepresence Server.


%prep
%setup -q


%build

# There's nothing to build for this guy.

%install
rm -rf %{buildroot}
# make install DESTDIR=%{buildroot}
mkdir -p %{buildroot}/usr/local
cp -R %{name} %{buildroot}/usr/local
mkdir -p %{buildroot}/var/www/telep/current
cp -R www/* %{buildroot}/var/www/telep/current
%{__install} -m 644 -Dp conf/telep.conf %{buildroot}/%{_sysconfdir}/telep/telep.conf
%{__install} -m 0755 -d %{buildroot}/var/log/telep

%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
%doc

/usr/local/%{name}
/var/www/telep
/etc/telep/telep.conf
%attr(-,telep,telep) /var/log/telep

%changelog
* Sat Jan 10 2015 Dave Sieh <dj0hnve@gmail.com> - 0.1.1c-1
- Fixed up the web server configuration.
* Sat Jan 10 2015 Dave Sieh <dj0hnve@gmail.com> - 0.1.1a-1
- First real attempt.
* Wed Jan 07 2015 Dave Sieh <dj0hnve@gmail.com> - 0.1.1-1
- Initial configuration.

