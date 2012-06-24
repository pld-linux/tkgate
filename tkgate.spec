Summary:	Digital circuits simulator
Summary(pl):	Symulator obwod�w cyfrowych
Name:		tkgate
Version:	1.8.5
Release:	0.1
Group:		X11/Applications/Science
License:	GPL
Source0:	ftp://gadoid.ices.cmu.edu/pub/tkgate/%{name}-%{version}.tgz
# Source0-md5:	0c14089c4f10f45796d8ef8e14ee6452
Patch0:		%{name}-config.patch
URL:		http://www.tkgate.org/
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
TkGate jest sterowanym zda�eniami symulatorem obwod�w cyfrowych z
graficznym interfejsem opartym o Tcl/Tk. TkGate pozwala korzysta� z
du�ego zestawu podstawowych element�w jak r�wnie� z definiowanych
przez u�ytkownika modu��w. Dystrybucja zawiera zestaw tutoriali i
przyk�adowych obwod�w, kt�re mog� zosta� za�adowane poprzez menu
"Help". W�r�d nich znajduje si� prosty procesor zaprogramowany do gry
w "Animals".

%prep
%setup -q
%patch0 -p1

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
%{_libdir}/%{name}-%{version}/examples
%dir %{_libdir}/%{name}-%{version}/libexec
%attr(755,root,root) %{_libdir}/%{name}-%{version}/libexec/*
%{_libdir}/%{name}-%{version}/gdf
%{_libdir}/%{name}-%{version}/scripts
%{_libdir}/%{name}-%{version}/messages*
%{_libdir}/%{name}-%{version}/sitename.txt
%{_mandir}/*/*
