# Logitech gaming keyboard extended keys redirector

This is a daemon that redirects G-keys of Logitech gaming keyboards
(tested with my G11) to regular F-key combinations, using `xdotool`.

* `G1` to `G12` -> `super` + `F1` to `F12`
* `G13` to `G18` -> `super` + `alt` + `F1` to `F6`
* `M1`, `M2`, `M3`, `MR` -> `super` + `alt` + `F7` to `F10`

## Installation

As superuser:

* Install the python module with `pip install .` in a clone of this repository
* Make the systemd unit service available with ```systemctl link `pwd`/gkeys.service```
* To manually start the service, use `systemctl start gkeys`
* To enable starting the service on boot, issue `systemctl enable gkeys`
