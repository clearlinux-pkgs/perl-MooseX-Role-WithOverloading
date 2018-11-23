#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-MooseX-Role-WithOverloading
Version  : 0.17
Release  : 3
URL      : https://cpan.metacpan.org/authors/id/E/ET/ETHER/MooseX-Role-WithOverloading-0.17.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/E/ET/ETHER/MooseX-Role-WithOverloading-0.17.tar.gz
Summary  : '(DEPRECATED) Roles which support overloading'
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0
Requires: perl-MooseX-Role-WithOverloading-data = %{version}-%{release}
Requires: perl-MooseX-Role-WithOverloading-lib = %{version}-%{release}
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

%package data
Summary: data components for the perl-MooseX-Role-WithOverloading package.
Group: Data

%description data
data components for the perl-MooseX-Role-WithOverloading package.


%package dev
Summary: dev components for the perl-MooseX-Role-WithOverloading package.
Group: Development
Requires: perl-MooseX-Role-WithOverloading-lib = %{version}-%{release}
Requires: perl-MooseX-Role-WithOverloading-data = %{version}-%{release}
Provides: perl-MooseX-Role-WithOverloading-devel = %{version}-%{release}

%description dev
dev components for the perl-MooseX-Role-WithOverloading package.


%package lib
Summary: lib components for the perl-MooseX-Role-WithOverloading package.
Group: Libraries
Requires: perl-MooseX-Role-WithOverloading-data = %{version}-%{release}

%description lib
lib components for the perl-MooseX-Role-WithOverloading package.


%prep
%setup -q -n MooseX-Role-WithOverloading-0.17

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
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
cp LICENCE %{buildroot}/usr/share/package-licenses/perl-MooseX-Role-WithOverloading/LICENCE
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
/usr/lib/perl5/vendor_perl/5.28.0/x86_64-linux-thread-multi/MooseX/Role/WithOverloading.pm
/usr/lib/perl5/vendor_perl/5.28.0/x86_64-linux-thread-multi/MooseX/Role/WithOverloading/Meta/Role.pm
/usr/lib/perl5/vendor_perl/5.28.0/x86_64-linux-thread-multi/MooseX/Role/WithOverloading/Meta/Role/Application.pm
/usr/lib/perl5/vendor_perl/5.28.0/x86_64-linux-thread-multi/MooseX/Role/WithOverloading/Meta/Role/Application/Composite.pm
/usr/lib/perl5/vendor_perl/5.28.0/x86_64-linux-thread-multi/MooseX/Role/WithOverloading/Meta/Role/Application/Composite/ToClass.pm
/usr/lib/perl5/vendor_perl/5.28.0/x86_64-linux-thread-multi/MooseX/Role/WithOverloading/Meta/Role/Application/Composite/ToInstance.pm
/usr/lib/perl5/vendor_perl/5.28.0/x86_64-linux-thread-multi/MooseX/Role/WithOverloading/Meta/Role/Application/Composite/ToRole.pm
/usr/lib/perl5/vendor_perl/5.28.0/x86_64-linux-thread-multi/MooseX/Role/WithOverloading/Meta/Role/Application/FixOverloadedRefs.pm
/usr/lib/perl5/vendor_perl/5.28.0/x86_64-linux-thread-multi/MooseX/Role/WithOverloading/Meta/Role/Application/ToClass.pm
/usr/lib/perl5/vendor_perl/5.28.0/x86_64-linux-thread-multi/MooseX/Role/WithOverloading/Meta/Role/Application/ToInstance.pm
/usr/lib/perl5/vendor_perl/5.28.0/x86_64-linux-thread-multi/MooseX/Role/WithOverloading/Meta/Role/Application/ToRole.pm
/usr/lib/perl5/vendor_perl/5.28.0/x86_64-linux-thread-multi/MooseX/Role/WithOverloading/Meta/Role/Composite.pm

%files data
%defattr(-,root,root,-)
/usr/share/package-licenses/perl-MooseX-Role-WithOverloading/LICENCE

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/MooseX::Role::WithOverloading.3
/usr/share/man/man3/MooseX::Role::WithOverloading::Meta::Role::Application.3

%files lib
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.28.0/x86_64-linux-thread-multi/auto/MooseX/Role/WithOverloading/WithOverloading.so
