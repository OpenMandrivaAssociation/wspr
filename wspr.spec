BuildRequires:	gcc-gfortran pkgconfig(python) python-imaging python-numpy 
BuildRequires:	pkgconfig(samplerate) f2c portaudio-devel fftw3-devel
BuildRequires:	python-numpy-devel

%define short_ver 3.00

Name:		wspr
Summary:	Weak Signal Propagation Reporter
Version:	3.00.r2436
Release:	1
Source0:	%{name}-%{version}.tar.bz2
Source1:        wspr.png
Group:		Communications
License:	GPL
URL:		http://developer.berlios.de/projects/wsjt/

Requires:	python
Requires:	python-imaging
Requires:	python-numpy
Requires:       hamlib

%description
The Weak Signal Propagation Reporter Network
is a group of amateur radio operators using
K1JT's MEPT_JT digital mode to probe radio
frequency propagation conditions using
very low power (QRP/QRPp) transmissions.

%package -n	python-%{name}
Summary:	WSPR library Python binding
Group:		Development/Python
Requires:	hamlib = %{version}-%{release}

%description -n python-%{name}
WSPR python bindings



%prep
%setup -q
#  -n %{name}-%{version}


%build 
./configure  --with-portaudio-include-dir=%{_includedir} \
	     --with-portaudio-lib-dir=%{_libdir} \
	     --libdir=%{_libdir}
make

%install

strip --strip-unneeded WsprMod/w.so

install -d %{buildroot}/%{py_sitedir}/WsprMod
install WsprMod/* %{buildroot}/%{py_sitedir}/WsprMod/
install -D wspr.py %{buildroot}/%{_datadir}/wspr/wspr.py
install -d %{buildroot}/%{_bindir}
install -d %{buildroot}/%{_datadir}/pixmaps/
install -d %{buildroot}/%{_datadir}/applications/

install ccf %{buildroot}/usr/bin
install fcal %{buildroot}/usr/bin
install fmeasure %{buildroot}/usr/bin
install fmt %{buildroot}/usr/bin/fmtstart
install fmtave %{buildroot}/usr/bin
install hftoa %{buildroot}/usr/bin
install wspr %{buildroot}/usr/bin
install wspr0 %{buildroot}/usr/bin
install wsprcode %{buildroot}/usr/bin
install wwv %{buildroot}/usr/bin

install hamlib_rig_numbers %{buildroot}/%{_datadir}/wspr
install 0230 %{buildroot}/%{_datadir}/wspr
install gocal %{buildroot}/%{_datadir}/wspr
install wsprrc %{buildroot}/%{_datadir}/wspr
install %{SOURCE1} %{buildroot}/%{_datadir}/pixmaps/wspr.png

sed -i -e '1i#!/usr/bin/python' %{buildroot}/%{py_sitedir}/WsprMod/*.*py
sed -i -e '1i#!/usr/bin/python' %{buildroot}/%{_datadir}/wspr/wspr.py


%files
%attr(0755 root root) %{_bindir}/*
%dir %attr(0755 root root) %{_datadir}/wspr
%attr(0644 root root) %{_datadir}/wspr/*
%attr(0644 root root) %{_datadir}/pixmaps/wspr.png
%doc LICENSE.TXT WSPR0_Instructions.TXT WSPR_Quick_Start.TXT


%files -n python-%{name}
%dir %{py_sitedir}/WsprMod
%{py_sitedir}/WsprMod/*


%changelog
* Thu May 10 2012 Alexander Khrukin <akhrukin@mandriva.org> 3.00.r2436-1
+ Revision: 798022
- imported package wspr

