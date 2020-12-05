Summary:	A HTTP(S)/FTP(S) application load stress testing tool
Name:		curl-loader
Version:	0.56
Release:	1
License:	GPLv2
Group:		System/Servers
Url:		http://curl-loader.sourceforge.net/
Source0:	http://sunet.dl.sourceforge.net/project/curl-loader/curl-loader/%{name}-%{version}/%{name}-%{version}.tar.bz2
Patch0:		curl-loader-0.53-link.patch
Patch1:		curl-loader-0.50-hack.diff
BuildRequires:	pkgconfig(libcurl)
BuildRequires:	pkgconfig(libevent)
BuildRequires:	pkgconfig(openssl)

%description
curl-loader is an open-source community tool written in C-language, simulating 
application load and application behavior of thousands and tens of thousand 
HTTP/HTTPS and FTP/FTPS clients, each with its own source IP-address.

%prep
%setup -q
%patch0 -p0 -b .link
%patch1 -p0

%build

%make OPT_FLAGS="%{optflags}" INCDIR="-I. -I%{_includedir}/curl -I%{_includedir}/openssl" LDFLAGS="%{ldflags}"

%install
install -d %{buildroot}%{_sbindir}
install -d %{buildroot}%{_mandir}/man1
install -d %{buildroot}%{_mandir}/man5

install -m0755 %{name} %{buildroot}%{_sbindir}/
install -m0644 doc/curl-loader.1 %{buildroot}%{_mandir}/man1/
install -m0644 doc/curl-loader-config.5 %{buildroot}%{_mandir}/man5/

%files
%doc doc/COPYING doc/PROBLEM-REPORTING doc/QUICK-START doc/README doc/THANKS doc/TODO conf-examples
%{_sbindir}/*
%{_mandir}/man1/*
%{_mandir}/man5/*

