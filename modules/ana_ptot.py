
from datetime import datetime
from modules.ana_generic import AnaGeneric

class AnaPTot(AnaGeneric):
    def _init(self):
        self._update_period   = self._opts["update_period"]
        self._redis_key       = self._opts["power_day_key"]
        self._tzone           = datetime.now().astimezone().tzinfo
        self._force_dm        = None
        self._last_dm         = self._get_day_mark()
        self._last_ts         = self._get_ts()
        self._value           = None
        self._day_start       = None
        self._last_kwh_sample = 0
        self._last_kwh        = 0
        

    def _update(self):
        ts = self._get_ts()
        dm = self._get_day_mark()

        # check if we just crossed the day start (00:00) - if so, reset 
        # the total power capture of the day
        if dm < self._last_dm:
            self._day_start = self._inval
        self._last_dm = dm

        if self._day_start is None:
            self._day_start = self._inval

        if (ts - self._last_ts) >= self._update_period:
            pdelta = self._inval - self._day_start
            #convert wh to kwh and send to redis
            self._red.set(self._redis_key, float("{0:.2f}".format(pdelta/1000)))
            self._value   = pdelta/1000
            self._last_ts = ts


    # turns a hour + minute into a single numerical value
    # e.g. 23:30 will become the value 2330
    def _get_day_mark(self):
        if self._force_dm is not None:
            return self._force_dm

        h = datetime.now(tz=self._tzone).hour
        m = datetime.now(tz=self._tzone).minute
        marker = (h * 100) + m
        return marker


    def force_dm(self, value):
        self._force_dm = value


    def overwrite_last_dm(self, value):
        self._last_dm = value


    def overwrite_last_ts(self, value):
        self._last_ts = value

# vim: set expandtab ts=4:
