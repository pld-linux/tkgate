Summary:	Digital circuits simulator
Summary(pl):	Symulator obwodów cyfrowych
Name:		tkgate
Version:	1.6i
Release:	2
Group:		X11/Applications/Science
License:	GPL
Source0:	ftp://gadoid.ices.cmu.edu/pub/tkgate/%{name}-%{version}.tgz
# Source0-md5:	75c38151392f7eba702a96f40ca64d3d
Patch0:		%{name}-config.patch
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

%description -l pl
TkGate jest sterowanym zda¿eniami symulatorem obwodów cyforwych z
graficznym interfejsem opartym o Tcl/Tk. TkGate pozwala korzystaæ z
du¿ego zestawu podstawowych elementów jak tównie¿ z definiowanych
przez u¿ytkownika modu³ów. Dystrybucja zawiera zestaw tutoriali i
przyk³adowych obwodów, które mog± zostaæ za³adowane poprzez menu
"Help". W¶ród nich znajduje siê prosty procesor zaprogramowany do gry
w "Animals".

%prep
%setup  -q
%patch0 -p1

%build
LDFLAGS="%{rpmldflags}" ; export LDFLAGS
CXXDEBUGFLAGS="%{rpmcflags}" ; export CXXDEBUGFLAGS

# This is NOT a GNU Configure.
./configure

%{__make} OPT_FLAGS="%{rpmcflags}"

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
%{_libdir}/%{name}-%{version}/examples
%dir %{_libdir}/%{name}-%{version}/libexec
%attr(755,root,root) %{_libdir}/%{name}-%{version}/libexec/*
%{_libdir}/%{name}-%{version}/gdf
%{_libdir}/%{name}-%{version}/scripts
%{_libdir}/%{name}-%{version}/messages*
%{_libdir}/%{name}-%{version}/sitename.txt
%{_mandir}/*/*
