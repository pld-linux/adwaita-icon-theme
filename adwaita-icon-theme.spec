Summary:	Adwaita icon theme for GNOME environment
Summary(pl.UTF-8):	Motyw ikon Adwaita dla środowiska GNOME
Name:		adwaita-icon-theme
Version:	3.16.0
Release:	2
License:	LGPL v3 or CC-BY-SA v3.0
Group:		Themes
Source0:	http://ftp.gnome.org/pub/GNOME/sources/adwaita-icon-theme/3.16/%{name}-%{version}.tar.xz
# Source0-md5:	cd4bdd988fe15ec31796950c690b8d27
URL:		http://www.gnome.org/
BuildRequires:	autoconf >= 2.53
BuildRequires:	automake >= 1:1.9
BuildRequires:	gettext-devel
BuildRequires:	glib2-devel >= 2.0
BuildRequires:	intltool >= 0.40.0
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	rpmbuild(macros) >= 1.601
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires(post):	gtk-update-icon-cache >= 3.14
Conflicts:	gnome-themes-standard < 3.14
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Adwaita icon theme for GNOME environment.

%description -l pl.UTF-8
Motyw ikon Adwaita dla środowiska GNOME.

%prep
%setup -q

%build
%{__glib_gettextize}
%{__intltoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	GTK_UPDATE_ICON_CACHE=/bin/true
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	install_sh="install -p" \
	DESTDIR=$RPM_BUILD_ROOT

> $RPM_BUILD_ROOT%{_iconsdir}/Adwaita/icon-theme.cache

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_icon_cache Adwaita

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING NEWS README
%dir %{_iconsdir}/Adwaita
%{_iconsdir}/Adwaita/index.theme
%{_iconsdir}/Adwaita/[0-9]*x[0-9]*
%{_iconsdir}/Adwaita/cursors
%{_iconsdir}/Adwaita/scalable
%{_iconsdir}/Adwaita/scalable-up-to-32
%ghost %{_iconsdir}/Adwaita/icon-theme.cache
%{_npkgconfigdir}/adwaita-icon-theme.pc
