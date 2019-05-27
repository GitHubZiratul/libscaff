lib_LTLIBRARIES = libscaffold.la
libscaffold_la_SOURCES = scaffold.c
libscaffold_la_LDFLAGS = \
    -version-info @SCAFFOLDLIB_MINOR@:@SCAFFOLDLIB_RELEASE@:@SCAFFOLDLIB_MAJOR@
include_HEADERS = scaffold.h

pkgconfigdir = @pkgconfigdir@
pkgconfig_DATA = libscaffold.pc
