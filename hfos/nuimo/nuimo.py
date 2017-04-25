from hfos.logger import hfoslog, debug, warn, critical, error
from hfos.component import ConfigurableComponent

try:
    import nuimo
except ImportError:
    nuimo = None
    hfoslog("No python-linux-nuimo library found, install "
            "requirements.txt", lvl=warn, emitter="NUIMO")


class Nuimo(ConfigurableComponent):
    configprops = {
        'controller': {'type': 'string', 'title': 'Bluetooth Controller',
                'description': 'Bluetooth controller to connect to the Nuimo',
                'default': 'hci0'},
        'address': {'type': 'string', 'title': 'MAC Address',
                 'description': 'Bluetooth address of the Nuimo'},
    }

    def __init__(self, *args, **kwargs):
        super(Nuimo, self).__init__("LDAP", *args, **kwargs)
        if nuimo is None:
            self.log("NOT started, no python-linux-nuimo found", lvl=warn)
            return

        self.log("Started")

        self.nuimo= None
        self._nuimo_connect()

    def _nuimo_connect(self):
        self.log("Connecting to Nuimo Controller", self.config.address,
                 "via", self.config.controller)
        try:
            self.nuimo = nuimo.Controller(mac_address=self.config.address,
                                    manager=self)
        except Exception as e:
            self.log("No connection to the Nuimo device! (", e, type(e), ")",
                     lvl=error)

    def received_gesture_event(self, event):
        pass

    def started_connecting(self):
        pass

    def connect_succeeded(self):
        pass

    def connect_failed(self, error):
        pass

    def started_disconnecting(self):
        pass

    def disconnect_succeeded(self):
        pass
