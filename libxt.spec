%define major 6
%define libxt %mklibname xt %{major}
%define develname %mklibname xt -d

Summary:	X Toolkit Intrinsics library
Name:		libxt
Version:	1.1.4
Release:	2
License:	MIT
Group:		Development/X11
Url:		http://xorg.freedesktop.org
Source0:	http://xorg.freedesktop.org/releases/individual/lib/libXt-%{version}.tar.bz2
BuildRequires:	pkgconfig(sm)
BuildRequires:	pkgconfig(x11)
BuildRequires:	x11-proto-devel >= 1.0.0
BuildRequires:	x11-util-macros >= 1.0.1

%description
X Toolkit Intrinsics library used to build older generation toolkits such
as Motif & Xaw.

%package -n %{libxt}
Summary:	X Toolkit Intrinsics library
Group:		Development/X11

%description -n %{libxt}
X Toolkit Intrinsics library used to build older generation toolkits such
as Motif & Xaw.

%package -n %{develname}
Summary:	Development files for %{name}
Group:		Development/X11
Requires:	%{libxt} = %{version}-%{release}
Provides:	libxt-devel = %{version}-%{release}
Obsoletes:	%{_lib}xt6-devel < 1.1.3
Obsoletes:	%{_lib}xt-static-devel < 1.1.3

%description -n %{develname}
Development files for %{name}.

%prep
%setup -qn libXt-%{version}

%build
%configure2_5x \
	--disable-static \
	--x-includes=%{_includedir} \
	--x-libraries=%{_libdir}

%make

%install
%makeinstall_std

%files -n %{libxt}
%{_libdir}/libXt.so.%{major}*

%files -n %{develname}
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

