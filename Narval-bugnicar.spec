%define short_name bugnicar

Summary:	Assistant that manages bugs
Summary(pl):	Asystent do zarz±dzania pluskwami
Name:		Narval-%{short_name}
Version:	20011016
Release:	1
Source0:	ftp://ftp.logilab.org/pub/narval/applications/%{short_name}-%{version}.npm
License:	GPL
Group:		Applications
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Requires:	Narval
Url:		http://www.logilab.org/narval/app.html

%description
Bugnicar is an extension set for Narval.

It provides a set up for an assistant that manages bugs.


%description -l pl
Bugnicar to zestaw rozszerzeñ dla Narvala.

Dostarcza konfiguracji asystenta który zarz±dza pluskwami.

%prep

%build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/%{_datadir}/narval/apps
install %{SOURCE0} $RPM_BUILD_ROOT/%{_datadir}/narval/apps

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_datadir}/narval/apps/*
