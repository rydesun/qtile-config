from libqtile.widget import base
from libqtile.log_utils import logger
import iwlib

def get_status(interface_name):
    interface = iwlib.get_iwconfig(interface_name)
    essid = bytes(interface['ESSID']).decode()
    return essid


class Wlan(base.InLoopPollText):
    orientations = base.ORIENTATION_HORIZONTAL
    defaults = [
        ('interface', 'wlan0', 'The interface to monitor'),
        ('update_interval', 1, 'The update interval.'),
        (
            'disconnected_message',
            'Disconnected',
            'String to show when the wlan is diconnected.'
        ),
        (
            'icon',
            '',
            'Wifi icon'
        )
    ]

    def __init__(self, **config):
        base.InLoopPollText.__init__(self, **config)
        self.add_defaults(Wlan.defaults)

    def poll(self):
        try:
            essid = get_status(self.interface)
            disconnected = essid is None or essid == ""
            if disconnected:
                return self.disconnected_message

            return self.icon + ' ' + essid
        except EnvironmentError:
            logger.error(
                '%s: Probably your wlan device is switched off or '
                ' otherwise not present in your system.',
                self.__class__.__name__)
