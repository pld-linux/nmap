Summary:	Port scanner
Summary(pl):	Skaner portów
Name:		nmap
Version:	2.12
Release:	1
Copyright:	GPL
Group:		Networking
Group(pl):   	Sieciowe
URL:		http://www.insecure.org/nmap/index.html
Source:		http://www.insecure.org/nmap/%{name}-%{version}.tgz
BuildRoot:	/tmp/%{name}-%{version}-root
Vendor:		Fyodor <fyodor@dhp.com>

%description
nmap is a utility for port scanning large networks, although it works
fine for single hosts.

%description -l pl
Nmap jest programem przeznaczonym do skanowania du¿ych sieci
jak i pojedynczych serwerów.

%prep
%setup -q

%build
CFLAGS=$RPM_OPT_FLAGS LDFLAGS=-s \
./configure %{_target_platform} \
	--prefix=%{_prefix}

make CCOPT="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{%{_bindir},%{_libdir},%{_mandir}/man1}

make \
    prefix=$RPM_BUILD_ROOT%{_prefix} \
    install

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man1/* 

%clean
rm -rf $RPM_BUILD_ROOT

%files 
%defattr(644,root,root,755)
%doc docs/*.html

%attr(755,root,root) %{_bindir}/*

%dir %{_libdir}/nmap
%attr(755,root,root) %{_libdir}/nmap/*

%{_mandir}/man1/*
