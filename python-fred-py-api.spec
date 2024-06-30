#
# spec file for package python-fred-py-api
#
# Copyright (c) 2024 SUSE LLC
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


Name:           python-fred-py-api
Version:        1.2.0
Release:        0
Summary:        A fully featured FRED Command Line Interface & Python API client library
License:        MIT
URL:            None
Source:         https://files.pythonhosted.org/packages/source/f/fred-py-api/fred_py_api-%{version}.tar.gz
BuildRequires:  python-rpm-macros
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools >= 61.0}
# SECTION test requirements
BuildRequires:  %{python_module click >= 7.0}
BuildRequires:  %{python_module requests >= 2.17.3}
BuildRequires:  python-setuptools
# /SECTION
BuildRequires:  fdupes
Requires:       python-click >= 7.0
Requires:       python-requests >= 2.17.3
Suggests:       python-black == 22.6.0
Suggests:       python-coverage == 6.4.2
Suggests:       python-black == 22.6.0
Suggests:       python-coverage == 6.4.2
Suggests:       python-tox == 3.25.1
Suggests:       python-sphinx == 7.2.6
BuildArch:      noarch
%python_subpackages

%description
A fully featured FRED Command Line Interface & Python API client library.

%prep
%autosetup -p1 -n fred-py-api-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/fred
%python_clone -a %{buildroot}%{_bindir}/categories
%python_clone -a %{buildroot}%{_bindir}/releases
%python_clone -a %{buildroot}%{_bindir}/series
%python_clone -a %{buildroot}%{_bindir}/sources
%python_clone -a %{buildroot}%{_bindir}/tags
%python_clone -a %{buildroot}%{_bindir}/fred
%python_clone -a %{buildroot}%{_bindir}/categories
%python_clone -a %{buildroot}%{_bindir}/releases
%python_clone -a %{buildroot}%{_bindir}/series
%python_clone -a %{buildroot}%{_bindir}/sources
%python_clone -a %{buildroot}%{_bindir}/tags
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%post
%python_install_alternative fred categories releases series sources tags fred categories releases series sources tags

%postun
%python_uninstall_alternative fred

%files %{python_files}
%python_alternative %{_bindir}/fred
%python_alternative %{_bindir}/categories
%python_alternative %{_bindir}/releases
%python_alternative %{_bindir}/series
%python_alternative %{_bindir}/sources
%python_alternative %{_bindir}/tags
%python_alternative %{_bindir}/fred
%python_alternative %{_bindir}/categories
%python_alternative %{_bindir}/releases
%python_alternative %{_bindir}/series
%python_alternative %{_bindir}/sources
%python_alternative %{_bindir}/tags
%{python_sitelib}/fred-py-api
%{python_sitelib}/fred-py-api-%{version}.dist-info

%changelog
