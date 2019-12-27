import sys
sys.path.append("..")

from modules.ana_ptot import AnaPTot
from rediscon_emu  import RedisConEmu
import tests
import time

red = RedisConEmu(name="PTOT", host="testhost")
red.setConMonInterval(1)
red.connect()

tests.announceTest("AnaPTot instantiation")
try:
    ana = AnaPTot(redObj=red, 
                    opts={"power_day_key":   "RED_KEY_PTOT",
                          "update_period":   30}, 
                    name="test_ana_ptot", 
                    debug=True)
    tests.assertEqual(1,1)

except Exception as e:
    tests.assertEqual(0,1, failtext=str(e))

#tests.announceTest("AnaPTot windowing function - startup")

