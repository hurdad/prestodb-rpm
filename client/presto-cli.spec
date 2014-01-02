Name:           presto-cli
Version:        %{PRESTO_VERSION}
Release:        1%{?dist}
Summary:        PrestoDB CLI
Group:		System Environment/Libraries        
License:        ASL 2.0
URL:            http://prestodb.io/       
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch
Requires:       java-1.7.0
Packager:       Alexander Hurd <hurdad@gmail.com>

%description
PrestoDB CLI Tool

%prep

%build

%install
%{__rm} -rf %{buildroot}
%{__mkdir} -p %{buildroot}%{_bindir}
%{__install} -m 755 %{_topdir}/tmp/presto-cli %{buildroot}%{_bindir}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{_bindir}/presto-cli

%changelog
* Wed Jan 1 2014 Alexander Hurd <hurdad@gmail.com> 1.0.1-1
- Initial specfile writeup.
