Summary:	A slit pager for fluxbox
Summary(pl):	Pager dla fluxboksa
Name:		fluxter
Version:	0.1.0
Release:	2
License:	GPL v2
Group:		X11/Window Managers/Tools
Source0:	http://benedict.isomedia.com/homes/stevencooper/files/%{name}-%{version}.tar.gz
# Source0-md5:	6d18553220e8fc33c54762d2e7d31528
URL:		http://benedict.isomedia.com/homes/stevencooper/projects/fluxter.html
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	XFree86-devel
Requires:	fluxbox
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Fluxter is a workspace pager dockapp, particularly useful with the
Fluxbox window manager. It is largely based on bbpager for Blackbox.

%description -l pl
Fluxter to dokowalna aplikacja s³u¿±ca do prze³±czania biurek,
u¿yteczna szczególnie w po³±czeniu z zarz±dc± okien Fluxbox. W du¿ej
czê¶ci jest oparta na bbpagerze z Blackboksa.

%prep
%setup -q

%build
rm -f missing
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--with-x

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS BUGS ChangeLog INSTALL NEWS README TODO
%attr(755,root,root) %{_bindir}/*
%{_datadir}/fluxbox/%{name}.bb
%{_datadir}/fluxbox/%{name}.nobb
