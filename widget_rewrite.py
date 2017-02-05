def new_net_get_stats(self):
    lines = []
    with open('/proc/net/dev', 'r') as f:
        lines = f.readlines()[2:]
    interfaces = {}
    down = 0
    up = 0
    for s in lines:
        int_s = s.split()
        down += float(int_s[1])
        up += float(int_s[-8])
    interfaces = {'down': down, 'up': up}
    return interfaces
def new_net_poll(self):
    try:
        new_int = self.get_stats()
        down = new_int['down'] - self.interfaces['down']
        up = new_int['up'] - self.interfaces['up']
        down = down / self.update_interval
        up = up / self.update_interval

        def humanize_bytes(value):
            suff = ["B", "K", "M", "G", "T"]
            while value > 1024. and len(suff) > 1:
                value /= 1024.
                suff.pop(0)
            if value > 921 and len(suff) > 1:
                value /= 1024.
                suff.pop(0)
                return "%.1f%s" % (value, suff[0])
            if value > 0 and suff[0] == "B":
                return "*B"
            if value == 0:
                return "N"
            return "%d%s" % (value, suff[0])

        down = humanize_bytes(down)
        up = humanize_bytes(up)
        str_base = "%s-%s"

        self.interfaces = new_int
        return str_base % (down, up)
    except Exception:
        logger.error('%s: device is switched off?', self.__class__.__name__)
def new_backlight_poll(self):
    info = self._get_info()
    if not info:
        return 'Error'
    percent = info['brightness'] / info['max']
    return '{percent:2.0%}'.format(percent=percent)
def new_battery_update(self):
        ntext = self._get_text()
        if ntext == 'Full':
            ntext = '\uf136100%'
        if ntext != self.text:
            self.text = ntext
            self.bar.draw
