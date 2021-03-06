from datetime import datetime

class AnaGeneric():
    def __init__(self, redObj, opts, debug=False):
        self._name  = "ana-generic"
        self._red   = redObj
        self._opts  = opts
        self._inval = None
        self._debug = debug
        self._first = True
        self._forced_ts = None
        self._value = None
        self._init()

    def _print_opts(self, hint, key, value):
        print("[%s] Type: %-8s %-18s: %s" % (self._name, hint, key, str(value)))

    def _init(self):
        raise ValueError("[%-10s] ERROR! _init not defined" % self._name)

    def _debug(self, text):
        if self._debug:
            print("[%-10s] %s" % (self._name, text))

    def update(self, value):
        self._inval = value
        self._update()

    def forceTS(self, value):
        self._forced_ts = value

    def getValue(self):
        return self._value

    def _get_ts(self):
        if self._forced_ts is None:
            return int(datetime.now().timestamp())
        else:
            return self._forced_ts

    def _update(self):
        raise ValueError("[%-10s] ERROR! _update not defined" % self._name)

# vim: set expandtab ts=4:
