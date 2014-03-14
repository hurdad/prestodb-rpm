Name:           presto-jdbc
Version:        %{PRESTO_VERSION}
Release:        2%{?dist}
Summary:        PrestoDB JDBC Driver
Group:		System Environment/Libraries        
License:        ASL 2.0
URL:            http://prestodb.io/       
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch
Packager:       Alexander Hurd <hurdad@gmail.com>

%description
PrestoDB JDBC Driver

%prep

%build

%install
%{__rm} -rf %{buildroot}
%{__mkdir} -p %{buildroot}%{_datadir}/java
%{__install} -m 644 %{_topdir}/tmp/presto-jdbc-%{PRESTO_VERSION}-standalone.jar  %{buildroot}%{_datadir}/java/
ln -s %{_datadir}/java/presto-jdbc-%{PRESTO_VERSION}-standalone.jar  %{buildroot}%{_datadir}/java/presto-jdbc.jar

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{_datadir}/java

%changelog
* Thu Jan 16 2014 Alexander Hurd <hurdad@gmail.com> 1.0.1-1
- Initial specfile writeup.
