Summary:	Network exploration tool and security scanner
Summary(es):	Herramienta de exploraciСn de la rede y seguridad
Summary(pl):	Programem do badania i audytu sieci
Summary(pt_BR):	Ferramenta de exploraГЦo da rede e seguranГa
Summary(ru):	Утилита сканирования сети и аудита безопасности
Summary(uk):	Утил╕та сканування мереж╕ та аудиту безпеки
Name:		nmap
Version:	3.00
Release:	1
License:	GPL
Group:		Networking
Source0:	http://www.insecure.org/nmap/dist/%{name}-%{version}.tgz
Source1:	%{name}.desktop
Source2:	%{name}.png
Patch0:		%{name}-DESTDIR.patch
#ipv6.patch based upon http://www.seb.peterson.easynet.be/nmap/nmap-2.54BETA36_ipv6.diff
Patch1:		%{name}-ipv6.patch
URL:		http://www.insecure.org/nmap/index.html
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gtk+-devel >= 1.0
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
connect(), TCP SYN (half open), ftp proxy (bounce attack),
Reverse-ident, ICMP (ping sweep), FIN, ACK sweep, Xmas Tree, SYN
sweep, and Null scan.

%description -l es
Nmap es un utilitario para la exploraciСn y auditorМa de redes.
Soporta "ping scanning", varias tИcnicas de bЗsqueda de puertos
abiertos, e identificaciСn remota de sistemas operacionales vМa
impresiones digitales TCP/IP.

%description -l pl
Nmap jest programem przeznaczonym do badania i audytu sieci. Wspiera
rС©ne techniki skanowania (badanie jakie usЁugi s╠ uruchomione na
danym ho╤cie), a tak©e TCP/IP fingerprinting (zdalne rozpoznawanie
typu systemu operacyjnego). Nmap oferuje rС©ne techniki skanowania
wykorzystuj╠ce: UDP, TCP connect(), TCP SYN (half open), ftp proxy
(bounce attack), Reverse-ident, ICMP (ping sweep), FIN, ACK sweep,
Xmas Tree, SYN sweep, and Null scan.

%description -l pt_BR
Nmap И um utilitАrio para a exploraГЦo e auditoria de redes. Ele
suporta "ping scanning", vАrias tИcnicas de procura por portas
abertas, e identificaГЦo remota de sistemas operacionais via
impressУes digitais TCP/IP.

%description -l ru
Nmap - это утилита для изучения сети и аудита безопасности. Она
поддерживает ping-сканирование (определение, какие хосты работают),
много методик сканирования портов (определение, какие сервисы
предоставляют хосты), и "отпечатки пальцев" TCP/IP (идентификация
операционной системы хоста). Nmap также поддерживает гибкое задание
цели и порта, скрытое сканирование (decoy scanning), определение
характеристик предсказуемости TCP sequence, сканирование sunRPC,
reverse-identd сканирование и другое.

%description -l uk
Nmap - це утил╕та для досл╕дження мереж╕ та аудиту безпеки. Вона
п╕дтриму╓ ping-сканування (визначення, як╕ хости працюють), багато
методик сканування порт╕в (визначення, як╕ серв╕си надають хости), та
"в╕дбитки пальц╕в" TCP/IP (╕дентиф╕кац╕я операц╕йно╖ системи хоста).
Nmap також п╕дтриму╓ гнучке задання ц╕л╕ та порта, приховане
сканування (decoy scanning), визначення характеристик передбачуваност╕
TCP sequence, сканування sunRPC, reverse-identd сканування та ╕нше.

%package X11
Summary:	Gtk+ frontend for nmap
Summary(pl):	Frontend Gtk+ dla nmapa
Summary(pt_BR):	Frontend gtk+ para o nmap
Summary(ru):	Gtk+ интерфейс для nmap
Summary(uk):	Gtk+ ╕нтерфейс для nmap
Group:		X11/Applications/Networking
Requires:	%{name} = %{version}
Obsoletes:	nmap-frontend

%description X11
This package includes nmapfe, a Gtk+ frontend for nmap.

%description X11 -l pl
Ten pakiet zawiera nmapfe, czyli frontend dla nmapa pisany z u©yciem
Gtk+.

%description X11 -l pt_BR
Frontend grАfico para o nmap (nmapfe) escrito em gtk+. NЦo contИm toda
a funcionalidade do nmap em si, mas И Зtil para usuАrios iniciantes.

%description X11 -l ru
Этот пакет содержит nmapfe, Gtk+ интерфейс для nmap.

%description X11 -l uk
Цей пакет м╕стить nmapfe, Gtk+ ╕нтерфейс для nmap.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
aclocal
%{__autoconf}
cd nbase
aclocal
%{__autoconf}
cd ../libpcap-possiblymodified
aclocal
%{__autoconf}
cd ../nmapfe
aclocal
%{__autoconf}
cd ..
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1,%{_datadir}/nmap} \
	$RPM_BUILD_ROOT{%{_prefix}/X11R6/bin,%{_prefix}/X11R6/man/man1} \
	$RPM_BUILD_ROOT{%{_applnkdir}/Network,%{_pixmapsdir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	deskdir=%{_applnkdir}/Network

install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/Network
install %{SOURCE2} $RPM_BUILD_ROOT%{_pixmapsdir}

%if %{!?_without_X:1}%{?_without_X:0}
mv -f $RPM_BUILD_ROOT%{_bindir}/nmapfe $RPM_BUILD_ROOT%{_prefix}/X11R6/bin
mv -f $RPM_BUILD_ROOT%{_mandir}/man1/{xnmap,nmapfe}.1 $RPM_BUILD_ROOT%{_prefix}/X11R6/man/man1
rm -f $RPM_BUILD_ROOT%{_bindir}/xnmap
ln -sf %{_prefix}/X11R6/bin/nmapfe $RPM_BUILD_ROOT%{_prefix}/X11R6/bin/xnmap
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc docs/*.txt CHANGELOG
%attr(755,root,root) %{_bindir}/nmap
%{_datadir}/nmap
%{_mandir}/man1/*

%if %{!?_without_X:1}%{?_without_X:0}
%files X11
%defattr(644,root,root,755)
%attr(755,root,root) %{_prefix}/X11R6/bin/nmapfe
%attr(755,root,root) %{_prefix}/X11R6/bin/xnmap
%{_prefix}/X11R6/man/man1/*
%{_applnkdir}/Network/nmap.desktop
%{_pixmapsdir}/*
%endif
