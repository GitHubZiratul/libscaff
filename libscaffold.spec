%define _unpackaged_files_terminate_build 1

%def_disable static

Name: libscaffold
Version: 0.0.1
Release: alt1

Summary: Sample library for the scaffold game
License: LGPLv2+
Group: System/Libraries
Url: git://git.altlinux.org/people/krash/public/libscaffold.git

Source: %name-%version.tar

BuildRequires: gcc

%description
This specfile is provided as sample specfile for packages with libraries.
It contains most of usual tags and constructions used in such specfiles.

%package devel
Summary: Headers for %name
Group: Development/C
Requires: %name = %version-%release

%description devel
Headers for building software that uses %name

%if_enabled static
%package devel-static
Summary: Static libraries for %name
Group: Development/C
Requires: %name-devel = %version-%release

%description devel-static
Static libs for building statically linked software that uses %name
%endif

%prep
%setup

%build
%autoreconf
%configure %{subst_enable static}

%install
%makeinstall_std

%files
# %doc AUTHORS README NEWS
%_libdir/*.so.*

%files devel
%_includedir/*.h
%_libdir/*.so
%_pkgconfigdir/*.pc

%if_enabled static
%files devel-static
%_libdir/lib%name.a
%endif

%changelog
* Tue May 28 2019 Leonid Krashenko <krash@altlinux.org> 0.0.1-alt1
- Initial build


