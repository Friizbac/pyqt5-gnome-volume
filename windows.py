import sys
import dbus
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import os
user = str(os.getuid())
srv_addr = 'unix:path=/run/user/' + user + '/pulse/dbus-socket'
bus=dbus.connection.Connection(srv_addr)





class Example(QWidget):
    
    def __init__(self):
        super().__init__()
        
        self.initUI()
        
    def initUI(self):               
        self.label = QLabel("sink" + user, self)
        sld = QSlider(Qt.Horizontal, self)
        sld.setFocusPolicy(Qt.NoFocus)
        sld.setRange(0, 65537)
        sld.setGeometry(30, 40, 100, 30)
        sld.valueChanged[int].connect(self.changeValue)

        
        
        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Volume changer')    
        self.show()

    def changeValue(self, value):

        location = 'sink0'
        location = ('/org/pulseaudio/core1/' + location)
        sink = ( dbus.Interface( bus.get_object(object_path=location),
        dbus_interface='org.freedesktop.DBus.Properties' ))

        if value == 0:
            sink.Set( 'org.PulseAudio.Core1.Device', 'Volume', [dbus.UInt32('0')], dbus_interface='org.freedesktop.DBus.Properties' )
        elif value > 0:
            sink.Set( 'org.PulseAudio.Core1.Device', 'Volume', [dbus.UInt32(value)], dbus_interface='org.freedesktop.DBus.Properties' )
            

        else:
            sink.Set( 'org.PulseAudio.Core1.Device', 'Volume', [dbus.UInt32('0')], dbus_interface='org.freedesktop.DBus.Properties' )


if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
