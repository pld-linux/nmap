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
BuildRoot:	/tmp/%{name}-%{version}-root

%description
nmap is a utility for port scanning large networks, although it works
fine for single hosts.

%description -l pl
Nmap jest programem przeznaczonym do skanowania du¿ych sieci
jak i pojedynczych serwerów.

%prep
%setup -q
%patch -p0

%build
CFLAGS="$RPM_OPT_FLAGS" LDFLAGS="-s" \
./configure \
	--prefix=%{_prefix} \
	--mandir=%{_mandir} \
	--libdir=%{_datadir}

make CCOPT="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1,%{datadir}/nmap}

make install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man1/* docs/*.txt

%clean
rm -rf $RPM_BUILD_ROOT

%files 
%defattr(644,root,root,755)
%doc docs/*.gz
%attr(755,root,root) %{_bindir}/*

%{_datadir}/nmap
%{_mandir}/man1/*
