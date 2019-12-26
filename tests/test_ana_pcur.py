
import sys
sys.path.append("..")

from modules.ana_pcur import AnaPCur
from rediscon_emu  import RedisConEmu
import tests
import time

red = RedisConEmu(name="PCUR", host="testhost")

tests.announceTest("AnaPCur instantiation")
try:
    ana = AnaPCur(redObj=red, 
                    redKey="RED_KEY_PCUR", 
                    opts={"avg_win_size": 10, "update_period": 30}, 
                    name="test_ana", 
                    debug=True)
    tests.assertEqual(1,1)

except Exception as e:
    tests.assertEqual(0,1, failtext=str(e))

