Name:       hw
Version:    1
Release:    1
Summary:    Most simple RPM package
License:    FIXME
Source0: https://github.com/Mormacill/coprtest/archive/refs/tags/1.1.tar.gz
BuildRequires: gcc

%description
This is my first RPM package, which does say Hello World.

%prep
%setup -q

%build
gcc hw.c

%install
mkdir -p %{buildroot}/usr/bin/
install -m 755 a.out %{buildroot}/usr/bin/a.out

%files
/usr/bin/a.out

%changelog
# let's skip this for now
