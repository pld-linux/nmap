#
# Conditional build:
%bcond_without	x	# don't build gtk-based nmap-X11
#
Summary:	Network exploration tool and security scanner
Summary(es.UTF-8):   Herramienta de exploración de la rede y seguridad
Summary(pl.UTF-8):   Program do badania i audytu sieci
Summary(pt_BR.UTF-8):   Ferramenta de exploração da rede e segurança
Summary(ru.UTF-8):   Утилита сканирования сети и аудита безопасности
Summary(uk.UTF-8):   Утиліта сканування мережі та аудиту безпеки
Summary(zh_CN.UTF-8):   [系统]强力端口扫描器
Summary(zh_TW.UTF-8):   [.)B系.$)B統].)B強力.$)B端.)B口.$)B掃.)B描.$)B器
Name:		nmap
Version:	4.20
Release:	1
License:	GPL
Group:		Networking
Source0:	http://www.insecure.org/nmap/dist/%{name}-%{version}.tar.bz2
# Source0-md5:	ea50419f99472200c4184a304e3831ea
Source1:	%{name}.png
Patch0:		%{name}-desktop.patch
Patch1:		%{name}-statistics.patch
Patch2:		%{name}-am18.patch
URL:		http://www.insecure.org/nmap/index.html
BuildRequires:	autoconf
BuildRequires:	automake
%{?with_x:BuildRequires:	gtk+2-devel >= 2.0}
BuildRequires:	libstdc++-devel
BuildRequires:	openssl-devel
BuildRequires:	pcre-devel
%{?with_x:BuildRequires:	pkgconfig}
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

%package X11
Summary:	GTK+ frontend for nmap
Summary(pl.UTF-8):   Frontend GTK+ dla nmapa
Summary(pt_BR.UTF-8):   Frontend GTK+ para o nmap
Summary(ru.UTF-8):   GTK+ интерфейс для nmap
Summary(uk.UTF-8):   GTK+ інтерфейс для nmap
Group:		X11/Applications/Networking
Requires:	%{name} = %{version}-%{release}
Obsoletes:	nmap-frontend

%description X11
This package includes nmapfe, a GTK+ frontend for nmap.

%description X11 -l pl.UTF-8
Ten pakiet zawiera nmapfe, czyli frontend dla nmapa pisany z użyciem
GTK+.

%description X11 -l pt_BR.UTF-8
Frontend gráfico para o nmap (nmapfe) escrito em GTK+. Não contém toda
a funcionalidade do nmap em si, mas é útil para usuários iniciantes.

%description X11 -l ru.UTF-8
Этот пакет содержит nmapfe, GTK+ интерфейс для nmap.

%description X11 -l uk.UTF-8
Цей пакет містить nmapfe, GTK+ інтерфейс для nmap.

%prep
%setup -q
%patch0 -p1
#patch1 -p1
%patch2 -p1

%build
cp -f /usr/share/automake/config.sub .
%{__aclocal}
%{__autoconf}
cd nbase
cp -f /usr/share/automake/config.sub .
# AC_C___ATTRIBUTE__
tail -n +302 aclocal.m4 >> acinclude.m4
%{__aclocal}
%{__autoconf}
cd ../libpcap
cp -f /usr/share/automake/config.sub .
# don't run aclocal - only local macros here!
%{__autoconf}
cd ../nmapfe
cp -f /usr/share/automake/config.sub .
%{!?with_x:echo 'AC_DEFUN([AM_PATH_GTK_2_0],[AC_DEFINE(MISSING_GTK)])' >> acinclude.m4}
%{__aclocal}
%{__autoconf}
cd ../nsock/src
cp -f /usr/share/automake/config.sub .
cd ../..
cp -f /usr/share/automake/config.sub libdnet-stripped/config
CXXFLAGS="%{rpmcflags} -fno-rtti -fno-exceptions"
%configure \
	--enable-ipv6 \
	%{!?with_x:--without-nmapfe}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_pixmapsdir}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	deskdir=%{_desktopdir}

%if %{with x}
cd $RPM_BUILD_ROOT%{_bindir}
rm -f xnmap
ln -s nmapfe xnmap
cd -

install %{SOURCE1} $RPM_BUILD_ROOT%{_pixmapsdir}
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc docs/*.txt CHANGELOG
%attr(755,root,root) %{_bindir}/nmap
%{_datadir}/nmap
%{_mandir}/man1/nmap.1*

%if %{with x}
%files X11
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/nmapfe
%attr(755,root,root) %{_bindir}/xnmap
%{_mandir}/man1/nmapfe.1*
%{_mandir}/man1/xnmap.1*
%{_desktopdir}/nmapfe.desktop
%{_pixmapsdir}/nmap.png
%endif
