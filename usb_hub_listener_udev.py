#!/usr/bin/env python

import glib
import os

from pyudev import Context, Monitor
from pyudev.glib import MonitorObserver

usb_hub_hdmi = 'usb3/3-1/3-1.1/3-1.1:1.0'


def device_event(observer, device):
    update_monitor_settings(device)


def update_monitor_settings(device):
    if device.action.decode("string-escape") == "add":
        if usb_hub_hdmi in device.device_path.decode("string-escape"):
            print 'set monitor on'
            os.system('xrandr --output DP-1 --auto --output eDP-1 --mode 1920x1080 --rate 59.93 --left-of DP-1')
    elif device.action.decode("string-escape") == "remove":
        if usb_hub_hdmi in device.device_path.decode("string-escape"):
            os.system('xrandr --output DP-1 --off --output eDP-1 --mode 1920x1080 --rate 59.93 --same-as DP-1')
            print 'set monitor off'


context = Context()
monitor = Monitor.from_netlink(context)

monitor.filter_by(subsystem='usb')
observer = MonitorObserver(monitor)

observer.connect('device-event', device_event)
monitor.start()

glib.MainLoop().run()
