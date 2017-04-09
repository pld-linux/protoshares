%define	snap	20131203
%define	rel	8
Summary:	ProtoShares
Name:		protoshares
Version:	0.8.5
Release:	1.%{snap}.%{rel}
License:	MIT/X11
Group:		X11/Applications
Source0:	ProtoShares-%{snap}.tar.bz2
# Source0-md5:	f18b07195152c72a1e322444d84b4543
Patch0:		boost-1.58.patch
URL:		http://invictus-innovations.com/protoshares
BuildRequires:	QtCore-devel
BuildRequires:	QtDBus-devel
BuildRequires:	QtGui-devel
BuildRequires:	boost-devel
BuildRequires:	db-cxx-devel
BuildRequires:	miniupnpc-devel >= 1.5
BuildRequires:	openssl-devel
BuildRequires:	qrencode-devel
BuildRequires:	qt4-qmake
Requires:	perl-base
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
ProtoShares

%package qt
Summary:	Qt-based ProtoShares Wallet
Group:		X11/Applications

%description qt
Qt-based ProtoShares Wallet.

%prep
%setup -q -n ProtoShares
%patch0 -p1

%build
qmake-qt4 protoshares-qt.pro \
	USE_UPNP=1 \
	USE_DBUS=1 \
	USE_QRCODE=1

%{__make}

qmake-qt4 protosharesd.pro

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{%{_bindir},%{_libdir}/%{name},%{_mandir}/man{1,5},%{_localedir},%{_desktopdir},%{_pixmapsdir},%{_datadir}/kde4/services}

install protoshares-qt $RPM_BUILD_ROOT%{_bindir}/protoshares-qt

sed -e 's#bitcoin#protoshares#g' contrib/debian/bitcoin-qt.desktop > $RPM_BUILD_ROOT%{_desktopdir}/protoshares-qt.desktop
sed -e 's#bitcoin#protoshares#g' contrib/debian/bitcoin-qt.protocol > $RPM_BUILD_ROOT%{_datadir}/kde4/services/protoshares-qt.protocol

%clean
rm -rf $RPM_BUILD_ROOT

%files
#%defattr(644,root,root,755)
#%doc doc/*.txt contrib/debian/examples/bitcoin.conf
#%attr(755,root,root) %{_bindir}/primeminer

%files qt
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/protoshares-qt
%{_datadir}/kde4/services/protoshares-qt.protocol
%{_desktopdir}/protoshares-qt.desktop
