Summary:	Port scanner
Summary(pl):	Skaner portów
Name:		nmap
Version:	2.07
Release:	2d
Copyright:	GPL
Group:		Networking
Group(pl):   	Sieciowe
URL:		http://www.insecure.org/nmap/index.html
Source:		http://www.insecure.org/nmap/%{name}-%{version}.tgz
BuildRoot:	/tmp/buildroot-%{name}-%{version}
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
./configure %{_target} \
	--prefix=/usr

make CCOPT="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT/usr/{bin,lib,man/man1}

make \
    prefix=$RPM_BUILD_ROOT/usr \
    install

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man1/* 

%clean
rm -rf $RPM_BUILD_ROOT

%files 
%defattr(644,root,root,755)
%doc docs/*.html

%attr(755,root,root) /usr/bin/*

%dir %{_libdir}/nmap
%attr(755,root,root) %{_libdir}/nmap/*

%{_mandir}/man1/*

%changelog
* Thu Feb 18 1999 Wojtek ¦lusarczyk <wojtek@shadow.eu.org>
  [2.07-2d]
- fixed Group,
- removed gzipping html docs.

* Sat Feb 13 1999 Arkadiusz Mi¶kiewicz <misiek@misiek.eu.org>
- new upstream release
- few small changes

* Wed Dec 30 1998 Arkadiusz Mi¶kiewicz <misiek@misiek.eu.org>
- new upstream release

* Wed Dec 16 1998 Arkadiusz Mi¶kiewicz <misiek@misiek.eu.org>
- new upstream release

* Thu Nov 03 1998 Arkadiusz Mi¶kiewicz <misiek@misiek.eu.org>
- corrected spec file for Polish Linux Distribution

* Sat Oct 3 1998  Ian Macdonald <ianmacd@xs4all.nl>
- first RPM release
