Name:           pi-bluetooth
Version:        0.1.19
Release:        6%{?dist}
Summary:        Bluetooth support for raspberry pies
BuildArch:      noarch
License:        BSD-3-Clause
URL:            https://github.com/RPi-Distro/pi-bluetooth
Source0:        https://github.com/RPi-Distro/pi-bluetooth/archive/87248a382d1a81b80a62730975135d87fffd7ef1.zip
Source1:        99-com-minimal.rules
BuildRequires:  systemd-rpm-macros
Requires:       bluez-deprecated
BuildArch:      noarch
Requires(post): systemd-units
Requires(preun): systemd-units
Requires(postun): systemd-units

%description
This packages the custom udev, systemd and helper shell scripts that
Raspberry Pi OS uses to get the onboard bluetooth to work.

%build

%prep
%autosetup -n pi-bluetooth-87248a382d1a81b80a62730975135d87fffd7ef1

%install
install -p -D -m 644 lib/udev/rules.d/90-pi-bluetooth.rules %{_sourcedir}/99-com-minimal.rules -t %{buildroot}%{_udevrulesdir}
install -p -D -m 755 usr/bin/bthelper usr/bin/btuart -t %{buildroot}%{_bindir} 
install -p -D -m 644 debian/pi-bluetooth.bthelper@.service %{buildroot}%{_unitdir}/bthelper@.service
install -p -D -m 644 debian/pi-bluetooth.hciuart.service %{buildroot}%{_unitdir}/hciuart.service
install -p -D -m 644 debian/copyright -t %{buildroot}%{_docdir}

%post
%systemd_post hciuart.service
# Should be udev trigger, but that's not how upstream does it
systemctl enable hciuart.service

%preun
%systemd_preun hciuart.service
%postun
%systemd_postun_with_restart hciuart.service

%files
%license %{_docdir}/copyright
%{_bindir}/bthelper
%{_bindir}/btuart
%{_udevrulesdir}/90-pi-bluetooth.rules
%{_udevrulesdir}/99-com-minimal.rules
%{_unitdir}/bthelper@.service
%{_unitdir}/hciuart.service


%changelog
* Tue Mar 14 2023 Robin Sonefors <robin@sonefors.net> - 0.1.19-5
- Set noarch. There's no real reason you couldn't use it on armv7

* Mon Mar 13 2023 Robin Sonefors <robin@sonefors.net> - 0.1.19-5
- Explicitly enable hciuart.service - it doesn't work otherwise

* Mon Mar 13 2023 Robin Sonefors <robin@sonefors.net> - 0.1.19-4
- Fix name of bthelper service

* Mon Mar 13 2023 Robin Sonefors <robin@sonefors.net> - 0.1.19-3
- Install hciuart.service properly - it required manually starting before

* Sat Mar 04 2023 Robin Sonefors <robin@sonefors.net> - 0.1.19-2
- Add bluez-deprecated dependency - the shell scripts depend on it

* Sat Mar 04 2023 Robin Sonefors <robin@sonefors.net> - 0.1.19-1
- First packaged version
