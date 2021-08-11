from libqtile.widget.battery import Battery as _Battery, BatteryState

from .base import TextBox


class Battery(TextBox, _Battery):
    def __init__(self, *args, **kwargs):
        self.defaults.extend((
            ("sep", (0.85, 0.65, 0.4, 0.25)),
            ("icon_charge", ""),
            ("icon_plug", ""),
            ("icon_full_energy", ""),
            ("icon_high_energy", ""),
            ("icon_half_energy", ""),
            ("icon_low_energy", ""),
            ("icon_empty_energy", ""),
            ("foreground", ""),
            ("foreground_discharge", ""),
            ("foreground_low", ""),
        ))
        super().__init__(*args, **kwargs)

    def build_string(self, status):
        if self.layout is not None:
            if status.state == BatteryState.DISCHARGING:
                if status.percent < self.low_percentage:
                    self.layout.colour = self.foreground_low
                else:
                    self.layout.colour = self.foreground_discharge
            else:
                self.layout.colour = self.foreground
        if len(self.sep) == 4:
            if status.percent >= self.sep[0]:
                icon = self.icon_full_energy
            elif status.percent >= self.sep[1]:
                icon = self.icon_high_energy
            elif status.percent >= self.sep[2]:
                icon = self.icon_half_energy
            elif status.percent >= self.sep[3]:
                icon = self.icon_low_energy
            else:
                icon = self.icon_empty_energy

        if status.state == BatteryState.CHARGING:
            extra_icon = self.icon_charge
        elif status.state == BatteryState.DISCHARGING:
            extra_icon = self.icon_discharge
        else:
            extra_icon = ""

        hour = status.time // 3600
        minute = (status.time // 60) % 60

        return self.format.format(
            icon=icon,
            percent = status.percent*100 if status.percent < 1 else 100,
            watt=status.power,
            hour=hour,
            min=minute,
            extra_icon=extra_icon,
        )
