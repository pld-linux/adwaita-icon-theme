Summary:	Adwaita icon theme for GNOME environment
Summary(pl.UTF-8):	Motyw ikon Adwaita dla środowiska GNOME
Name:		adwaita-icon-theme
Version:	48.1
Release:	1
License:	LGPL v3 or CC-BY-SA v3.0
Group:		Themes
Source0:	https://download.gnome.org/sources/adwaita-icon-theme/48/%{name}-%{version}.tar.xz
# Source0-md5:	a3923f90a1885cfc1d5b0626762ec0b7
URL:		https://www.gnome.org/
BuildRequires:	gtk-update-icon-cache
BuildRequires:	meson >= 0.64.0
BuildRequires:	ninja >= 1.5
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	rpmbuild(macros) >= 2.042
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
%meson

%meson_build

%install
rm -rf $RPM_BUILD_ROOT

%meson_install

> $RPM_BUILD_ROOT%{_iconsdir}/Adwaita/icon-theme.cache

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_icon_cache Adwaita

%postun
if [ "$1" != "0" ]; then
	%update_icon_cache Adwaita
fi

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING NEWS
%dir %{_iconsdir}/Adwaita
%{_iconsdir}/Adwaita/index.theme
%{_iconsdir}/Adwaita/16x16
%{_iconsdir}/Adwaita/cursors
%{_iconsdir}/Adwaita/scalable
%{_iconsdir}/Adwaita/symbolic
%ghost %{_iconsdir}/Adwaita/icon-theme.cache
%{_npkgconfigdir}/adwaita-icon-theme.pc
