%define modname websocket
%define distname websocket-client
%define oname websocket_client

Name:		python-websocket-client
Version:	1.9.0
Release:	1
Summary:	WebSocket client for python
Group:		Development/Python
License:	LGPL-2.0
URL:		https://pypi.python.org/pypi/websocket-client
Source0:	https://pypi.python.org/packages/source/w/websocket-client/%{oname}-%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildSystem:	python
BuildArch:     noarch
BuildRequires:	pkgconfig
BuildRequires:	pkgconfig(python)
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(wheel)
BuildRequires:	python%{pyver}dist(six)

Requires:	python%{pyver}dist(six)

# This package used to be the only user of this obsolete backport
Obsoletes:	python-backports.ssl_match_hostname

%description
python-websocket-client module is WebSocket client for python. This
provides the low level APIs for WebSocket. All APIs are the synchronous
functions.

python-websocket-client supports only hybi-13.

%prep
%autosetup -n %{oname}-%{version} -p1
# Remove upstream's egg-info
rm -vrf %{oname}.egg-info

%build
%py_build

%install
%py_install

%install -a
# unbundle cacert
rm -fv %{buildroot}/%{python_sitelib}/%{modname}/cacert.pem
# And link in the mozilla ca
ln -s /etc/pki/tls/cert.pem \
    %{buildroot}/%{python_sitelib}/%{modname}/cacert.pem

# remove tests that got installed into the buildroot
rm -rf %{buildroot}/%{python_sitelib}/tests/

# Remove executable bit from installed files.
find %{buildroot}/%{python_sitelib} -type f -exec chmod -x {} \;


%files
%doc README.md
%license LICENSE
%{python_sitelib}/%{modname}/
%{python_sitelib}/%{oname}*%{version}*
%{_bindir}/wsdump
