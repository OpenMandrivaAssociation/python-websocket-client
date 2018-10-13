%define modname websocket
%define distname websocket-client
%define eggname websocket_client

Name:          python-websocket-client
Version:       0.53.0
Release:       1
Summary:       WebSocket client for python

Group:         Development/Python
License:       LGPLv2
URL:           http://pypi.python.org/pypi/websocket-client
Source0:       http://pypi.python.org/packages/source/w/%{distname}/%{eggname}-%{version}.tar.gz

BuildArch:     noarch
#Python2
BuildRequires: pkgconfig(python2)
BuildRequires: pythonegg(setuptools)
BuildRequires: pythonegg(six)
#Python3
BuildRequires: pkgconfig(python)
BuildRequires: python3egg(setuptools)
BuildRequires: python3egg(six)

Requires:      python2-six

%description
python-websocket-client module is WebSocket client for python. This
provides the low level APIs for WebSocket. All APIs are the synchronous
functions.

python-websocket-client supports only hybi-13.

%package -n python3-websocket-client
Summary:       WebSocket client for python
Group:         Development/Python
Requires:      python-six

%description -n python3-websocket-client
python-websocket-client module is WebSocket client for python. This
provides the low level APIs for WebSocket. All APIs are the synchronous
functions.

python-websocket-client supports only hybi-13.

%prep
%setup -q -n %{eggname}-%{version}

# Remove bundled egg-info in case it exists
rm -rf %{distname}.egg-info

cp -a . %{pydir}

%build
%py2_build

pushd %{pydir}
%py_build
popd

%install
pushd %{pydir}
%py_install
mv %{buildroot}/%{_bindir}/wsdump.py \
    %{buildroot}/%{_bindir}/python3-wsdump

# unbundle cacert
rm %{buildroot}/%{python3_sitelib}/%{modname}/cacert.pem
# And link in the mozilla ca
ln -s /etc/pki/tls/cert.pem \
    %{buildroot}/%{python3_sitelib}/%{modname}/cacert.pem

# remove tests that got installed into the buildroot
rm -rf %{buildroot}/%{python3_sitelib}/tests/

# Remove executable bit from installed files.
find %{buildroot}/%{python3_sitelib} -type f -exec chmod -x {} \;
popd

%py2_install
mv %{buildroot}/%{_bindir}/wsdump.py \
    %{buildroot}/%{_bindir}/wsdump

# unbundle cacert
rm %{buildroot}/%{python_sitelib}/%{modname}/cacert.pem
# And link in the mozilla ca
ln -s /etc/pki/tls/cert.pem \
    %{buildroot}/%{python_sitelib}/%{modname}/cacert.pem

# remove tests that got installed into the buildroot
rm -rf %{buildroot}/%{python_sitelib}/tests/

# Remove executable bit from installed files.
find %{buildroot}/%{python_sitelib} -type f -exec chmod -x {} \;


%check
pushd %{pydir}
%{__python} setup.py test
popd

%{__python2} setup.py test


%files
%doc README.rst 
%license LICENSE
%{python2_sitelib}/%{modname}/
%{python2_sitelib}/%{eggname}*%{version}*
%{_bindir}/wsdump

%files -n python3-websocket-client
%doc README.rst 
%license LICENSE
%{python3_sitelib}/%{modname}/
%{python3_sitelib}/%{eggname}*%{version}*
%{_bindir}/python3-wsdump
