
import sys
sys.path.append("..")

from modules.ana_pcur import AnaPCur
from rediscon_emu  import RedisCon
import tests
import time

red = RedisCon(name="PCUR", host="testhost")
red.setConMonInterval(1)
red.connect()

tests.announceTest("AnaPCur instantiation")
try:
    ana = AnaPCur(redObj=red, 
                    opts={"power_current_key": "RED_KEY_PCUR", 
                          "avg_win_size":      10, 
                          "update_period":     30}, 
                    debug=True)
    tests.assertEqual(1,1)

except Exception as e:
    tests.assertEqual(0,1, failtext=str(e))

ana.print_opts()
tests.announceTest("AnaPCur windowing function - startup")
ana.update(5)
ana.update(5)
ana.update(5)
ana.update(5)
ana.update(5)
tests.assertEqual(ana.getValue(), 2.5, "window half filled", str(ana._val_window))

tests.announceTest("AnaPCur windowing function - fillup")
ana.update(5)
ana.update(5)
ana.update(5)
ana.update(5)
ana.update(5)
tests.assertEqual(ana.getValue(), 5, "window full filled", str(ana._val_window))

tests.announceTest("AnaPCur windowing function - fill 0s")
ana.update(0)
ana.update(0)
ana.update(0)
ana.update(0)
ana.update(0)
tests.assertEqual(ana.getValue(), 2.5, "window 0/5 filled", str(ana._val_window))

tests.announceTest("AnaPCur value update after timeout")
tests.assertEqual(red.getLastKey(), None, "redis key not set yet")
tests.assertEqual(red.getLastVal(), None, "redis val not set yet")
tests.log("force TS")
ana.forceTS(100)
tests.log("force last TS")
ana.overwrite_last_ts(100)
tests.log("inject value")
ana.update(0)
tests.log("advance TS by 30")
ana.forceTS(160)
ana.update(0)
tests.assertEqual(red.getLastKey(), "RED_KEY_PCUR", "redis should be updated with key", str(ana._last_ts))
tests.assertEqual(red.getLastVal(), 1.5,            "redis should be updated with value")

