AC_INIT([libscaffold], [0.0.1], [krash@altlinux.org])
AM_INIT_AUTOMAKE([foreign])
LT_INIT

AC_PROG_CC

SCAFFOLDLIB_VERSION=0.0.1
SCAFFOLDLIB_MAJOR=0
SCAFFOLDLIB_MINOR=0
SCAFFOLDLIB_RELEASE=1

# Substitutions for .in files
AC_SUBST(SCAFFOLDLIB_VERSION)
AC_SUBST(SCAFFOLDLIB_MAJOR)
AC_SUBST(SCAFFOLDLIB_MINOR)
AC_SUBST(SCAFFOLDLIB_RELEASE)

# Additional arguments (and substitutions)
# Allow the pkg-config directory to be set
AC_ARG_WITH(pkgconfigdir,
        AC_HELP_STRING([--with-pkgconfigdir],
        [Use the specified pkgconfig dir (default is libdir/pkgconfig)]),
        [pkgconfigdir=${withval}],
        [pkgconfigdir='${libdir}/pkgconfig'])

AC_SUBST([pkgconfigdir])
AC_MSG_NOTICE([pkgconfig directory is ${pkgconfigdir}])

AC_CONFIG_FILES([Makefile libscaffold.pc:libscaffold.pc.in])
AC_OUTPUT
