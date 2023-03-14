Name:           oz-layout
Version:        1
Release:        1%{?dist}
Summary:        My personal keyboard layout
BuildArch:      noarch
License:        LicenseRef-Fedora-Public-Domain
Source0:        oz
Source1:        evdev.xml

%description
My personal keyboard layout, probably of little interest to anybody else


%install
%{__install} -D -m644 %{SOURCE0} %{buildroot}/etc/xkb/symbols/us
%{__install} -D -m644 %{SOURCE1} %{buildroot}/etc/xkb/rules/evdev.xml

%files
/etc/xkb/rules/evdev.xml
/etc/xkb/symbols/us


%changelog
* Tue Mar 14 2023 Robin Sonefors <robin@sonefors.net>
- Initial version
