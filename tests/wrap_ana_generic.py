
import sys
sys.path.append("..")

from modules.ana_generic import AnaGeneric


class TestAnaGeneric(AnaGeneric):

    def _init(self):
        print("TestAnaGeneric: init")

    def _update(self):
        print("TestAnaGeneric: update = %s" % str(self._inval))

    def getLastVal(self):
        return self._inval

    def getTS(self):
        return self._get_ts()
