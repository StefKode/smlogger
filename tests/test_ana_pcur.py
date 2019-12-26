
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

tests.announceTest("AnaPCur windowing function - startup")
ana.update(5)
ana.update(5)
ana.update(5)
ana.update(5)
ana.update(5)
tests.assertEqual(ana._value, 2.5, "window half filled", str(ana._val_window))
