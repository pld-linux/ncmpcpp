Summary:	ncurses mpd client inspired by ncmpc
Summary(pl.UTF-8):	klient mpd wzorowany na ncmpc
Name:		ncmpcpp
Version:	0.5.8
Release:	1
License:	GPL v2
Group:		Applications
Source0:	http://unkart.ovh.org/ncmpcpp/%{name}-%{version}.tar.bz2
# Source0-md5:	288952c6b4cf4fa3683f3f83a58da37c
URL:		http://unkart.ovh.org/ncmpcpp/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	curl-devel
BuildRequires:	fftw3-devel
BuildRequires:	libmpdclient-devel >= 2.1
BuildRequires:	libstdc++-devel
BuildRequires:	libtool
BuildRequires:	ncurses-devel
BuildRequires:	pkgconfig
BuildRequires:	taglib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Ncmpcpp has UI very similar to ncmpc's one, but it provides new useful
features such as support for regular expressions in search engine,
extended song format, items filtering, last.fm support, ability to
sort playlist, local filesystem browser and other minor functions.

%description -l pl.UTF-8
Ncmpcpp posiada bardzo podobny interfejs użytkownika do tego znanego z
ncmpc, ale wspiera dodatkowo obsługę wyrażeń regularnych w wewnętrznej
wyszukiwarce, rozszerzony format piosenek, filtrowanie pozycji,
obsługę last.fm, umożliwia sortowanie playlisty, posiada przeglądarkę
plików lokalnych oraz inne drobne udogodnienia.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# clean up bogus docdir
%{__rm} -r $RPM_BUILD_ROOT%{_docdir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING NEWS doc/config doc/keys
%attr(755,root,root) %{_bindir}/ncmpcpp
%{_mandir}/man1/ncmpcpp.1*
