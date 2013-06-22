Summary:	Note editor designed to remain simple to use
Name:		bijiben
Version:	3.8.3
Release:	1
License:	GPL v2
Group:		X11/Applications
Source0:	http://download.gnome.org/sources/bijiben/3.8/%{name}-%{version}.tar.xz
# Source0-md5:	2ddf2452c4d8e1f2c57ee1899d95673e
URL:		https://live.gnome.org/Bijiben
BuildRequires:	clutter-gtk-devel
BuildRequires:	gtk+3-webkit-devel
BuildRequires:	libxml2-devel
BuildRequires:	libzeitgeist-devel
BuildRequires:	pkg-config
BuildRequires:	tracker-devel
Requires(post,postun):	/usr/bin/gtk-update-icon-cache
Requires(post,postun):	glib-gio-gsettings
Requires(post,postun):	hicolor-icon-theme
Requires(post,postun):	desktop-file-utils
Requires:	gnome-shell
Suggests:	tracker
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_libexecdir	%{_libdir}/bijiben

%description
Note editor designed to remain simple to use.

%prep
%setup -q

%build
%configure \
	--disable-schemas-compile	\
	--disable-silent-rules
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name} --with-gnome

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_gsettings_cache
%update_icon_cache hicolor
%update_desktop_database

%postun
%update_gsettings_cache
%update_icon_cache hicolor
%update_desktop_database

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/bijiben
%{_datadir}/bijiben
%{_datadir}/dbus-1/services/org.gnome.Bijiben.SearchProvider.service
%{_datadir}/glib-2.0/schemas/org.gnome.bijiben.gschema.xml
%{_desktopdir}/bijiben.desktop
%{_iconsdir}/hicolor/*/apps/bijiben.*

%dir %{_libexecdir}
%attr(755,root,root) %{_libexecdir}/bijiben-shell-search-provider
%{_datadir}/gnome-shell/search-providers/bijiben-search-provider.ini

