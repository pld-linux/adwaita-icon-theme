Summary:	Adwaita icon theme for GNOME environment
Summary(pl.UTF-8):	Motyw ikon Adwaita dla środowiska GNOME
Name:		adwaita-icon-theme
Version:	3.32.0
Release:	1
License:	LGPL v3 or CC-BY-SA v3.0
Group:		Themes
Source0:	http://ftp.gnome.org/pub/GNOME/sources/adwaita-icon-theme/3.32/%{name}-%{version}.tar.xz
# Source0-md5:	4b16278cfed860a86c8221de62eec151
Patch0:		%{name}-noarch.patch
URL:		http://www.gnome.org/
BuildRequires:	autoconf >= 2.53
BuildRequires:	automake >= 1:1.9
BuildRequires:	gtk-update-icon-cache
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
%patch0 -p1

%build
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
%doc AUTHORS COPYING NEWS
%dir %{_iconsdir}/Adwaita
%{_iconsdir}/Adwaita/index.theme
%{_iconsdir}/Adwaita/[0-9]*x[0-9]*
%{_iconsdir}/Adwaita/cursors
%{_iconsdir}/Adwaita/scalable
%{_iconsdir}/Adwaita/scalable-up-to-32
%ghost %{_iconsdir}/Adwaita/icon-theme.cache
%{_npkgconfigdir}/adwaita-icon-theme.pc
