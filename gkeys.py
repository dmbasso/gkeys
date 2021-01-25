#!/usr/bin/python3.9

"""Logitech gaming keyboard extended keys redirector

Usage:
    gkeys [-d DISPLAY] [-u UID] [-v]
    gkeys (-h | --help)

Options:
    -h --help   Show this screen
    -d DISPLAY  Set the X server address [default: :0]
    -u UID      Set the user id to drop from superuser [default: 1000]
    -v          Print key events
"""


import os
import sys
import evdev
import subprocess as sp
from docopt import docopt


def setup_device():
    dev = [
      dev for path in evdev.list_devices()
      if (dev := evdev.InputDevice(path)).name == "G15 Extra Keys"
    ][0]
    dev.grab()
    return dev


def event_loop(opts):
    print(f"Started with: {opts}")
    dev = setup_device()
    verbose = opts.get("-v")
    # on my G11 at least
    key_names = [f"G{i}" for i in range(19)] + [f"M{i}" for i in "123R"]
    uid = int(opts.get("-u", 1000))
    os.environ["DISPLAY"] = opts.get("-d")
    os.setuid(uid)
    for ev in dev.read_loop():
        if ev.type != evdev.ecodes.EV_KEY or not ev.value:
            continue
        gkey = ev.code - 166
        if 0 < gkey < 23:
            m, fkey = divmod(gkey, 13)
            mod = "super+alt" if m else "super"
            if m:
                fkey += 1
            if verbose:
                print(f"{key_names[gkey]} -> {mod}+F{fkey}")
            sp.run(["xdotool", "key", f"{mod}+F{fkey}"])
        elif verbose:
            print(f"Unexpected key code {ev.code} {gkey}")


def main():
    opts = docopt(__doc__, version="1.0.0")
    sp.run(["xdotool", "--version"], capture_output=True, check=True)
    if (uid := os.getuid()):
        sp.run(["sudo", *sys.argv, "-u", str(uid)])
    else:
        event_loop(opts)


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        pass
