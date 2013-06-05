%define major 6
%define libxt %mklibname xt %{major}
%define develname %mklibname xt -d

Name:		libxt
Summary:	X Toolkit Intrinsics library
Version:	1.1.4
Release:	1
Group:		Development/X11
License:	MIT
URL:		http://xorg.freedesktop.org
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
# wrong place to put these
# relocated to x11-font-alias
#Requires: x11-font-daewoo-misc
#Requires: x11-font-isas-misc
#Requires: x11-font-jis-misc
Conflicts:	libxorg-x11 < 7.0
Provides:	%{name} = %{version}

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
Conflicts:	libxorg-x11-devel < 7.0

%description -n %{develname}
Development files for %{name}.

%prep
%setup -qn libXt-%{version}
%apply_patches

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


%changelog
* Thu Mar 29 2012 Bernhard Rosenkraenzer <bero@bero.eu> 1.1.3-1
+ Revision: 788256
- Update to 1.1.3

* Sat Mar 10 2012 Alexander Khrukin <akhrukin@mandriva.org> 1.1.2-1
+ Revision: 783975
- version update 1.1.2

* Thu Mar 08 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.1.1-5
+ Revision: 783349
- Remove pre scriptlet to correct rpm upgrade moving from /usr/X11R6.

* Tue Dec 27 2011 Matthew Dawkins <mattydaw@mandriva.org> 1.1.1-4
+ Revision: 745633
- rebuild
- disabled static build
- removed .la files
- cleaned up spec

* Wed Dec 14 2011 Matthew Dawkins <mattydaw@mandriva.org> 1.1.1-3
+ Revision: 741163
- rebuild
- added back missing devel provides

* Tue Dec 13 2011 Matthew Dawkins <mattydaw@mandriva.org> 1.1.1-2
+ Revision: 740609
- rebuild
- dropped wrong placed reqs
- cleaned spec

* Mon Apr 11 2011 Matthew Dawkins <mattydaw@mandriva.org> 1.1.1-1
+ Revision: 652679
- new version 1.1.1

* Tue Nov 30 2010 Paulo Ricardo Zanoni <pzanoni@mandriva.com> 1.0.9-3mdv2011.0
+ Revision: 603752
- Improve package description.
  Based on the 1.0.9 release announcement email and cgit description.

* Mon Nov 29 2010 Paulo Ricardo Zanoni <pzanoni@mandriva.com> 1.0.9-2mdv2011.0
+ Revision: 603126
- Require x11-font-daewoo-misc, x11-font-isas-misc and x11-font-jis-misc
  If the fonts required by libxt are not present, xlib can spend a lot of time
  looking for them, which makes simple apps like "xmessage" and "xcalc" take
  almost 10 seconds to start on systems with a lot of fonts. This case is usually
  triggered by Xt apps that call XtSetLanguageProc on UTF-8 systems. Since UTF-8
  is the default, require the fonts.
  CCBUG: 60967

* Fri Oct 29 2010 Thierry Vignaud <tv@mandriva.org> 1.0.9-1mdv2011.0
+ Revision: 589851
- new release

* Wed Mar 17 2010 Paulo Ricardo Zanoni <pzanoni@mandriva.com> 1.0.8-1mdv2010.1
+ Revision: 523757
- New version: 1.0.8

* Tue Nov 24 2009 Paulo Ricardo Zanoni <pzanoni@mandriva.com> 1.0.7-3mdv2010.1
+ Revision: 469706
- Fix Requires for static-devel

* Tue Nov 17 2009 Paulo Ricardo Zanoni <pzanoni@mandriva.com> 1.0.7-2mdv2010.1
+ Revision: 466919
- Adapt to correct library naming policy.

* Tue Nov 10 2009 Paulo Ricardo Zanoni <pzanoni@mandriva.com> 1.0.7-1mdv2010.1
+ Revision: 464044
- New version: 1.0.7

* Sat Jul 04 2009 Tomasz Pawel Gajc <tpg@mandriva.org> 1.0.6-1mdv2010.0
+ Revision: 392296
- update to new version 1.0.6
- drop patch 1, fixed upstream

* Sat Jun 28 2008 Oden Eriksson <oeriksson@mandriva.com> 1.0.5-4mdv2009.0
+ Revision: 229747
- rebuild

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

  + Paulo Andrade <pcpa@mandriva.com.br>
    - Revert build requires.

* Mon Jan 14 2008 Paulo Andrade <pcpa@mandriva.com.br> 1.0.5-2mdv2008.1
+ Revision: 151688
- Update BuildRequires and rebuild.

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Mon Dec 17 2007 Thierry Vignaud <tv@mandriva.org> 1.0.5-1mdv2008.1
+ Revision: 129296
- kill re-definition of %%buildroot on Pixel's request
- fix man pages extension


* Mon Feb 05 2007 Gustavo Pichorim Boiko <boiko@mandriva.com> 1.0.5-1mdv2007.0
+ Revision: 116293
- new upstream version: 1.0.5

* Tue Nov 21 2006 Thierry Vignaud <tvignaud@mandriva.com> 1.0.4-1mdv2007.1
+ Revision: 85951
- new release

* Wed Aug 30 2006 Antonio Hobmeir Neto <neto@mandriva.com> 1.0.2-3mdv2007.0
+ Revision: 58635
- Linking cplusplus for solve problem in compiling ddd aplication. (#24097)

  + Gustavo Pichorim Boiko <boiko@mandriva.com>
    - rebuild to fix cooker uploading
    - X11R7.1
    - increment release
    - fixed more dependencies
    - Adding X.org 7.0 to the repository

  + Andreas Hasenack <andreas@mandriva.com>
    - renamed mdv to packages because mdv is too generic and it's hosting only packages anyway

