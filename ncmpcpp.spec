Summary:	ncurses mpd client inspired by ncmpc
Summary(pl.UTF-8):	klient mpd wzorowany na ncmpc
Name:		ncmpcpp
Version:	0.10.1
Release:	4
License:	GPL v2
Group:		Applications
Source0:	https://github.com/ncmpcpp/ncmpcpp/archive/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	2c90b825291c51bd7630b909daee7cd6
URL:		https://github.com/ncmpcpp/ncmpcpp
BuildRequires:	autoconf >= 2.71
BuildRequires:	automake
BuildRequires:	boost-devel
BuildRequires:	curl-devel
BuildRequires:	fftw3-devel
BuildRequires:	gcc-c++ >= 6:4.6
BuildRequires:	libmpdclient-devel >= 2.8
BuildRequires:	libstdc++-devel >= 6:10
BuildRequires:	libtool
BuildRequires:	ncurses-devel
BuildRequires:	ncurses-ext-devel
BuildRequires:	pkgconfig
BuildRequires:	readline-devel
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
%configure \
	BOOST_LIB_SUFFIX="" \
	--enable-clock \
	--enable-outputs \
	--enable-visualizer
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
%doc AUTHORS CHANGELOG.md COPYING doc/bindings doc/config
%attr(755,root,root) %{_bindir}/ncmpcpp
%{_mandir}/man1/ncmpcpp.1*
