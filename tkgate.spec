Summary:	Digital circuits simulator
Summary(pl):	Symulator obwod�w cyfrowych
Name:		tkgate
Version:	1.3b
Release:	1
Group:		X11/Applications
Group(pl):	X11/Aplikacje
License:	GPL
Source0:	ftp://gadoid.ices.cmu.edu/pub/tkgate/%{name}-%{version}.tgz
Patch0:		tkgate-config.patch
BuildRequires:	tk-devel
BuildRequires:	tcl-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
TkGate is an event driven digital circuit simulator with a tcl/tk-based
graphical editor.  TkGate supports a wide range of primitive circuit elements
as well as user-defined modules for hierarchical design. The distribution
comes with a number of tutorial and example circuits which can be loaded
through the "Help" menu. The example circuits include a simple CPU, programmed
to run the Animals game.

%description -l pl
TkGate jest sterowanym zda�eniami symulatorem obwod�w cyforwych z graficznym
interfejsem opartym o tcl/tk. TkGate pozwala korzysta� z du�ego zestawu
podstawowych element�w jak t�wnie� z definiowanych przez u�ytkownika modu��w.
Dystrybucja zawiera zestaw tutoriali i przyk�adowych obwod�w, kt�re mog�
zosta� za�adowane poprzez menu "Help". W�r�d nich znajduje si� prosty procesor
zaprogramowany do gry w "Animals".

%prep
%setup  -q
%patch0 -p1

%build
LDFLAGS="-s" ; export LDFLAGS
export CXXDEBUGFLAGS="$RPM_OPT_FLAGS"

# This is NOT a GNU Configure.
./configure 

make OPT_FLAGS="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT

make install install.man \
	DESTDIR="$RPM_BUILD_ROOT"

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man*/* \
	README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_prefix}/bin/*
%dir %{_libdir}/%{name}-%{version}
%{_libdir}/%{name}-%{version}/bitmaps
%{_libdir}/%{name}-%{version}/doc
%{_libdir}/%{name}-%{version}/examples
%dir %{_libdir}/%{name}-%{version}/libexec
%attr(755,root,root) %{_libdir}/%{name}-%{version}/libexec/*
%{_libdir}/%{name}-%{version}/scripts
%{_libdir}/%{name}-%{version}/README
%{_libdir}/%{name}-%{version}/gate.lib
%{_libdir}/%{name}-%{version}/messages*
%{_libdir}/%{name}-%{version}/sitename.txt
%{_mandir}/*/*
