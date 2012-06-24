%include	/usr/lib/rpm/macros.perl
%define	pdir	Digest
%define	pnam	LineByLine
Summary:	Digest::LineByLine Perl module
Summary(cs):	Modul Digest::LineByLine pro Perl
Summary(da):	Perlmodul Digest::LineByLine
Summary(de):	Digest::LineByLine Perl Modul
Summary(es):	M�dulo de Perl Digest::LineByLine
Summary(fr):	Module Perl Digest::LineByLine
Summary(it):	Modulo di Perl Digest::LineByLine
Summary(ja):	Digest::LineByLine Perl �⥸�塼��
Summary(ko):	Digest::LineByLine �� ����
Summary(no):	Perlmodul Digest::LineByLine
Summary(pl):	Modu� Perla Digest::LineByLine
Summary(pt):	M�dulo de Perl Digest::LineByLine
Summary(pt_BR):	M�dulo Perl Digest::LineByLine
Summary(ru):	������ ��� Perl Digest::LineByLine
Summary(sv):	Digest::LineByLine Perlmodul
Summary(uk):	������ ��� Perl Digest::LineByLine
Summary(zh_CN):	Digest::LineByLine Perl ģ��
Name:		perl-Digest-LineByLine
Version:	1.0
Release:	2
License:	Artistic or GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pnam}-%{version}.tar.gz
BuildRequires:	perl >= 5.6
BuildRequires:	perl-Digest-SHA1
BuildRequires:	rpm-perlprov >= 4.0.2-104
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module allows you to add line-by-line authentication codes to a
plain-text file. The file can still be manipulated using all the
text-file tools you know and love, including a text editor. However,
if someone else tampers with the file, you can detect the tampering.

%description -l pl
Ten podu� pozwala na dodawanie kod�w uwierzytelniaj�cych do kolejnych
linii pliku tekstowego. Ten plik mo�e by� nadal modyfikowany przy
u�yciu wszystkich narz�dzi tekstowych, w��cznie z edytorem. Mimo to,
je�li kto� inny b�dzie grzeba� w pliku, mo�na to wykry�.

%prep
%setup -q -c

%build
touch Makefile.PL
%{__perl} -MExtUtils::MakeMaker -e 'WriteMakefile(NAME=>"Digest::LineByLine")'
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{perl_sitelib}/Digest/*.pm
%{_mandir}/man3/*
