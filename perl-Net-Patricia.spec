%define module	Net-Patricia
%define moddir	Net/Patricia

Name:		perl-%{module}
Version:	1.15
Release:	%mkrel 1
License:	GPL or Artistic
Group:		Development/Perl
Summary:	Patricia Trie perl module for fast IP address lookups
URL:		http://search.cpan.org/dist/%{module}
Source:		http://search.cpan.org/CPAN/modules/by-module/%{module}/%{module}-%{version}.tar.gz
BuildRequires:	perl-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}

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
%setup -q -n %{module}-%{version}

%build
%{__perl} Makefile.PL
%make

%install
rm -Rf %{buildroot}
%make DESTDIR=%{buildroot} pure_vendor_install \
INSTALLSITELIB=%perl_vendorlib \
INSTALLSITEMAN1DIR=%{_mandir}/man1 \
INSTALLSITEMAN3DIR=%{_mandir}/man3
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'

%check
%make test

%clean
rm -Rf %{buildroot}

%files
%defattr(-,root,root)
%{perl_vendorarch}/%{moddir}*
%{perl_vendorarch}/auto/%{moddir}*
%{_mandir}/man?/*



