%define		modulename	pychm
Summary:	Python package to handle CHM files
Summary(pl.UTF-8):   Pakiet dla pythona do obsługi plików CHM
Name:		python-chm
Version:	0.8.4
Release:	1
License:	GPL v2+
Group:		Libraries/Python
Source0:	http://dl.sourceforge.net/gnochm/%{modulename}-%{version}.tar.gz
# Source0-md5:	ff7f0baf94290c44263a1618e7e6a116
URL:		http://gnochm.sourceforge.net/pychm.html
BuildRequires:	chmlib-devel
BuildRequires:	python
BuildRequires:	python-devel >= 1:2.5
%pyrequires_eq	python
Obsoletes:	pychm
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The chm package provides three modules, chm, chmlib and extra, which
provide access to the API implemented by the C library chmlib and some
additional classes and functions. They are used to access MS-ITSS
encoded files - Compressed HTML Help files (.chm).

%description -l pl.UTF-8
Pakiet chm udostępnia trzy moduły - chm, chmlib i extra, które
udostępniają dostęp do API biblioteki chmlib oraz kilka dodatkowych
klas i funkcji. Są one wykorzystywane do dostępu zakodowanych w
MS-ITSS plików - skompresowanych plików pomocy HTML(.chm).

%prep
%setup -q -n %{modulename}-%{version}

%build
python setup.py build

%install
rm -rf $RPM_BUILD_ROOT
python setup.py install \
	--root=$RPM_BUILD_ROOT \
	--optimize=2

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog NEWS README
%dir %{py_sitedir}/chm
%attr(755,root,root) %{py_sitedir}/chm/*.so
%{py_sitedir}/chm/*.py[oc]
%{py_sitedir}/pychm-*.egg-info
