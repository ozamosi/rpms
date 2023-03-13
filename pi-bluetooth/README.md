# Fedora RPM package for pi-bluetooth

This makes the on-board bluetooth chip from a Raspberry Pi 4 work on Fedora.

Raspberry Pi OS contains a package called [`pi-bluetooth`](https://github.com/RPi-Distro/pi-bluetooth/)
that sets up the on-board bluetooth chip. This package contains a
couple of helper scripts that makes the chip be recognized.

This packages those scripts for Fedora. RPMs are kept in
[COPR](https://copr.fedorainfracloud.org/coprs/rsonefors/pi-bluetooth/)

## Installation

When you've installed Fedora on your Raspberry Pi, you'll find that running

```bash
bluetoothctl list
```

returns no bluetooth adapters.

With superuser permissions, do

```bash
dnf copr enable rsonefors/pi-bluetooth
dnf install pi-bluetooth
reboot
```

After rebooting, you should now see a device being returned by

```bash
bluetoothctl list
```
