#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-MooseX-Role-WithOverloading
Version  : 0.17
Release  : 15
URL      : https://cpan.metacpan.org/authors/id/E/ET/ETHER/MooseX-Role-WithOverloading-0.17.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/E/ET/ETHER/MooseX-Role-WithOverloading-0.17.tar.gz
Summary  : '(DEPRECATED) Roles which support overloading'
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0
Requires: perl-MooseX-Role-WithOverloading-license = %{version}-%{release}
Requires: perl-MooseX-Role-WithOverloading-perl = %{version}-%{release}
BuildRequires : buildreq-cpan
BuildRequires : perl(Moose)
BuildRequires : perl(Moose::Exporter)
BuildRequires : perl(Moose::Role)
BuildRequires : perl(aliased)
BuildRequires : perl(namespace::autoclean)
BuildRequires : perl(namespace::clean)

%description
This archive contains the distribution MooseX-Role-WithOverloading,
version 0.17:

%package dev
Summary: dev components for the perl-MooseX-Role-WithOverloading package.
Group: Development
Provides: perl-MooseX-Role-WithOverloading-devel = %{version}-%{release}
Requires: perl-MooseX-Role-WithOverloading = %{version}-%{release}

%description dev
dev components for the perl-MooseX-Role-WithOverloading package.


%package license
Summary: license components for the perl-MooseX-Role-WithOverloading package.
Group: Default

%description license
license components for the perl-MooseX-Role-WithOverloading package.


%package perl
Summary: perl components for the perl-MooseX-Role-WithOverloading package.
Group: Default
Requires: perl-MooseX-Role-WithOverloading = %{version}-%{release}

%description perl
perl components for the perl-MooseX-Role-WithOverloading package.


%prep
%setup -q -n MooseX-Role-WithOverloading-0.17
cd %{_builddir}/MooseX-Role-WithOverloading-0.17

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-MooseX-Role-WithOverloading
cp %{_builddir}/MooseX-Role-WithOverloading-0.17/LICENCE %{buildroot}/usr/share/package-licenses/perl-MooseX-Role-WithOverloading/54a5fbc0aebdc943ab66b67ab7c5c6d4df048609
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/MooseX::Role::WithOverloading.3
/usr/share/man/man3/MooseX::Role::WithOverloading::Meta::Role::Application.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-MooseX-Role-WithOverloading/54a5fbc0aebdc943ab66b67ab7c5c6d4df048609

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.34.0/x86_64-linux-thread-multi/MooseX/Role/WithOverloading.pm
/usr/lib/perl5/vendor_perl/5.34.0/x86_64-linux-thread-multi/MooseX/Role/WithOverloading/Meta/Role.pm
/usr/lib/perl5/vendor_perl/5.34.0/x86_64-linux-thread-multi/MooseX/Role/WithOverloading/Meta/Role/Application.pm
/usr/lib/perl5/vendor_perl/5.34.0/x86_64-linux-thread-multi/MooseX/Role/WithOverloading/Meta/Role/Application/Composite.pm
/usr/lib/perl5/vendor_perl/5.34.0/x86_64-linux-thread-multi/MooseX/Role/WithOverloading/Meta/Role/Application/Composite/ToClass.pm
/usr/lib/perl5/vendor_perl/5.34.0/x86_64-linux-thread-multi/MooseX/Role/WithOverloading/Meta/Role/Application/Composite/ToInstance.pm
/usr/lib/perl5/vendor_perl/5.34.0/x86_64-linux-thread-multi/MooseX/Role/WithOverloading/Meta/Role/Application/Composite/ToRole.pm
/usr/lib/perl5/vendor_perl/5.34.0/x86_64-linux-thread-multi/MooseX/Role/WithOverloading/Meta/Role/Application/FixOverloadedRefs.pm
/usr/lib/perl5/vendor_perl/5.34.0/x86_64-linux-thread-multi/MooseX/Role/WithOverloading/Meta/Role/Application/ToClass.pm
/usr/lib/perl5/vendor_perl/5.34.0/x86_64-linux-thread-multi/MooseX/Role/WithOverloading/Meta/Role/Application/ToInstance.pm
/usr/lib/perl5/vendor_perl/5.34.0/x86_64-linux-thread-multi/MooseX/Role/WithOverloading/Meta/Role/Application/ToRole.pm
/usr/lib/perl5/vendor_perl/5.34.0/x86_64-linux-thread-multi/MooseX/Role/WithOverloading/Meta/Role/Composite.pm
/usr/lib/perl5/vendor_perl/5.34.0/x86_64-linux-thread-multi/auto/MooseX/Role/WithOverloading/WithOverloading.so
