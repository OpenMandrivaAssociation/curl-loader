Summary:	A HTTP(S)/FTP(S) application load stress testing tool
Name:		curl-loader
Version:	0.50
Release:	%mkrel 3
License:	GPLv2
Group:		System/Servers
URL:		http://curl-loader.sourceforge.net/
Source0:	http://sunet.dl.sourceforge.net/project/curl-loader/curl-loader/%{name}-%{version}/%{name}-%{version}.tar.gz
Patch0:		curl-loader-0.50-linkage_fixes.diff
Patch1:		curl-loader-0.50-hack.diff
BuildRequires:	curl-devel >= 7.19.6
BuildRequires:	libevent-devel >= 1.4.11
BuildRequires:	openssl-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
curl-loader is an open-source community tool written in C-language, simulating 
application load and application behavior of thousands and tens of thousand 
HTTP/HTTPS and FTP/FTPS clients, each with its own source IP-address.

%prep

%setup -q
%patch0 -p0
%patch1 -p0

%build

%make OPT_FLAGS="%{optflags}" INCDIR="-I. -I%{_includedir}/curl -I%{_includedir}/openssl" LDFLAGS="%{ldflags}"

%install
rm -rf %{buildroot}

install -d %{buildroot}%{_sbindir}
install -d %{buildroot}%{_mandir}/man1
install -d %{buildroot}%{_mandir}/man5

install -m0755 %{name} %{buildroot}%{_sbindir}/
install -m0644 doc/curl-loader.1 %{buildroot}%{_mandir}/man1/
install -m0644 doc/curl-loader-config.5 %{buildroot}%{_mandir}/man5/

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc doc/COPYING doc/HOWTOS doc/PROBLEM-REPORTING doc/QUICK-START doc/README doc/THANKS doc/TODO conf-examples
%{_sbindir}/*
%{_mandir}/man1/*
%{_mandir}/man5/*

