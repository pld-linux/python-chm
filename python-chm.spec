%define		modulename	pychm
Summary:	Python package to handle CHM files
Summary(pl):	Pakiet dla pythona do obs³ugi plików CHM
Name:		python-chm
Version:	0.8.2
Release:	1
Source0:	http://dl.sourceforge.net/gnochm/%{modulename}-%{version}.tar.gz
# Source0-md5:	d1bc0d4d2d9f91aef5bf12ab0f92f0da
License:	GPL v2
Group:		Libraries/Python
URL:		http://gnochm.sourceforge.net/pychm.html
BuildRequires:	chmlib-devel
BuildRequires:	python
BuildRequires:	python-devel >= 2.2.1
%pyrequires_eq	python
Obsoletes:	pychm
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The chm package provides three modules, chm, chmlib and extra, which
provide access to the API implemented by the C library chmlib and some
additional classes and functions. They are used to access MS-ITSS
encoded files - Compressed HTML Help files (.chm).

%description
Pakiet chm udostêpnia trzy modu³y - chm, chmlib i extra, które
udostêpniaj± dostêp do API biblioteki chmlib oraz kilka dodatkowych
klas i funkcji. S± one wykorzystywane do dostêpu zakodowanych w
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

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README NEWS COPYING ChangeLog
%dir %{py_sitedir}/chm
%attr(755,root,root) %{py_sitedir}/chm/*.so
%{py_sitedir}/chm/*.py[oc]
