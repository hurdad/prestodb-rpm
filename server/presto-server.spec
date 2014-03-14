Name:           presto-server
Version:        %{VERSION}
Release:        2%{?dist}
Summary:        Presto Server
Group:		System Environment/Daemons       
License:        ASL 2.0
URL:            http://prestodb.io/       
Source0:        presto-server-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires:       util-linux-ng
Packager:       Alexander Hurd <hurdad@gmail.com>

%description
PrestoDB Server

%prep
%setup -q -n presto-server-%{VERSION}

%build

%install
%{__rm} -rf %{buildroot}

%{__mkdir} -p %{buildroot}%{_datadir}/presto-server/
%{__mkdir} -p %{buildroot}%{_sysconfdir}/presto-server/
%{__mkdir} -p %{buildroot}%{_initddir} 
%{__mkdir} -p %{buildroot}%{_sharedstatedir}/presto-server/
%{__mkdir} -p %{buildroot}%{_localstatedir}/run
%{__mkdir} -p %{buildroot}%{_localstatedir}/log

%{__cp} -rp %{_builddir}/presto-server-%{VERSION}/* %{buildroot}%{_datadir}/presto-server/
%{__cp} -rp %{_topdir}/configs/* %{buildroot}%{_sysconfdir}/presto-server/
%{__cp} -rp %{_topdir}/../initscripts/presto-server %{buildroot}%{_initddir}

ln -s %{_sharedstatedir}/presto-server %{buildroot}%{_datadir}/presto-server/data
ln -s %{_sysconfdir}/presto-server %{buildroot}%{_datadir}/presto-server/etc
ln -s %{_sharedstatedir}/presto-server/var/log %{buildroot}%{_datadir}/presto-server/log
ln -s %{_sharedstatedir}/presto-server/var/log %{buildroot}%{_localstatedir}/log/presto-server
ln -s %{_sharedstatedir}/presto-server/var/run %{buildroot}%{_localstatedir}/run/presto-server

%clean
%{__rm} -rf %{buildroot}

%post
#generate a uuid for the configuration
uuid=`uuidgen`
echo "node.environment=production
node.id=$uuid
node.data-dir=/var/lib/presto-server" > /etc/presto-server/node.properties   

%preun
/etc/init.d/presto-server stop

%files
%defattr(-,root,root,-)
%{_datadir}
%{_sysconfdir}
%{_localstatedir}

%changelog
* Wed Jan 1 2014 Alexander Hurd <hurdad@gmail.com> 1.0.1-1
- Initial specfile writeup.
