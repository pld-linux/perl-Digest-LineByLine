%include	/usr/lib/rpm/macros.perl
%define		pdir	Digest
%define		pnam	LineByLine
Summary:	Digest::LineByLine - line-by-line message authentication for a plain text file
Summary(pl):	Digest::LineByLine - uwierzytelnianie plik�w tekstowych "wiersz po wierszu"
Name:		perl-Digest-LineByLine
Version:	1.0
Release:	3
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pnam}-%{version}.tar.gz
# Source0-md5:	b5177f677abadae08cf40cd3510813b4
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	perl-Digest-SHA1
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module allows you to add line-by-line authentication codes to a
plain-text file. The file can still be manipulated using all the
text-file tools you know and love, including a text editor. However,
if someone else tampers with the file, you can detect the tampering.

%description -l pl
Ten modu� pozwala na dodawanie kod�w uwierzytelniaj�cych do kolejnych
linii pliku tekstowego. Ten plik mo�e by� nadal modyfikowany przy
u�yciu wszystkich narz�dzi tekstowych, w��cznie z edytorem. Mimo to,
je�li kto� inny b�dzie grzeba� w pliku, mo�na to wykry�.

%prep
%setup -q -c

%build
touch Makefile.PL
%{__perl} -MExtUtils::MakeMaker -e 'WriteMakefile(NAME=>"Digest::LineByLine")' \
	INSTALLDIRS=vendor
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{perl_vendorlib}/Digest/*.pm
%{_mandir}/man3/*
