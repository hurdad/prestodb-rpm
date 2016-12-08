%define __jar_repack %{nil}

Name:           presto-cli
Version:        %{PRESTO_VERSION}
Release:        1%{?dist}
Summary:        Presto DB CLI
Group:		System Environment/Libraries        
License:        ASL 2.0
URL:            http://prestodb.io/       
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch
Packager:       Alexander Hurd <hurdad@gmail.com>

%description
Presto DB CLI Tool

%prep

%build

%install
%{__rm} -rf %{buildroot}
%{__mkdir} -p %{buildroot}%{_bindir}
%{__install} -m 755 %{_topdir}/tmp/presto %{buildroot}%{_bindir}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{_bindir}/presto

%changelog
* Wed Jan 16 2014 Alexander Hurd <hurdad@gmail.com> 1.0.1-2
- Renaming from presto-cli to presto

* Wed Jan 1 2014 Alexander Hurd <hurdad@gmail.com> 1.0.1-1
- Initial specfile writeup.
