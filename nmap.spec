#
%bcond_with	system_dnet
#
Summary:	Network exploration tool and security scanner
Summary(es.UTF-8):	Herramienta de exploración de la rede y seguridad
Summary(pl.UTF-8):	Program do badania i audytu sieci
Summary(pt_BR.UTF-8):	Ferramenta de exploração da rede e segurança
Summary(ru.UTF-8):	Утилита сканирования сети и аудита безопасности
Summary(uk.UTF-8):	Утиліта сканування мережі та аудиту безпеки
Name:		nmap
Version:	5.21
Release:	5
License:	GPL v2 clarified, with OpenSSL exception
Group:		Networking/Utilities
Source0:	http://nmap.org/dist/%{name}-%{version}.tar.bz2
# Source0-md5:	f77fa51d89ab27d35e5cd87bb086b858
Patch0:		%{name}-am18.patch
Patch1:		%{name}-system-lua.patch
Patch2:		%{name}-system-dnet.patch
Patch3:		%{name}-desktop.patch
URL:		http://nmap.org/
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	gettext-devel
%{?with_system_dnet:BuildRequires:	libdnet-devel}
BuildRequires:	libpcap-devel
BuildRequires:	libstdc++-devel
BuildRequires:	libtool
BuildRequires:	lua51-devel >= 5.1
BuildRequires:	openssl-devel
BuildRequires:	pcre-devel
BuildRequires:	python-devel >= 1:2.4
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.167
BuildRequires:	sed >= 4.0
Requires:	ca-certificates
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Nmap is a utility for network exploration or security auditing. It
supports ping scanning (determine which hosts are up), many port
scanning techniques (determine what services the hosts are offering),
and TCP/IP fingerprinting (remote host operating system
identification). Nmap also offers flexible target and port
specification, decoy scanning, determination of TCP sequence
predictability characteristics, sunRPC scanning, reverse-identd
scanning, and more.

nmap supports a large number of scanning techniques such as: UDP, TCP
connect(), TCP SYN (half open), FTP proxy (bounce attack),
Reverse-ident, ICMP (ping sweep), FIN, ACK sweep, Xmas Tree, SYN
sweep, and Null scan.

%description -l es.UTF-8
Nmap es un utilitario para la exploración y auditoría de redes.
Soporta "ping scanning", varias técnicas de búsqueda de puertos
abiertos, e identificación remota de sistemas operacionales vía
impresiones digitales TCP/IP.

%description -l pl.UTF-8
Nmap jest programem przeznaczonym do badania i audytu sieci. Wspiera
różne techniki skanowania (badanie jakie usługi są uruchomione na
danym hoście), a także TCP/IP fingerprinting (zdalne rozpoznawanie
typu systemu operacyjnego). Nmap oferuje różne techniki skanowania
wykorzystujące: UDP, TCP connect(), TCP SYN (half open), FTP proxy
(bounce attack), Reverse-ident, ICMP (ping sweep), FIN, ACK sweep,
Xmas Tree, SYN sweep i Null scan.

%description -l pt_BR.UTF-8
Nmap é um utilitário para a exploração e auditoria de redes. Ele
suporta "ping scanning", várias técnicas de procura por portas
abertas, e identificação remota de sistemas operacionais via
impressões digitais TCP/IP.

%description -l ru.UTF-8
Nmap - это утилита для изучения сети и аудита безопасности. Она
поддерживает ping-сканирование (определение, какие хосты работают),
много методик сканирования портов (определение, какие сервисы
предоставляют хосты), и "отпечатки пальцев" TCP/IP (идентификация
операционной системы хоста). Nmap также поддерживает гибкое задание
цели и порта, скрытое сканирование (decoy scanning), определение
характеристик предсказуемости TCP sequence, сканирование sunRPC,
reverse-identd сканирование и другое.

%description -l uk.UTF-8
Nmap - це утиліта для дослідження мережі та аудиту безпеки. Вона
підтримує ping-сканування (визначення, які хости працюють), багато
методик сканування портів (визначення, які сервіси надають хости), та
"відбитки пальців" TCP/IP (ідентифікація операційної системи хоста).
Nmap також підтримує гнучке задання цілі та порта, приховане
сканування (decoy scanning), визначення характеристик передбачуваності
TCP sequence, сканування sunRPC, reverse-identd сканування та інше.

%package zenmap
Summary:	Graphical frontend for nmap
Summary(pl.UTF-8):	Graficzny frontend dla nmapa
Group:		X11/Applications/Networking
Requires:	%{name} = %{version}-%{release}
Requires:	bash
Requires:	python-pygtk-gtk >= 2:2.6
Requires:	python-sqlite >= 2.0
Provides:	nmap-X11
Obsoletes:	nmap-X11
Obsoletes:	nmap-frontend

%description zenmap
This package includes zenmap, a graphical frontend for nmap.

%description zenmap -l pl.UTF-8
Ten pakiet zawiera zenmap, czyli graficzny frontend dla nmapa.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
ln -s config/acinclude.m4 libdnet-stripped
%{__libtoolize}
find -type f -name configure.ac -o -name configure.in | while read CFG; do
	cd $(dirname "$CFG")
	%{__aclocal}
	%{__autoconf}
	cd "$OLDPWD"
done
cp -f /usr/share/automake/config.sub .

CXXFLAGS="%{rpmcxxflags} -fno-rtti -fno-exceptions"
CPPFLAGS="-I/usr/include/lua51"
%configure \
	LIBLUA_LIBS="-llua51" \
	--with-libdnet%{!?with_system_dnet:=included} \
	--with-liblua

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_pixmapsdir}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install docs/zenmap.1 $RPM_BUILD_ROOT%{_mandir}/man1

%py_ocomp $RPM_BUILD_ROOT%{py_sitescriptdir}
%py_comp $RPM_BUILD_ROOT%{py_sitescriptdir}
%py_postclean

ln -sf /etc/certs/ca-certificates.crt $RPM_BUILD_ROOT/%{_datadir}/ncat/ca-bundle.crt

# remove unneeded files
rm -f $RPM_BUILD_ROOT%{_bindir}/uninstall_zenmap

# fix locale names
mv $RPM_BUILD_ROOT%{_mandir}/{jp,ja}
mv $RPM_BUILD_ROOT%{_mandir}/pt{_PT,}
mv $RPM_BUILD_ROOT%{_mandir}/zh{,_CN}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
# note: COPYING contains important notes and clarifications
%doc docs/README docs/*.txt CHANGELOG COPYING
%attr(755,root,root) %{_bindir}/ncat
%attr(755,root,root) %{_bindir}/ndiff
%attr(755,root,root) %{_bindir}/nmap
%{_datadir}/nmap
%{_datadir}/ncat
%{_mandir}/man1/ncat.1*
%{_mandir}/man1/ndiff.1*
%{_mandir}/man1/nmap.1*
%lang(de) %{_mandir}/de/man1/nmap.1*
%lang(es) %{_mandir}/es/man1/nmap.1*
%lang(fr) %{_mandir}/fr/man1/nmap.1*
%lang(hr) %{_mandir}/hr/man1/nmap.1*
%lang(hu) %{_mandir}/hu/man1/nmap.1*
%lang(it) %{_mandir}/it/man1/nmap.1*
%lang(ja) %{_mandir}/ja/man1/nmap.1*
%lang(pl) %{_mandir}/pl/man1/nmap.1*
%lang(pt_BR) %{_mandir}/pt_BR/man1/nmap.1*
%lang(pt) %{_mandir}/pt/man1/nmap.1*
%lang(ro) %{_mandir}/ro/man1/nmap.1*
%lang(ru) %{_mandir}/ru/man1/nmap.1*
%lang(sk) %{_mandir}/sk/man1/nmap.1*
%lang(zh_CN) %{_mandir}/zh_CN/man1/nmap.1*

%files zenmap
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/nmapfe
%attr(755,root,root) %{_bindir}/xnmap
%attr(755,root,root) %{_bindir}/zenmap
%dir %{py_sitescriptdir}/radialnet
%dir %{py_sitescriptdir}/radialnet/bestwidgets
%dir %{py_sitescriptdir}/radialnet/core
%dir %{py_sitescriptdir}/radialnet/gui
%dir %{py_sitescriptdir}/radialnet/util
%dir %{py_sitescriptdir}/zenmapCore
%dir %{py_sitescriptdir}/zenmapGUI
%dir %{py_sitescriptdir}/zenmapGUI/higwidgets
%{py_sitescriptdir}/radialnet/*.py[co]
%{py_sitescriptdir}/radialnet/bestwidgets/*.py[co]
%{py_sitescriptdir}/radialnet/core/*.py[co]
%{py_sitescriptdir}/radialnet/gui/*.py[co]
%{py_sitescriptdir}/radialnet/util/*.py[co]
%{py_sitescriptdir}/zenmapCore/*.py[co]
%{py_sitescriptdir}/zenmapGUI/*.py[co]
%{py_sitescriptdir}/zenmapGUI/higwidgets/*.py[co]
%if "%{pld_release}" != "ac"
%{py_sitescriptdir}/zenmap-*.egg-info
%endif
%dir %{_datadir}/zenmap
%{_datadir}/zenmap/config
%{_datadir}/zenmap/docs
%{_datadir}/zenmap/misc
%dir %{_datadir}/zenmap/locale
%lang(de) %{_datadir}/zenmap/locale/de
%lang(fr) %{_datadir}/zenmap/locale/fr
%lang(hr) %{_datadir}/zenmap/locale/hr
%lang(pt_BR) %{_datadir}/zenmap/locale/pt_BR
%lang(ru) %{_datadir}/zenmap/locale/ru
%{_datadir}/zenmap/pixmaps
%{_datadir}/zenmap/su-to-zenmap.sh
%{_desktopdir}/zenmap-root.desktop
%{_desktopdir}/zenmap.desktop
%{_mandir}/man1/zenmap.1*
