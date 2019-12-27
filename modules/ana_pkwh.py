
from datetime import datetime
from modules.ana_generic import AnaGeneric

class AnaPKwh(AnaGeneric):
    def _init(self):
        self._name            = "AnaPKwh"
        self._update_period   = self._opts["kwh_period"]
        self._red_key         = self._opts["power_kwh_key"]
        self._tzone           = datetime.now().astimezone().tzinfo
        self._last_ts         = self._get_ts()
        self._value           = 0
        self._sumvalue        = 0
        
    def print_opts(self):
        self._print_opts("timing", "kwh_period", self._update_period)
        self._print_opts("redis",  "power_kwh_key", self._red_key)

    def _update(self):
        ts = self._get_ts()

        self._sumvalue += self._inval
        tdelta = ts - self._last_ts
        print(tdelta, self._sumvalue)

        if tdelta >= self._update_period:
            pkwh  = (self._sumvalue * tdelta) / (60 * 60 * 1000)
            print(pkwh)

            #convert wh to kwh and send to redis
            self._red.set(self._red_key, float("{0:.2f}".format(pkwh)))
            self._value    = pkwh
            self._sumvalue = 0
            self._last_ts  = ts


    def overwrite_last_ts(self, value):
        self._last_ts = value

# vim: set expandtab ts=4:
