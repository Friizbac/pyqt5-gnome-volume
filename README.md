# PyQt5 gnome desktop volume changer
Change volume using graphical interface with pyqt5

This graphical interface is using DBus, so you'll have to if not load dbus-protocol module
 - in etc/pulse/default.pa add line (load-module module-dbus-protocol) or just enter command: pacmd load-module module-dbus-protocol
