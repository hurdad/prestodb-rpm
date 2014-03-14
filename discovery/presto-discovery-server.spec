Name:           presto-discovery-server
Version:        %{VERSION}
Release:        2%{?dist}
Summary:        Presto Discovery Server
Group:		System Environment/Daemons       
License:        ASL 2.0
URL:            http://prestodb.io/       
Source0:        discovery-server-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires:       util-linux-ng
Packager:       Alexander Hurd <hurdad@gmail.com>

%description
PrestoDB Discovery Server

%prep
%setup -q -n discovery-server-%{VERSION}

%build

%install
%{__rm} -rf %{buildroot}

%{__mkdir} -p %{buildroot}%{_datadir}/discovery-server
%{__mkdir} -p %{buildroot}%{_sysconfdir}/discovery-server
%{__mkdir} -p %{buildroot}%{_initddir} 
%{__mkdir} -p %{buildroot}%{_sharedstatedir}/discovery-server
%{__mkdir} -p %{buildroot}%{_localstatedir}/run
%{__mkdir} -p %{buildroot}%{_localstatedir}/log

%{__cp} -rp %{_builddir}/discovery-server-%{VERSION}/* %{buildroot}%{_datadir}/discovery-server/
%{__cp} -rp %{_topdir}/configs/* %{buildroot}%{_sysconfdir}/discovery-server/
%{__cp} -rp %{_topdir}/../initscripts/discovery-server %{buildroot}%{_initddir}

ln -s %{_sharedstatedir}/discovery-server %{buildroot}%{_datadir}/discovery-server/data
ln -s %{_sysconfdir}/discovery-server %{buildroot}%{_datadir}/discovery-server/etc
ln -s %{_sharedstatedir}/discovery-server/var/log %{buildroot}%{_datadir}/discovery-server/log
ln -s %{_sharedstatedir}/discovery-server/var/log %{buildroot}%{_localstatedir}/log/discovery-server
ln -s %{_sharedstatedir}/discovery-server/var/run %{buildroot}%{_localstatedir}/run/discovery-server

%clean
%{__rm} -rf %{buildroot}

%post
#generate a uuid for the configuration
uuid=`uuidgen`
echo "node.environment=production
node.id=$uuid
node.data-dir=/var/lib/discovery-server" > /etc/discovery-server/node.properties
   
%preun
/etc/init.d/discovery-server stop

%files
%defattr(-,root,root,-)
%{_datadir}
%{_sysconfdir}
%{_localstatedir}

%changelog
* Wed Jan 1 2014 Alexander Hurd <hurdad@gmail.com> 1.0.1-1
- Initial specfile writeup.
