Name:       test
Version:    $VERSION
Release:    $RELEASE
Summary:    Test rpm

License:    Test
BuildRoot:  %{_tmppath}/%{name}-%{version}-root
BuildArch:  noarch

%description
test rpm

#
# Post-install
#
%post

mkdir -p /opt/bvi/test2

#
# File list
#
%files
