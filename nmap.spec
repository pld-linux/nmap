Summary:	Port scanner
Summary(pl):	Skaner portów
Name:		nmap
Version:	2.12
Release:	1
Copyright:	GPL
Group:		Networking
Group(pl):   	Sieciowe
Source:		http://www.insecure.org/nmap/%{name}-%{version}.tgz
Patch:		nmap-DESTDIR.patch
URL:            http://www.insecure.org/nmap/index.html
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_libdir		%{_datadir}

%description
Nmap is designed to allow system administrators and curious individuals to
scan large networks to determine which hosts are up and what services they
are offering.

nmap supports a large number of scanning techniques such as: UDP, TCP
connect(), TCP SYN (half open), ftp proxy (bounce attack), Reverse-ident,
ICMP (ping sweep), FIN, ACK sweep, Xmas Tree, SYN sweep, and Null scan.

%description -l pl
Nmap jest programem przeznaczonym do skanowania du¿ych sieci
jak i pojedynczych serwerów w celu okre¶lenia które hosty w danym momencie
pracuja, a tak¿e jakie serwisy oferuj±.

nmap oferuje ró¿ne techniki skanowania wykorzystuj±ce: UDP, TCP connect(),
TCP SYN (half open), ftp proxy (bounce attack), Reverse-ident,
ICMP (ping sweep), FIN, ACK sweep, Xmas Tree, SYN sweep, and Null scan.

%prep
%setup -q
%patch -p0

%build
LDFLAGS="-s"; export LDFLAGS
%configure
cd libpcap-possiblymodified
%configure
cd ..

%{__make} CCOPT="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1,%{datadir}/nmap}

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man1/* docs/*.txt

%clean
rm -rf $RPM_BUILD_ROOT

%files 
%defattr(644,root,root,755)
%doc docs/*.gz
%attr(755,root,root) %{_bindir}/*

%{_datadir}/nmap
%{_mandir}/man1/*
