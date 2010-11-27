%define upstream_name	 Net-Patricia
%define upstream_version 1.19

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:	Patricia Trie perl module for fast IP address lookups
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://search.cpan.org/CPAN/modules/by-module/Net/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:  perl(Socket6)
BuildRequires:	perl-devel
BuildRequires:	perl-Net-CIDR-Lite

BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}

%description
This module uses a Patricia Trie data structure to quickly perform IP address
prefix matching for applications such as IP subnet, network or routing table
lookups. The data structure is based on a radix tree using a radix of two, so
sometimes you see patricia implementations called "radix" as well. The term
"Trie" is derived from the word "retrieval" but is pronounced like "try".
Patricia stands for "Practical Algorithm to Retrieve Information Coded as
Alphanumeric", and was first suggested for routing table lookups by Van
Jacobsen. Patricia Trie performance characteristics are well-known as it has
been employed for routing table lookups within the BSD kernel since the 4.3
Reno release.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL
%make

%check
%make test

%install
rm -Rf %{buildroot}
%make DESTDIR=%{buildroot} pure_vendor_install \
INSTALLSITELIB=%perl_vendorlib \
INSTALLSITEMAN1DIR=%{_mandir}/man1 \
INSTALLSITEMAN3DIR=%{_mandir}/man3
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'

%clean
rm -Rf %{buildroot}

%files
%defattr(-,root,root)
%{perl_vendorarch}/Net*
%{perl_vendorarch}/auto/Net*
%{_mandir}/man?/*
