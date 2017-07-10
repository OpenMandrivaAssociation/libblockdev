%define major 2

%define libbdutils	%mklibname bd_utils %{major}
%define libbdutilsdev	%mklibname -d bd_utils

%define libblock	%mklibname blockdev %{major}
%define libblockdev	%mklibname -d blockdev

%define libbdbtrfs	%mklibname bd_btrfs %{major}
%define libbdbtrfsdev	%mklibname -d bd_btrfs

%define libbdcrypto	%mklibname bd_crypto %{major}
%define libbdcryptodev	%mklibname -d bd_crypto

%define libbddm		%mklibname bd_dm %{major}
%define libbddmdev	%mklibname -d bd_dm

%define libbdloop	%mklibname bd_loop %{major}
%define libbdloopdev	%mklibname -d bd_loop

%define libbdlvm	%mklibname bd_lvm %{major}
%define libbdlvmdev	%mklibname -d bd_lvm
# /libbd_lvm-dbus.so
%define libbdlvmdbus	%mklibname bd_lvm-dbus %{major}
%define libbdlvmdbusdev %mklibname -d bd_lvm-dbus
# libbd_mdraid.so
%define libbdmdraid	%mklibname bd_mdraid %{major}
%define libbdmdraiddev	%mklibname -d bd_mdraid
# libbd_mpath.so.*
%define libdbmpath	%mklibname bd_mpath %{major}
%define libbdmpathdev	%mklibname -d bd_mpath
# /libbd_swap.so.
%define libdbswap	%mklibname bd_swap %{major}
%define libbdswapdev	%mklibname -d bd_swap
# /libbd_part.so.
%define libdbpart	%mklibname bd_part %{major}
%define libbdpartdev	%mklibname -d bd_part
# /libbd_part_err.so.
%define libdbparterr	%mklibname bd_part_err %{major}
%define libbdparterrdev	%mklibname -d bd_part_err
# /libbd_kbd.so.
%define libdbkbd	%mklibname bd_kbd %{major}
%define libbdkbddev	%mklibname -d bd_kbd
# libbd_fs.so.
%define libdbfs	%mklibname bd_fs %{major}
%define libbdfsdev	%mklibname -d bd_fs


%define Werror_cflags %nil
%define with_python3 1
%define with_gtk_doc 0
%define with_bcache 1
%define with_btrfs 1
%define with_crypto 1
%define with_dm 1
%define with_loop 1
%define with_lvm 1
%define with_lvm_dbus 1
%define with_mdraid 1
%define with_mpath 1
%define with_swap 1
%define with_kbd 1
%define with_part 1
%define with_part_err 1
%define with_fs 1
%define with_gi 1

%if %{with_btrfs} != 1
%define btrfs_copts --without-btrfs
%endif
%if %{with_crypto} != 1
%define crypto_copts --without-crypto
%endif
%if %{with_dm} != 1
%define dm_copts --without-dm
%endif
%if %{with_loop} != 1
%define loop_copts --without-loop
%endif
%if %{with_lvm} != 1
%define lvm_copts --without-lvm
%endif
%if %{with_lvm_dbus} != 1
%define lvm_dbus_copts --without-lvm_dbus
%endif
%if %{with_mdraid} != 1
%define mdraid_copts --without-mdraid
%endif
%if %{with_mpath} != 1
%define mpath_copts --without-mpath
%endif
%if %{with_swap} != 1
%define swap_copts --without-swap
%endif
%if %{with_kbd} != 1
%define kbd_copts --without-kbd
%endif
%if %{with_part} != 1
%define part_copts --without-part
%endif
%if %{with_fs} != 1
%define fs_copts --without-fs
%endif
%if %{with_gi} != 1
%define gi_copts --disable-introspection
%endif

%define configure_opts %{?distro_copts} %{?btrfs_copts} %{?crypto_copts} %{?dm_copts} %{?loop_copts} %{?lvm_copts} %{?lvm_dbus_copts} %{?mdraid_copts} %{?mpath_copts} %{?swap_copts} %{?kbd_copts} %{?part_copts} %{?fs_copts} %{?gi_copts}

Name:        libblockdev
Version:     2.10
Release:     1
Summary:     A library for low-level manipulation with block devices
License:     LGPLv2+
URL:         https://github.com/rhinstaller/libblockdev
Source0:     https://github.com/storaged-project/libblockdev/archive/%{version}-1.tar.gz
Source1:     libblockdev.rpmlintrc

BuildRequires: pkgconfig(glib-2.0)
%if %{with_gi}
BuildRequires: pkgconfig(gobject-introspection-1.0)
%endif
%if %{with_python3}
BuildRequires: python-devel
%endif
%if %{with_gtk_doc}
BuildRequires: gtk-doc
%endif

# Needed for the escrow tests in tests/crypto_test.py, but not used to build
# BuildRequires: volume_key
# BuildRequires: nss-tools

# Needed for python 2 vs. 3 compatibility in the tests, but not used to build
# BuildRequires: python-six
# BuildRequires: python3-six

%description
The libblockdev is a C library with GObject introspection support that can be
used for doing low-level operations with block devices like setting up LVM,
BTRFS, LUKS or MD RAID. The library uses plugins (LVM, BTRFS,...) and serves as
a thin wrapper around its plugins' functionality. All the plugins, however, can
be used as standalone libraries. One of the core principles of libblockdev is
that it is stateless from the storage configuration's perspective (e.g. it has
no information about VGs when creating an LV).

%package -n	%{libblock}
Summary:	Libblockdev libraries
Group:		System/Libraries

%description -n	%{libblock}
The libblockdev is a C library with GObject introspection support that can be
used for doing low-level operations with block devices like setting up LVM,
BTRFS, LUKS or MD RAID.

%package -n	%{libblockdev}
Summary:	Development files for libblockdev
Requires:	%{libblock} = %{version}-%{release}
Requires:	pkgconfig(glib-2.0)

%description -n %{libblockdev}
This package contains header files and pkg-config files needed for development
with the libblockdev library.

%if %{with_python3}
%package -n python-blockdev
Summary:     Python3 gobject-introspection bindings for libblockdev
Requires: %{name} = %{version}-%{release}

%description -n python-blockdev
This package contains enhancements to the gobject-introspection bindings for
libblockdev in Python3.
%endif

%package -n %{libbdutils}
Summary:     A library with utility functions for the libblockdev library

%description -n %{libbdutils}
The libblockdev-utils is a library providing utility functions used by the
libblockdev library and its plugins.

%package -n	%{libbdutilsdev}
Summary:	Development files for libblockdev-utils
Requires:	%{libbdutils} = %{version}-%{release}
Requires:	pkgconfig(glib-2.0)

%description -n %{libbdutilsdev}
This package contains header files and pkg-config files needed for development
with the libblockdev-utils library.

%if %{with_btrfs}
%package -n %{libbdbtrfs}
BuildRequires:	libbytesize-devel
Summary:	The BTRFS plugin for the libblockdev library
Requires:	%{libbdutils}
Requires:	btrfs-progs

%description -n %{libbdbtrfs}
The libblockdev library plugin (and in the same time a standalone library)
providing the BTRFS-related functionality.

%package -n	%{libbdbtrfsdev}
Summary:	Development files for the libblockdev-btrfs plugin/library
Requires:	%{libbdbtrfs} = %{version}-%{release}
Requires:	pkgconfig(glib-2.0)
Requires:	%{libbdutilsdev} = %{EVRD}

%description -n %{libbdbtrfsdev}
This package contains header files and pkg-config files needed for development
with the libblockdev-btrfs plugin/library.
%endif

%if %{with_crypto}
%package -n %{libbdcrypto}
BuildRequires: pkgconfig(libcryptsetup)
BuildRequires: volume_key-devel
BuildRequires: nss-devel
Summary:     The crypto plugin for the libblockdev library

%description -n %{libbdcrypto}
The libblockdev library plugin (and in the same time a standalone library)
providing the functionality related to encrypted devices (LUKS).

%package -n	%{libbdcryptodev}
Summary:	Development files for the libblockdev-crypto plugin/library
Requires:	%{libbdcrypto} = %{version}-%{release}
Requires:	pkgconfig(glib-2.0)

%description -n %{libbdcryptodev}
This package contains header files and pkg-config files needed for development
with the libblockdev-crypto plugin/library.
%endif

%if %{with_part_err}
%package -n	%{libdbparterr}
BuildRequires:	pkgconfig(libcryptsetup)
Summary:	A library with utility functions for the libblockdev library
Requires:	%{libbdutils} = %{version}-%{release}

%description -n %{libdbparterr}
The libblockdev library plugin (and in the same time a standalone library)
providing the functionality related to encrypted devices (LUKS).

%package -n	%{libbdparterrdev}
Summary:	Development files for the libblockdev-crypto plugin/library
Requires:	%{libdbparterr} = %{version}-%{release}
Requires:	%{libbdutilsdev} = %{version}-%{release}
Requires:	pkgconfig(glib-2.0)

%description -n %{libbdparterrdev}
This package contains header files and pkg-config files needed for development
with the libblockdev-crypto plugin/library.
%endif

%if %{with_dm}
%package -n	%{libbddm}
BuildRequires:	device-mapper-devel
BuildRequires:	%{_lib}dmraid-devel
BuildRequires:	pkgconfig(systemd)
Summary:	The Device Mapper plugin for the libblockdev library
Requires:	%{libbdutils}
Requires:	device-mapper
Requires:	dmraid

%description -n %{libbddm}
The libblockdev library plugin (and in the same time a standalone library)
providing the functionality related to Device Mapper.

%package -n %{libbddmdev}
Summary:     Development files for the libblockdev-dm plugin/library
Requires: %{libbddm} = %{version}-%{release}
Requires: pkgconfig(glib-2.0)
Requires: device-mapper-devel
Requires: pkgconfig(systemd)
Requires: dmraid-devel
Requires: %{libbdutilsdev}

%description -n %{libbddmdev}
This package contains header files and pkg-config files needed for development
with the libblockdev-dm plugin/library.
%endif

%if %{with_fs}
%package -n	%{libdbfs}
BuildRequires:	parted-devel
BuildRequires:	pkgconfig(blkid)
BuildRequires:	pkgconfig(mount)
Summary:	The FS plugin for the libblockdev library
Requires:	%{libbdutils}
Requires:	device-mapper-multipath

%description -n %{libdbfs}
The libblockdev library plugin (and in the same time a standalone library)
providing the functionality related to operations with file systems.

%package -n	%{libbdfsdev}
Summary:	Development files for the libblockdev-fs plugin/library
Requires:	%{libdbfs} = %{version}-%{release}
Requires:	%{libbdutilsdev}
Requires:	pkgconfig(glib-2.0)
Requires:	xfsprogs
Requires:	dosfstools

%description -n %{libbdfsdev}
This package contains header files and pkg-config files needed for development
with the libblockdev-fs plugin/library.
%endif

%if %{with_kbd}
%package -n %{libdbkbd}
BuildRequires:	kmod-devel
Summary:	The KBD plugin for the libblockdev library
Requires:	%{libbdutils}
%if %{with_bcache}
Requires:	bcache-tools
%endif

%description -n %{libdbkbd}
The libblockdev library plugin (and in the same time a standalone library)
providing the functionality related to kernel block devices (namely zRAM and
Bcache).

%package -n %{libbdkbddev}
Summary:	Development files for the libblockdev-kbd plugin/library
Requires:	%{libdbkbd} = %{version}-%{release}
Requires:	%{libbdutilsdev}
Requires:	pkgconfig(glib-2.0)

%description	-n %{libbdkbddev}
This package contains header files and pkg-config files needed for development
with the libblockdev-kbd plugin/library.
%endif

%if %{with_loop}
%package -n %{libbdloop}
Summary:     The loop plugin for the libblockdev library
Requires: %{libbdutils}

%description -n %{libbdloop}
The libblockdev library plugin (and in the same time a standalone library)
providing the functionality related to loop devices.

%package -n	%{libbdloopdev}
Summary:	Development files for the libblockdev-loop plugin/library
Requires:	%{libbdloop} = %{version}-%{release}
Requires:	%{libbdutilsdev}
Requires:	pkgconfig(glib-2.0)

%description -n %{libbdloopdev}
This package contains header files and pkg-config files needed for development
with the libblockdev-loop plugin/library.
%endif

%if %{with_lvm}
%package -n	%{libbdlvm}
BuildRequires:	device-mapper-devel
Summary:	The LVM plugin for the libblockdev library
Requires:	%{libbdutils}
Requires:	lvm2
# for thin_metadata_size
# fix me
#Requires: device-mapper-persistent-data

%description -n %{libbdlvm}
The libblockdev library plugin (and in the same time a standalone library)
providing the LVM-related functionality.

%package -n	%{libbdlvmdev}
Summary:	Development files for the libblockdev-lvm plugin/library
Requires:	%{libbdlvm} = %{version}-%{release}
Requires:	%{libbdutilsdev}
Requires:	pkgconfig(glib-2.0)

%description -n %{libbdlvmdev}
This package contains header files and pkg-config files needed for development
with the libblockdev-lvm plugin/library.
%endif

%if %{with_lvm_dbus}
%package -n	%{libbdlvmdbus}
BuildRequires:	device-mapper-devel
Summary:	The LVM plugin for the libblockdev library
Requires:	%{libbdutils}
Requires:	lvm2-dbusd >= 2.02.156
# for thin_metadata_size
Requires: device-mapper-persistent-data

%description -n %{libbdlvmdbus}
The libblockdev library plugin (and in the same time a standalone library)
providing the LVM-related functionality utilizing the LVM DBus API.

%package -n	%{libbdlvmdbusdev}
Summary:	Development files for the libblockdev-lvm-dbus plugin/library
Requires:	%{libbdlvmdbus} = %{version}-%{release}
Requires:	%{libbdutilsdev}
Requires:	pkgconfig(glib-2.0)

%description -n %{libbdlvmdbusdev}
This package contains header files and pkg-config files needed for development
with the libblockdev-lvm-dbus plugin/library.
%endif

%if %{with_mdraid}
%package -n %{libbdmdraid}
BuildRequires:	libbytesize-devel
Summary:	The MD RAID plugin for the libblockdev library
Requires:	%{libbdutils}
Requires:	mdadm

%description	-n %{libbdmdraid}
The libblockdev library plugin (and in the same time a standalone library)
providing the functionality related to MD RAID.

%package -n	%{libbdmdraiddev}
Summary:	Development files for the libblockdev-mdraid plugin/library
Requires:	%{libbdmdraid} = %{version}-%{release}
Requires:	%{libbdutilsdev}
Requires:	pkgconfig(glib-2.0)

%description -n %{libbdmdraiddev}
This package contains header files and pkg-config files needed for development
with the libblockdev-mdraid plugin/library.
%endif

%if %{with_mpath}
%package -n %{libdbmpath}
BuildRequires:	device-mapper-devel
Summary:	The multipath plugin for the libblockdev library
Requires:	%{libbdutils}
Requires:	device-mapper-multipath

%description -n %{libdbmpath}
The libblockdev library plugin (and in the same time a standalone library)
providing the functionality related to multipath devices.

%package -n	%{libbdmpathdev}
Summary:	Development files for the libblockdev-mpath plugin/library
Requires:	%{libdbmpath} = %{version}-%{release}
Requires:	%{libbdutilsdev}
Requires:	pkgconfig(glib-2.0)

%description -n %{libbdmpathdev}
This package contains header files and pkg-config files needed for development
with the libblockdev-mpath plugin/library.
%endif


%if %{with_part}
%package -n	%{libdbpart}
BuildRequires:	parted-devel
Summary:	The partitioning plugin for the libblockdev library
Requires:	%{libbdutils}
Requires:	device-mapper-multipath
Requires:	gdisk
Requires:	util-linux

%description -n	%{libdbpart}
The libblockdev library plugin (and in the same time a standalone library)
providing the functionality related to partitioning.

%package -n	%{libbdpartdev}
Summary:	Development files for the libblockdev-part plugin/library
Requires:	%{libdbpart} = %{version}-%{release}
Requires:	%{libbdutilsdev}
Requires:	pkgconfig(glib-2.0)

%description -n	%{libdbpart}
This package contains header files and pkg-config files needed for development
with the libblockdev-part plugin/library.
%endif

%if %{with_swap}
%package -n	%{libdbswap}
Summary:	The swap plugin for the libblockdev library
Requires:	%{libbdutils}
Requires:	util-linux

%description -n %{libdbswap}
The libblockdev library plugin (and in the same time a standalone library)
providing the functionality related to swap devices.

%package -n	%{libbdswapdev}
Summary:	Development files for the libblockdev-swap plugin/library
Requires:	%{libdbswap} = %{version}-%{release}
Requires:	%{libbdutilsdev}
Requires:	pkgconfig(glib-2.0)

%description -n %{libbdswapdev}
This package contains header files and pkg-config files needed for development
with the libblockdev-swap plugin/library.
%endif


%ifarch s390 s390x
%package s390
BuildRequires: s390utils-devel
Summary:    The s390 plugin for the libblockdev library
Requires: s390utils

%description s390
The libblockdev library plugin (and in the same time a standalone library)
providing the functionality related to s390 devices.

%package s390-devel
Summary:     Development files for the libblockdev-s390 plugin/library
Requires: %{name}-s390 = %{version}-%{release}
Requires: %{libbdutilsdev}
Requires: pkgconfig(glib-2.0)
Requires: s390utils-devel

%description s390-devel
This package contains header files and pkg-config files needed for development
with the libblockdev-s390 plugin/library.
%endif

%package	plugins-all
Summary:	Meta-package that pulls all the libblockdev plugins as dependencies
Requires:	%{name} = %{version}-%{release}

%if %{with_btrfs}
Requires:	%{libbdbtrfs} = %{version}-%{release}
%endif

%if %{with_crypto}
Requires:	%{libbdcrypto} = %{version}-%{release}
%endif

%if %{with_dm}
Requires:	%{libbddmdev} = %{version}-%{release}
%endif

%if %{with_fs}
Requires: %{name}-fs = %{version}-%{release}
%endif

%if %{with_kbd}
Requires:	%{libdbkbd} = %{version}-%{release}
%endif

%if %{with_loop}
Requires:	%{libbdloop} = %{version}-%{release}
%endif

%if %{with_lvm}
Requires:	%{libbdlvm}  = %{version}-%{release}
%endif

%if %{with_mdraid}
Requires:	%{libbdmdraid} = %{version}-%{release}
%endif

%if %{with_mpath}
Requires:	%{libdbmpath} = %{version}-%{release}
%endif

%if %{with_part_err}
Requires: 	%{libdbparterr} = %{version}-%{release}
%endif
%if %{with_part}
Requires:	%{libdbpart} = %{version}-%{release}
%endif

%if %{with_swap}
Requires:	%{libdbswap} = %{version}-%{release}
%endif

%ifarch s390 s390x
Requires: %{name}-s390 = %{version}-%{release}
%endif

%description plugins-all
A meta-package that pulls all the libblockdev plugins as dependencies.

%prep
%setup -q -n %{name}-%{version}-1
sed -i 's!-Werror!!g' configure.ac src/utils/Makefile.am src/plugins/Makefile.am

%build
export
%configure %{?configure_opts}
%{__make} %{?_smp_mflags}

%install
%{make_install}
find %{buildroot} -type f -name "*.la" | xargs %{__rm}

%files -n %{libblock}
%{_libdir}/libblockdev.so.%{major}*
%if %{with_gi}
%{_libdir}/girepository*/BlockDev*.typelib
%endif
%config %{_sysconfdir}/libblockdev/conf.d/00-default.cfg

%files -n %{libblockdev}
%{!?_licensedir:%global license %%doc}
%license LICENSE
%doc features.rst specs.rst
%{_libdir}/libblockdev.so
%dir %{_includedir}/blockdev
%{_includedir}/blockdev/blockdev.h
%{_includedir}/blockdev/plugins.h
%{_libdir}/pkgconfig/blockdev.pc
%if %{with_gtk_doc}
%{_datadir}/gtk-doc/html/libblockdev
%endif
%if %{with_gi}
%{_datadir}/gir*/BlockDev*.gir
%endif

%if %{with_python3}
%files -n python-blockdev
%{python_sitearch}/gi/overrides/BlockDev*
%endif

%files -n %{libbdutils}
%{_libdir}/libbd_utils.so.*

%if %{with_part_err}
%files -n %{libdbparterr}
%{_libdir}/libbd_part_err.so.*

%files -n %{libbdparterrdev}
%{_libdir}/libbd_part_err.so
%endif

%files -n %{libbdutilsdev}
%{_libdir}/libbd_utils.so
%dir %{_includedir}/blockdev
%{_includedir}/blockdev/utils.h
%{_includedir}/blockdev/sizes.h
%{_includedir}/blockdev/exec.h
%{_includedir}/blockdev/extra_arg.h
%{_includedir}/blockdev/dev_utils.h

%if %{with_btrfs}

%files -n %{libbdbtrfs}
%{_libdir}/libbd_btrfs.so.%{major}*

%files -n %{libbdbtrfsdev}
%{_libdir}/libbd_btrfs.so
%dir %{_includedir}/blockdev
%{_includedir}/blockdev/btrfs.h
%endif

%if %{with_crypto}
%files -n %{libbdcrypto}
%{_libdir}/libbd_crypto.so.%{major}*

%files -n %{libbdcryptodev}
%{_libdir}/libbd_crypto.so
%dir %{_includedir}/blockdev
%{_includedir}/blockdev/crypto.h
%endif

%if %{with_dm}
%files -n %{libbddm}
%{_libdir}/libbd_dm.so.*

%files -n %{libbddmdev}
%{_libdir}/libbd_dm.so
%dir %{_includedir}/blockdev
%{_includedir}/blockdev/dm.h
%endif

%if %{with_fs}
%files -n %{libdbfs}
%{_libdir}/libbd_fs.so.*

%files -n %{libbdfsdev}
%{_libdir}/libbd_fs.so
%dir %{_includedir}/blockdev
%{_includedir}/blockdev/fs.h
%endif

%if %{with_kbd}
%files -n %{libdbkbd}
%{_libdir}/libbd_kbd.so.*

%files -n %{libbdkbddev}
%{_libdir}/libbd_kbd.so
%dir %{_includedir}/blockdev
%{_includedir}/blockdev/kbd.h
%endif

%if %{with_loop}
%files -n %{libbdloop}
%{_libdir}/libbd_loop.so.%{major}*

%files -n %{libbdloopdev}
%{_libdir}/libbd_loop.so
%dir %{_includedir}/blockdev
%{_includedir}/blockdev/loop.h
%endif

%if %{with_lvm}
%files -n %{libbdlvm}
%{_libdir}/libbd_lvm.so.%{major}*

%files -n %{libbdlvmdev}
%{_libdir}/libbd_lvm.so
%dir %{_includedir}/blockdev
%{_includedir}/blockdev/lvm.h
%endif

%if %{with_lvm_dbus}
%files -n %{libbdlvmdbus}
%{_libdir}/libbd_lvm-dbus.so.*
%config %{_sysconfdir}/libblockdev/conf.d/10-lvm-dbus.cfg

%files -n %{libbdlvmdbusdev}
%{_libdir}/libbd_lvm-dbus.so
%endif

%if %{with_mdraid}
%files -n %{libbdmdraid}
%{_libdir}/libbd_mdraid.so.*

%files -n %{libbdmdraiddev}
%{_libdir}/libbd_mdraid.so
%dir %{_includedir}/blockdev
%{_includedir}/blockdev/mdraid.h
%endif

%if %{with_mpath}
%files -n %{libdbmpath}
%{_libdir}/libbd_mpath.so.*

%files -n %{libbdmpathdev}
%{_libdir}/libbd_mpath.so
%dir %{_includedir}/blockdev
%{_includedir}/blockdev/mpath.h
%endif

%if %{with_part}
%files -n %{libdbpart}
%{_libdir}/libbd_part.so.*

%files -n %{libbdpartdev}
%{_libdir}/libbd_part.so
%dir %{_includedir}/blockdev
%{_includedir}/blockdev/part.h
%endif

%if %{with_swap}
%files -n %{libdbswap}
%{_libdir}/libbd_swap.so.%{major}*

%files -n %{libbdswapdev}
%{_libdir}/libbd_swap.so
%dir %{_includedir}/blockdev
%{_includedir}/blockdev/swap.h
%endif

%ifarch s390 s390x
%files s390
%{_libdir}/libbd_s390.so.*

%files s390-devel
%{_libdir}/libbd_s390.so
%dir %{_includedir}/blockdev
%{_includedir}/blockdev/s390.h
%endif

%files plugins-all
