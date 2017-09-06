# xrandr_automatic_monitor_configurator
Python script which automatically configures my monitor settings when attaching my desk USB hub.

## Customization
Add your own script or system calls to the existing code as desired.

## Installation
After cloning the resository create a systemd service to automatically start the listener at boot. See usb-listener.s
ervice as an example. Modify the file as required.

Copy the .service file to your systemd directory (usually `/lib/systemd/system`).

Ensure the new unit (.service file) has the correct permissions: `sudo chmod 664 usb-listener.service`.

Reload the systemctl daemon: `sudo systemctl daemon-reload`.

Enable the new service: `sudo systemctl enable usb-listener.service`.

Start the new service: `sudo systemctl start usb-listener.service`.

Verify the service is running without any issues: `sudo systemctl status usb-listener.service`.
