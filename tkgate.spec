Summary:	Digital circuits simulator
Summary(pl.UTF-8):	Symulator obwodów cyfrowych
Name:		tkgate
Version:	1.8.6
Release:	0.1
Group:		X11/Applications/Science
License:	GPL
Source0:	ftp://gadoid.ices.cmu.edu/pub/tkgate/%{name}-%{version}.tgz
# Source0-md5:	85f619c1c7de23185b80f1512e91e28a
Patch0:		%{name}-config.patch
Patch1:		%{name}-destdir.patch
URL:		http://www.tkgate.org/
BuildRequires:	flex
BuildRequires:	bison
BuildRequires:	tcl-devel
BuildRequires:	tk-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
TkGate is an event driven digital circuit simulator with a
Tcl/Tk-based graphical editor. TkGate supports a wide range of
primitive circuit elements as well as user-defined modules for
hierarchical design. The distribution comes with a number of tutorial
and example circuits which can be loaded through the "Help" menu. The
example circuits include a simple CPU, programmed to run the Animals
game.

%description -l pl.UTF-8
TkGate jest sterowanym zdarzeniami symulatorem obwodów cyfrowych z
graficznym interfejsem opartym o Tcl/Tk. TkGate pozwala korzystać z
dużego zestawu podstawowych elementów jak również z definiowanych
przez użytkownika modułów. Dystrybucja zawiera zestaw tutoriali i
przykładowych obwodów, które mogą zostać załadowane poprzez menu
"Help". Wśród nich znajduje się prosty procesor zaprogramowany do gry
w "Animals".

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
LDFLAGS="%{rpmldflags}" ; export LDFLAGS
CXXDEBUGFLAGS="%{rpmcflags}" ; export CXXDEBUGFLAGS

# This is NOT a GNU Configure.
./configure

%{__make} \
	OPT_FLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install install.man \
	DESTDIR="$RPM_BUILD_ROOT"

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%doc README
%dir %{_libdir}/%{name}-%{version}
%{_libdir}/%{name}-%{version}/bitmaps
%{_libdir}/%{name}-%{version}/doc
%{_libdir}/%{name}-%{version}/locale
%dir %{_libdir}/%{name}-%{version}/libexec
%attr(755,root,root) %{_libdir}/%{name}-%{version}/libexec/*
%{_libdir}/%{name}-%{version}/gdf
%{_libdir}/%{name}-%{version}/scripts
%{_libdir}/%{name}-%{version}/sitename.txt
%{_mandir}/*/*
