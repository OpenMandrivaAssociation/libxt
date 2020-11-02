# libXt is used by libXmu, which in turn is used by wine
%ifarch %{x86_64}
%bcond_without compat32
%else
%bcond_with compat32
%endif

%define major 6
%define libname %mklibname xt %{major}
%define devname %mklibname xt -d

%if %{with compat32}
%define lib32name libxt%{major}
%define dev32name libxt-devel
%endif

%global optflags %{optflags} -O3

Summary:	X Toolkit Intrinsics library
Name:		libxt
Version:	1.2.0
Release:	8
License:	MIT
Group:		Development/X11
Url:		http://xorg.freedesktop.org
Source0:	http://xorg.freedesktop.org/releases/individual/lib/libXt-%{version}.tar.bz2
BuildRequires:	pkgconfig(sm)
BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(xproto)
BuildRequires:	pkgconfig(xorg-macros)
%if %{with compat32}
BuildRequires:	devel(libSM)
BuildRequires:	devel(libX11)
BuildRequires:	devel(libICE)
BuildRequires:	devel(libxcb)
BuildRequires:	devel(libXau)
BuildRequires:	devel(libXdmpc)
%endif

%description
X Toolkit Intrinsics library used to build older generation toolkits such
as Motif & Xaw.

%package -n %{libname}
Summary:	X Toolkit Intrinsics library
Group:		Development/X11

%description -n %{libname}
X Toolkit Intrinsics library used to build older generation toolkits such
as Motif & Xaw.

%package -n %{devname}
Summary:	Development files for %{name}
Group:		Development/X11
Requires:	%{libname} = %{version}-%{release}

%description -n %{devname}
Development files for %{name}.

%if %{with compat32}
%package -n %{lib32name}
Summary:	X Toolkit Intrinsics library (32-bit)
Group:		Development/X11

%description -n %{lib32name}
X Toolkit Intrinsics library used to build older generation toolkits such
as Motif & Xaw.

%package -n %{dev32name}
Summary:	Development files for %{name} (32-bit)
Group:		Development/X11
Requires:	%{devname} = %{version}-%{release}
Requires:	%{lib32name} = %{version}-%{release}

%description -n %{dev32name}
Development files for %{name}.
%endif

%prep
%autosetup -n libXt-%{version} -p1
export CONFIGURE_TOP="`pwd`"
%if %{with compat32}
mkdir build32
cd build32
%configure32
cd ..
%endif
mkdir build
cd build
%configure

%build
%if %{with compat32}
%make_build -C build32
%endif
%make_build -C build

%install
%if %{with compat32}
%make_install -C build32
%endif
%make_install -C build

%files -n %{libname}
%{_libdir}/libXt.so.%{major}*

%files -n %{devname}
%{_libdir}/libXt.so
%{_libdir}/pkgconfig/xt.pc
%{_includedir}/X11/Core.h
%{_includedir}/X11/VarargsI.h
%{_includedir}/X11/RectObj.h
%{_includedir}/X11/TranslateI.h
%{_includedir}/X11/Vendor.h
%{_includedir}/X11/CallbackI.h
%{_includedir}/X11/ResConfigP.h
%{_includedir}/X11/IntrinsicI.h
%{_includedir}/X11/IntrinsicP.h
%{_includedir}/X11/ConstrainP.h
%{_includedir}/X11/Constraint.h
%{_includedir}/X11/InitialI.h
%{_includedir}/X11/EventI.h
%{_includedir}/X11/ObjectP.h
%{_includedir}/X11/Xtos.h
%{_includedir}/X11/CreateI.h
%{_includedir}/X11/Intrinsic.h
%{_includedir}/X11/CoreP.h
%{_includedir}/X11/Object.h
%{_includedir}/X11/CompositeP.h
%{_includedir}/X11/HookObjI.h
%{_includedir}/X11/RectObjP.h
%{_includedir}/X11/ConvertI.h
%{_includedir}/X11/Shell.h
%{_includedir}/X11/ShellI.h
%{_includedir}/X11/ShellP.h
%{_includedir}/X11/StringDefs.h
%{_includedir}/X11/VendorP.h
%{_includedir}/X11/SelectionI.h
%{_includedir}/X11/PassivGraI.h
%{_includedir}/X11/Composite.h
%{_includedir}/X11/ThreadsI.h
%{_includedir}/X11/ResourceI.h
%{_mandir}/man3/Xt*.3*
%{_mandir}/man3/Menu*
%{_docdir}/libXt/*

%if %{with compat32}
%files -n %{lib32name}
%{_prefix}/lib/libXt.so.%{major}*

%files -n %{dev32name}
%{_prefix}/lib/libXt.so
%{_prefix}/lib/pkgconfig/xt.pc
%endif
