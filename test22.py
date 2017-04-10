import os
import sys
import dbus
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import os
user = str(os.getuid())
srv_addr = 'unix:path=/run/user/' + user + '/pulse/dbus-socket'
bus=dbus.connection.Connection(srv_addr)
class Device(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    core = bus.get_object(object_path="/org/pulseaudio/core1")
    location = (core.Get("org.PulseAudio.Core1", "Sinks", dbus_interface="org.freedesktop.DBus.Properties"))
    
    def initUI(self):
        self.lb1 = QLabel(self.location[0], self)
        combo = QComboBox(self)
        for k in self.location:
            combo.addItem(k)
        combo.move(50, 80)
        self.lb1.move(50, 150)

        combo.activated[str].connect(self.onActivated)

        sld = QSlider(Qt.Horizontal, self)
        sld.setFocusPolicy(Qt.NoFocus)
        sld.setRange(0, 65537)
        sld.setGeometry(30, 40, 230, 30)
        sld.valueChanged[int].connect(self.changeValue)

        
        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Volume changer')    
        self.show()

    def onActivated(self, text):

        "\n"
        location2 = self.lb1.setText(text)
        location2
        self.lb1.adjustSize()
    def changeValue(self, value):
        self.sink = ( dbus.Interface( bus.get_object(object_path=str(self.lb1.text())), dbus_interface='org.freedesktop.DBus.Properties' ))
        self.sink.Set( 'org.PulseAudio.Core1.Device', 'Volume', [dbus.UInt32(value)], dbus_interface='org.freedesktop.DBus.Properties' )


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Device()
    sys.exit(app.exec_())

