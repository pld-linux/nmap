#
# Conditional build:
%bcond_with	system_dnet	# use system libdnet instead of local modified version
%bcond_without	python		# Python2 based scripts (zenmap, ndiff)
%bcond_without	lua		# Nmap Scripting Engine (lua based)

Summary:	Network exploration tool and security scanner
Summary(es.UTF-8):	Herramienta de exploración de la rede y seguridad
Summary(pl.UTF-8):	Program do badania i audytu sieci
Summary(pt_BR.UTF-8):	Ferramenta de exploração da rede e segurança
Summary(ru.UTF-8):	Утилита сканирования сети и аудита безопасности
Summary(uk.UTF-8):	Утиліта сканування мережі та аудиту безпеки
Name:		nmap
Version:	7.92
Release:	2
License:	Nmap Public Source License
Group:		Networking/Utilities
Source0:	https://nmap.org/dist/%{name}-%{version}.tar.bz2
# Source0-md5:	849f7298a786ce4cd5728db989cff763
Patch0:		%{name}-desktop.patch
Patch1:		ncat-system-ssl.patch
Patch2:		%{name}-pythondir.patch
URL:		http://nmap.org/
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	gettext-tools
%{?with_system_dnet:BuildRequires:	libdnet-devel}
BuildRequires:	liblinear-devel
BuildRequires:	libpcap-devel
BuildRequires:	libstdc++-devel
BuildRequires:	libtool
%{?with_lua:BuildRequires:	lua53-devel >= 5.3}
BuildRequires:	openssl-devel
BuildRequires:	pcre-devel
BuildRequires:	python-devel >= 1:2.4
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.672
BuildRequires:	sed >= 4.0
%if %{with python}
Suggests:	%{name}-ndiff = %{version}-%{release}
%endif
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

#java code is run on target
%define		_noautoreqfiles	%{_datadir}/nmap/nselib/data/jdwp-class/.*

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

%package java
Summary:	NSE scripts that require java
Group:		Applications/Networking
Requires:	%{name} = %{version}-%{release}

%description java
NSE scripts that require java.

%package ncat
Summary:	Nmap's Netcat replacement
Summary(pl.UTF-8):	Zamiennik Netcata z pakietu Nmap
Group:		Applications/System
Requires:	ca-certificates
Provides:	nc
Conflicts:	nmap < 6.47-3

%description ncat
Ncat is a feature packed networking utility which will read and write
data across a network from the command line. It uses both TCP and UDP
for communication and is designed to be a reliable back-end tool to
instantly provide network connectivity to other applications and
users. Ncat will not only work with IPv4 and IPv6 but provides the
user with a virtually limitless number of potential uses.

%description ncat -l pl.UTF-8
Ncat to narzędzie sieciowe o wielu możliwościach, czytające i
zapisujące dane przez sieć z linii poleceń. Do komunikacji używa
zarówno TCP, jak i UDP; jest zaprojektowane jako wiarygodne narzędzie
backendowe, zapewniające łączność sieciową dla innych aplikacji i
użytkowników. Działa nie tylko z IPv4 i IPv6, ale udostępnia
użytkownikowi praktycznie nieograniczoną liczbę potencjalnych
zastosowań.

%package ndiff
Summary:	ndiff - utility to compare the results of Nmap scans
Summary(pl.UTF-8):	ndiff - narzędzie do porównywania wyników skanowań Nmapa
Group:		Applications/Networking
Conflicts:	nmap < 7.91-2

%description ndiff
Ndiff is a tool to aid in the comparison of Nmap scans. It takes two
Nmap XML output files and prints the differences between them.

%description ndiff -l pl.UTF-8
Ndiff to narzędzie pomagające przy porównywaniu wyników skanowań
Nmapa. Przyjmuje dwa pliki wyjściowe Nmapa w formacie XML i wypisuje
różnice między nimi.

%package zenmap
Summary:	Graphical frontend for nmap
Summary(pl.UTF-8):	Graficzny frontend dla nmapa
Group:		X11/Applications/Networking
Requires:	%{name} = %{version}-%{release}
Requires:	bash
Requires:	python-pygtk-gtk >= 2:2.6
Requires:	python-sqlite >= 2.0
Suggests:	gksu
Provides:	nmap-X11
Obsoletes:	nmap-X11 < 4.53
Obsoletes:	nmap-frontend < 3

%description zenmap
This package includes zenmap, a graphical frontend for nmap.

%description zenmap -l pl.UTF-8
Ten pakiet zawiera zenmap, czyli graficzny frontend dla nmapa.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
# use system provided libraries
%{__rm} -r liblinear liblua libpcap libpcre libssh2 libz

%build
CPPFLAGS="-I/usr/include/lua5.3"
%configure \
	%{?with_lua:LIBLUA_LIBS="-llua5.3"} \
	--with-liblinear \
	--with%{!?with_lua:out}-liblua \
	--with-libdnet%{!?with_system_dnet:=included} \
	--with%{!?with_python:out}-zenmap \
	--with%{!?with_python:out}-ndiff \
	STRIP=/bin/true

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_pixmapsdir}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%if %{with python}
cp -p docs/zenmap.1 $RPM_BUILD_ROOT%{_mandir}/man1

%py_ocomp $RPM_BUILD_ROOT%{py_sitescriptdir}
%py_comp $RPM_BUILD_ROOT%{py_sitescriptdir}
%py_postclean

# remove unneeded files
%{__rm} $RPM_BUILD_ROOT%{_bindir}/uninstall_zenmap
%{__rm} $RPM_BUILD_ROOT%{_bindir}/uninstall_ndiff

# unify locale names
%{__mv} $RPM_BUILD_ROOT%{_datadir}/zenmap/locale/zh{,_CN}
%endif

# unify locale names
%{__mv} $RPM_BUILD_ROOT%{_mandir}/pt{_PT,}
%{__mv} $RPM_BUILD_ROOT%{_mandir}/zh{,_CN}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc docs/README docs/*.txt CHANGELOG HACKING
%attr(755,root,root) %{_bindir}/nmap
%attr(755,root,root) %{_bindir}/nping
%{_datadir}/nmap
%exclude %{_datadir}/nmap/nselib/data/jdwp-class
%exclude %{_datadir}/nmap/scripts/jdwp-*
%{_mandir}/man1/nmap.1*
%{_mandir}/man1/nping.1*
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

%files java
%defattr(644,root,root,755)
%{_datadir}/nmap/nselib/data/jdwp-class
%{_datadir}/nmap/scripts/jdwp-*

%files ncat
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/ncat
%{_mandir}/man1/ncat.1*

%if %{with python}
%files ndiff
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/ndiff
%{_mandir}/man1/ndiff.1*
%{py_sitescriptdir}/ndiff.py[co]

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
%{py_sitescriptdir}/zenmap-%{version}-py*.egg-info
%dir %{_datadir}/zenmap
%{_datadir}/zenmap/config
%{_datadir}/zenmap/docs
%{_datadir}/zenmap/misc
%dir %{_datadir}/zenmap/locale
%lang(de) %{_datadir}/zenmap/locale/de
%lang(es) %{_datadir}/zenmap/locale/es
%lang(fr) %{_datadir}/zenmap/locale/fr
%lang(hi) %{_datadir}/zenmap/locale/hi
%lang(hr) %{_datadir}/zenmap/locale/hr
%lang(it) %{_datadir}/zenmap/locale/it
%lang(ja) %{_datadir}/zenmap/locale/ja
%lang(pl) %{_datadir}/zenmap/locale/pl
%lang(pt_BR) %{_datadir}/zenmap/locale/pt_BR
%lang(ru) %{_datadir}/zenmap/locale/ru
%lang(zh_CN) %{_datadir}/zenmap/locale/zh_CN
%{_datadir}/zenmap/pixmaps
%attr(755,root,root) %{_datadir}/zenmap/su-to-zenmap.sh
%{_desktopdir}/zenmap-root.desktop
%{_desktopdir}/zenmap.desktop
%{_mandir}/man1/zenmap.1*
%endif
