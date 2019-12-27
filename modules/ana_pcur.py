
from modules.ana_generic import AnaGeneric

class AnaPCur(AnaGeneric):
    def _init(self):
        self._name          = "AnaPCur"
        self._avg_win_size  = self._opts["avg_win_size"]
        self._update_period = self._opts["update_period"]
        self._red_key       = self._opts["power_current_key"]
        self._val_window    = [0] * self._avg_win_size
        self._last_ts       = self._get_ts()
        

    def print_opts(self):
        self._print_opts("timing", "update_period",     self._update_period)
        self._print_opts("redis",  "power_current_key", self._red_key)
        self._print_opts("algo",   "avg_win_size",      self._avg_win_size)

    def _update(self):
        self._window_insert(self._inval)
        self._value = self._window_avg()
        ts = self._get_ts()
        if (ts - self._last_ts) >= self._update_period:
            self._red.set(self._red_key, self._value)
            self._last_ts = ts


    def _window_insert(self, v):
        size = self._avg_win_size
        for i in range(0, size - 1):
            self._val_window[i] = self._val_window[i + 1]
        self._val_window[size - 1] = v


    def _window_avg(self):
        size = self._avg_win_size
        avg  = 0
        for i in range(0, size):
            avg += self._val_window[i]
        return avg / size

    def getValue(self):
        return self._value

    def overwrite_last_ts(self, value):
        self._last_ts = value

# vim: set expandtab ts=4:
