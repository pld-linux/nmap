Summary:     Port scanner
Name:	     nmap
Version:     2.07
Release:     1d
Copyright:   GPL
Group:	     Applications/Networking
Group(pl):   Aplikacje/Sieæ
URL:	     http://www.insecure.org/nmap/index.html
Source:	     http://www.insecure.org/nmap/%{name}-%{version}.tgz
BuildRoot:   /tmp/buildroot-%{name}-%{version}
Vendor:	     Fyodor <fyodor@dhp.com>
Summary(pl): Skaner portów

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
./configure --prefix=/usr

make CCOPT="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT/usr/{bin,lib,man/man1}
make install prefix=$RPM_BUILD_ROOT/usr

gzip -9nf $RPM_BUILD_ROOT/usr/man/man1/* docs/*.html

%clean
rm -rf $RPM_BUILD_ROOT

%files 
%defattr(644,root,root,755)
%doc docs/*.html.gz
%attr(755,root,root) /usr/bin/*
%attr(755,root,root) /usr/lib/nmap/*
%attr(644,root, man) /usr/man/man1/*
%dir /usr/lib/nmap

%changelog
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
