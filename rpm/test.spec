Name:    test
Version: $VERSION
Release: $RELEASE
Summary: Test rpm

License: Test

%description
test rpm

%prep
exit 0

%clean

rm -rf %{buildroot}

%post

mkdir /opt/bvi/test 
