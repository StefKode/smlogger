
class RedisConEmu():
    def __init__(self, name="not-set", host=None, port=6379, db=0, log_enabled=False, trx_log=False):
        self.name = name
        self.host = host
        self.port = port
        self.db = db
        self.log_enabled = log_enabled
        self.trx_log = trx_log
        self._lastval = None
        self._lastkey = None

    def _log(text):
        print("[RedisCon-Emu]: %s" % text)


    def getVersion(self):
        return "Redis Con Emulator"


    def setConMonInterval(self, secs):
        self._log("setConMonInterval = %d" % secs)


    def connect(self):
        self._log("setConMonInterval = %d" % secs)
        if self.connected:
            self._log("error: redis is already connected")
            return
        self.connected = True

    def subscribeToList(self, sublist):
        self._log("subscribe: %s" % str(sublist))

    def get(self, key):
        if not self.connected:
            self._log("ERROR - get on closed connection")
        self._log("ERROR - get Emulation not implemeneted")

 
    def set(self, key, value):
        if not self.connected:
            self._log("ERROR - set on closed connection")
        self._log("set(%s) = %s" % (str(key), str(value)))
        self._lastval = value
        self._lastkey = key


    def getLastKey():
        return self._lastkey


    def getLastValue():
        return self._lastval


    def subscribedChanges(self):
        if not self.connected:
            self._log("ERROR - subscribedChanges on closed connection")
        self._log("ERROR - subscribedChanges Emulation not implemeneted")

    def close(self):
        if not self.connected:
            self._log("ERROR - close() on closed connection")
        self._log("close redis")
        self.connected = False

