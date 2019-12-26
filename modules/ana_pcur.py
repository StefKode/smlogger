
from modules.ana_generic import AnaGeneric

class AnaPCur(AnaGeneric):
    def _init(self):
        self._avg_win_size  = self._opts["avg_win_size"]
        self._update_period = self._opts["update_period"]
        self._val_window = [0] * self._avg_win_size
        self._last_ts = self._get_ts()
        

    def _update(self):
        self._window_insert(self._inval)
        ts = self._get_ts()
        if (ts - self._last_ts) >= self._update_period:
            self._red.set(self._red_key, self._window_avg())
            self._last_ts = ts

    def _window_insert(self, v):
        size = self._avg_win_size

        for i in range(0, size - 1):
            self._val_window[i] = self._val_window[i + 1]

        self._val_window[size - 1] = v


    def _window_avg(self, ):
        size = self._avg_win_size
        avg  = 0
        for i in range(0, size):
            avg += self._val_window[i]
        return int(avg / size)


# vim: set expandtab ts=4:
