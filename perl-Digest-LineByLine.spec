%include	/usr/lib/rpm/macros.perl
%define		pdir	Digest
%define		pnam	LineByLine
Summary:	Digest::LineByLine Perl module
Summary(cs):	Modul Digest::LineByLine pro Perl
Summary(da):	Perlmodul Digest::LineByLine
Summary(de):	Digest::LineByLine Perl Modul
Summary(es):	Módulo de Perl Digest::LineByLine
Summary(fr):	Module Perl Digest::LineByLine
Summary(it):	Modulo di Perl Digest::LineByLine
Summary(ja):	Digest::LineByLine Perl ¥â¥¸¥å¡¼¥ë
Summary(ko):	Digest::LineByLine ÆÞ ¸ðÁÙ
Summary(no):	Perlmodul Digest::LineByLine
Summary(pl):	Modu³ Perla Digest::LineByLine
Summary(pt):	Módulo de Perl Digest::LineByLine
Summary(pt_BR):	Módulo Perl Digest::LineByLine
Summary(ru):	íÏÄÕÌØ ÄÌÑ Perl Digest::LineByLine
Summary(sv):	Digest::LineByLine Perlmodul
Summary(uk):	íÏÄÕÌØ ÄÌÑ Perl Digest::LineByLine
Summary(zh_CN):	Digest::LineByLine Perl Ä£¿é
Name:		perl-Digest-LineByLine
Version:	1.0
Release:	1
License:	Artistic or GPL
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pnam}-%{version}.tar.gz
BuildRequires:	perl >= 5.6
BuildRequires:	perl-Digest-SHA1
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module allows you to add line-by-line authentication codes to a
plain-text file. The file can still be manipulated using all the
text-file tools you know and love, including a text editor. However,
if someone else tampers with the file, you can detect the tampering.

%description -l pl
Ten podu³ pozwala na dodawanie kodów uwierzytelniaj±cych do kolejnych
linii pliku tekstowego. Ten plik mo¿e byæ nadal modyfikowany przy
u¿yciu wszystkich narzêdzi tekstowych, w³±cznie z edytorem. Mimo to,
je¶li kto¶ inny bêdzie grzeba³ w pliku, mo¿na to wykryæ.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{perl_sitelib}/Digest,%{_mandir}/man3}

install LineByLine.pm $RPM_BUILD_ROOT%{perl_sitelib}/Digest

pod2man --section=3pm LineByLine.pm > $RPM_BUILD_ROOT%{_mandir}/man3/Digest::LineByLine.3pm

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{perl_sitelib}/Digest/*
%{_mandir}/man3/*
