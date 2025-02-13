#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-bowler
Version  : 0.9.0
Release  : 24
URL      : https://files.pythonhosted.org/packages/f4/02/4728875b1fc4382ea71e771c3475a2af6ccaf140663b36c8456ebba4ac5a/bowler-0.9.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/f4/02/4728875b1fc4382ea71e771c3475a2af6ccaf140663b36c8456ebba4ac5a/bowler-0.9.0.tar.gz
Summary  : Safe code refactoring for modern Python projects
Group    : Development/Tools
License  : MIT
Requires: pypi-bowler-bin = %{version}-%{release}
Requires: pypi-bowler-license = %{version}-%{release}
Requires: pypi-bowler-python = %{version}-%{release}
Requires: pypi-bowler-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(attrs)
BuildRequires : pypi(click)
BuildRequires : pypi(fissix)
BuildRequires : pypi(moreorless)
BuildRequires : pypi(setuptools)
BuildRequires : pypi(volatile)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
**Safe code refactoring for modern Python projects.**

%package bin
Summary: bin components for the pypi-bowler package.
Group: Binaries
Requires: pypi-bowler-license = %{version}-%{release}

%description bin
bin components for the pypi-bowler package.


%package license
Summary: license components for the pypi-bowler package.
Group: Default

%description license
license components for the pypi-bowler package.


%package python
Summary: python components for the pypi-bowler package.
Group: Default
Requires: pypi-bowler-python3 = %{version}-%{release}

%description python
python components for the pypi-bowler package.


%package python3
Summary: python3 components for the pypi-bowler package.
Group: Default
Requires: python3-core
Provides: pypi(bowler)
Requires: pypi(attrs)
Requires: pypi(click)
Requires: pypi(fissix)
Requires: pypi(moreorless)
Requires: pypi(volatile)

%description python3
python3 components for the pypi-bowler package.


%prep
%setup -q -n bowler-0.9.0
cd %{_builddir}/bowler-0.9.0
pushd ..
cp -a bowler-0.9.0 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1672260569
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export FCFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export FFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export CXXFLAGS="$CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 setup.py build

popd
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
PYTHONPATH=%{buildroot}$(python -c "import sys; print(sys.path[-1])") python setup.py test || :

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-bowler
cp %{_builddir}/bowler-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/pypi-bowler/1506731a652bba9abdf804ba3c95651ec5a68bdc || :
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -tt setup.py build install --root=%{buildroot}-v3
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/bowler

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-bowler/1506731a652bba9abdf804ba3c95651ec5a68bdc

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
