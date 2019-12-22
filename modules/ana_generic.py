from datetime import datetime

class AnaGeneric():
    def __init__(self, redObj, redKey, opts, name="unset", debug=False):
        self._red   = redObj
        self._red_key = redKey
        self._opts  = opts
        self._inval = None
        self._debug = debug
        self._name  = name
        self._first = True
        self._init()

    def _init():
        raise ValueError("[%-10s] ERROR! _init not defined" % self._name)

    def _debug(text):
        if self._debug:
            print("[%-10s] %s" % (self._name, text))

    def update(self, value):
        self._inval = value
        self._update()

    def _get_ts(self):
        return int(datetime.now().timestamp())

    def _update(self):
        raise ValueError("[%-10s] ERROR! _update not defined" % self._name)

# vim: set expandtab ts=4:
