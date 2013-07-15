%define upstream_name	 Net-Patricia
%define upstream_version 1.20

Name:       perl-%{upstream_name}
Version:    %perl_convert_version 1.20
Release:	1

Summary:	Patricia Trie perl module for fast IP address lookups
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://search.cpan.org/CPAN/modules/by-module/Net/Net-Patricia-1.20.tar.gz

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


%changelog
* Wed Jan 25 2012 Per Øyvind Karlsen <peroyvind@mandriva.org> 1.190.0-2
+ Revision: 768358
- svn commit -m mass rebuild of perl extension against perl 5.14.2

* Sat Nov 27 2010 Guillaume Rousse <guillomovitch@mandriva.org> 1.190.0-1mdv2011.0
+ Revision: 601938
- update to new version 1.19

* Mon Oct 25 2010 Buchan Milne <bgmilne@mandriva.org> 1.180.0-1mdv2011.0
+ Revision: 589297
- BR perl-Net-CIDR-Lite, required for testing
- update to new version 1.18

  + Jérôme Quelin <jquelin@mandriva.org>
    - rebuild for perl 5.12

* Thu Feb 25 2010 Jérôme Quelin <jquelin@mandriva.org> 1.160.0-1mdv2010.1
+ Revision: 511040
- adding missing buildrequires:
- update to 1.16

* Tue Aug 04 2009 Jérôme Quelin <jquelin@mandriva.org> 1.150.0-2mdv2010.0
+ Revision: 408970
- fix url
- rebuild using %%perl_convert_version

* Tue May 05 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.15-1mdv2010.0
+ Revision: 372317
- new version

* Thu Jul 31 2008 Thierry Vignaud <tv@mandriva.org> 1.014-7mdv2009.0
+ Revision: 258058
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 1.014-6mdv2009.0
+ Revision: 246160
- rebuild

* Tue Jan 15 2008 Thierry Vignaud <tv@mandriva.org> 1.014-4mdv2008.1
+ Revision: 152225
- rebuild

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Sat Dec 22 2007 Guillaume Rousse <guillomovitch@mandriva.org> 1.014-3mdv2008.1
+ Revision: 137055
- rebuild

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Sat Oct 28 2006 Nicolas Lécureuil <neoclust@mandriva.org> 1.014-2mdv2007.0
+ Revision: 73478
- import perl-Net-Patricia-1.014-2mdv2007.1

* Fri Jul 07 2006 Buchan Milne <bgmilne@obsidian.co.za> 1.014-1mdv2007.0
- first Mandriva package


