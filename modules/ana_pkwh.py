
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
        self._count           = 0
        
    def print_opts(self):
        self._print_opts("timing", "kwh_period", self._update_period)
        self._print_opts("redis",  "power_kwh_key", self._red_key)

    def _update(self):
        ts = self._get_ts()

        self._sumvalue += self._inval
        self._count    += 1
        tdelta          = ts - self._last_ts

        if tdelta >= self._update_period:
            # compensate for sampling shifts (scaling)
            # used to assume one power addition per second
            corr  = tdelta / self._count
            # get power area as a fraction of one hour
            # Notes:
            #  - everything is normed to 1 second
            #  - sumvalue can be assumed to be the addition of 60 power measurements
            #  - delta t is therefore 1s (left out of the code)
            #  - this function reports the sum of these fragments per update_period
            #  - as the unit is kwh we need to divide by 3600 because delta t is 1s
            #    and divide by 1000 to get from W to kWh
            pkwh  = (self._sumvalue * corr) / (3600 * 1000)

            #send to redis
            self._red.set(self._red_key, float("{0:.4f}".format(pkwh)))
            self._value    = pkwh
            self._sumvalue = 0
            self._count    = 0
            self._last_ts  = ts


    def overwrite_last_ts(self, value):
        self._last_ts = value

# vim: set expandtab ts=4:
