%define modname websocket
%define distname websocket-client
%define eggname websocket_client

Name:          python-websocket-client
Version:    1.2.1
Release:    2
Summary:       WebSocket client for python

Group:         Development/Python
License:       LGPLv2
URL:           http://pypi.python.org/pypi/websocket-client
Source0:	https://pypi.python.org/packages/source/w/websocket-client/%{distname}-%{version}.tar.gz
BuildArch:     noarch

BuildRequires: pkgconfig(python)
BuildRequires: python3dist(setuptools)
BuildRequires: python3dist(six)

Requires:      python-six
Requires:      python-backports.ssl_match_hostname

%description
python-websocket-client module is WebSocket client for python. This
provides the low level APIs for WebSocket. All APIs are the synchronous
functions.

python-websocket-client supports only hybi-13.

%prep
%setup -q -n %{distname}-%{version}

# Remove bundled egg-info in case it exists
rm -rf %{distname}.egg-info

%py_build

%install
%py_install

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
%{python_sitelib}/%{eggname}*%{version}*
#{_bindir}/wsdump*
