Summary:	A slit pager for fluxbox
Summary(pl):	-
Name:		fluxter
Version:	0.1.0
Release:	1
License:	GPL
Group:		X11/Window Managers/Tools
Source0:	http://benedict.isomedia.com/homes/stevencooper/files/%{name}-%{version}.tar.gz
# Source0-md5:	6d18553220e8fc33c54762d2e7d31528
URL:		http://benedict.isomedia.com/homes/stevencooper/projects/fluxter.html
Requires:	fluxbox
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Fluxter is a workspace pager dockapp, particularly useful with the
Fluxbox window manager. It is largely based on bbpager for Blackbox.

%description -l pl

%prep
%setup -q

%build
rm -f missing
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README
%attr(755,root,root) %{_bindir}/*
%{_datadir}/fluxbox/%{name}.bb
%{_datadir}/fluxbox/%{name}.nobb
