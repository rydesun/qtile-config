from libqtile.widget import ThermalSensor as _ThermalSensor


class ThermalSensor(_ThermalSensor):
    def poll(self):
        return " " + super().poll().replace(".0", "")
