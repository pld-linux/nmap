Summary:	Port scanner
Summary(es):	Herramienta de exploración de la rede y seguridad
Summary(pl):	Skaner portów
Summary(pt_BR):	Ferramenta de exploração da rede e segurança
Name:		nmap
Version:	2.54BETA30
Release:	1
License:	GPL
Group:		Networking
Source0:	http://www.insecure.org/nmap/dist/%{name}-%{version}.tgz
Patch0:		%{name}-DESTDIR.patch
Patch1:		%{name}-time.patch
URL:		http://www.insecure.org/nmap/index.html
BuildRequires:	gtk+-devel >= 1.0
BuildRequires:	autoconf
BuildRequires:	automake
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Nmap is designed to allow system administrators and curious
individuals to scan large networks to determine which hosts are up and
what services they are offering.

nmap supports a large number of scanning techniques such as: UDP, TCP
connect(), TCP SYN (half open), ftp proxy (bounce attack),
Reverse-ident, ICMP (ping sweep), FIN, ACK sweep, Xmas Tree, SYN
sweep, and Null scan.

%description -l es
Nmap es un utilitario para la exploración y auditoría de redes.
Soporta "ping scanning", varias técnicas de búsqueda de puertos
abiertos, e identificación remota de sistemas operacionales vía
impresiones digitales TCP/IP.

%description -l pl
Nmap jest programem przeznaczonym do skanowania du¿ych sieci jak i
pojedynczych serwerów w celu okre¶lenia które hosty w danym momencie
pracuja, a tak¿e jakie serwisy oferuj±.

nmap oferuje ró¿ne techniki skanowania wykorzystuj±ce: UDP, TCP
connect(), TCP SYN (half open), ftp proxy (bounce attack),
Reverse-ident, ICMP (ping sweep), FIN, ACK sweep, Xmas Tree, SYN
sweep, and Null scan.

%description -l pt_BR
Nmap é um utilitário para a exploração e auditoria de redes. Ele
suporta "ping scanning", várias técnicas de procura por portas
abertas, e identificação remota de sistemas operacionais via
impressões digitais TCP/IP.

%package X11
Summary:	Gtk+ frontend for nmap
Summary(pl):	Frontend Gtk+ dla nmapa
Summary(pt_BR):	Frontend gtk+ para o nmap
Group:		X11/Applications/Networking
Requires:	%{name} = %{version}
Requires:	gtk+
Obsoletes:	nmap-frontend

%description X11
This package includes nmapfe, a Gtk+ frontend for nmap.

%description X11 -l pl
Ten pakiet zawiera nmapfe, czyli frontend dla nmapa pisany z u¿yciem
Gtk+.

%description X11 -l pt_BR
Frontend gráfico para o nmap (nmapfe) escrito em gtk+. Não contém toda
a funcionalidade do nmap em si, mas é útil para usuários iniciantes.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
aclocal
autoconf
(cd nbase
aclocal
autoconf)
(cd libpcap-possiblymodified
aclocal
autoconf)
(cd nmapfe
aclocal
autoconf)
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1,%{_datadir}/nmap} \
	$RPM_BUILD_ROOT{%{_prefix}/X11R6/bin,%{_prefix}/X11R6/man/man1} \
	$RPM_BUILD_ROOT%{_applnkdir}/Network

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	deskdir=%{_applnkdir}/Network

%if %{!?_without_X:1}%{?_without_X:0}
mv -f $RPM_BUILD_ROOT%{_bindir}/nmapfe $RPM_BUILD_ROOT%{_prefix}/X11R6/bin
mv -f $RPM_BUILD_ROOT%{_mandir}/man1/{xnmap,nmapfe}.1 $RPM_BUILD_ROOT%{_prefix}/X11R6/man/man1
rm -f $RPM_BUILD_ROOT%{_bindir}/xnmap
ln -sf %{_prefix}/X11R6/bin/nmapfe $RPM_BUILD_ROOT%{_prefix}/X11R6/bin/xnmap
%endif

gzip -9nf docs/*.txt CHANGELOG

%clean
rm -rf $RPM_BUILD_ROOT

%files 
%defattr(644,root,root,755)
%doc docs/*.gz *.gz
%attr(755,root,root) %{_bindir}/*
%{_datadir}/nmap
%{_mandir}/man1/*

%if %{!?_without_X:1}%{?_without_X:0}
%files X11
%defattr(644,root,root,755)
%attr(755,root,root) %{_prefix}/X11R6/bin/nmapfe
%attr(755,root,root) %{_prefix}/X11R6/bin/xnmap
%{_prefix}/X11R6/man/man1/*
%{_applnkdir}/Network/nmapfe.desktop
%endif
