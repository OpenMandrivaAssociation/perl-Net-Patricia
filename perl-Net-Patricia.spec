%define modname	Net-Patricia
%define moddir	Net/Patricia

Name:		perl-%{modname}
Version:	1.014
Release:	%mkrel 6
License:	GPL or Artistic
Group:		Development/Perl
Summary:	Patricia Trie perl module for fast IP address lookups
Source:		http://search.cpan.org/CPAN/modules/by-module/%{modname}/%{modname}-%{version}.tar.bz2
URL:		http://search.cpan.org/dist/%{modname}
BuildRequires:	perl-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-root

%description
Boulder - An API for hierarchical tag/value structures

%prep
%setup -q -n %{modname}-%{version}

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



