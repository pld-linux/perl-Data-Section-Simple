#
# Conditional build:
%bcond_without	tests	# unit tests
#
%define		pdir	Data
%define		pnam	Section-Simple
Summary:	Data::Section::Simple - Read data from __DATA__ section of file
Summary(pl.UTF-8):	Data::Section::Simple - odczyt danych z sekcji __DATA__ pliku
Name:		perl-Data-Section-Simple
Version:	0.07
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	https://www.cpan.org/modules/by-module/Data/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	5a079d3d7712fa3c8256494cf026a153
URL:		https://metacpan.org/dist/Data-Section-Simple
BuildRequires:	perl-ExtUtils-MakeMaker >= 6.30
BuildRequires:	perl-devel >= 1:5.8.1
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	rpmbuild(macros) >= 1.745
%if %{with tests}
BuildRequires:	perl-Test-Requires
BuildRequires:	perl-Test-Simple >= 0.88
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Data::Section::Simple is a simple module to extract data from
__DATA__ section of the file.

%description -l pl.UTF-8
Data::Section::Simple to prosty moduł wydobywający dane z sekcji
__DATA__ pliku.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%dir %{perl_vendorlib}/Data/Section
%{perl_vendorlib}/Data/Section/Simple.pm
%{_mandir}/man3/Data::Section::Simple.3pm*
