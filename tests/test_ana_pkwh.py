import sys
sys.path.append("..")

from modules.ana_pkwh import AnaPKwh
from rediscon_emu  import RedisCon
import tests
import time
import sys

red = RedisCon(name="PKWH", host="testhost")
red.setConMonInterval(1)
red.connect()

tests.announceTest("AnaPKwh instantiation")
try:
    ana = AnaPKwh(redObj=red, 
                    opts={"power_kwh_key": "RED_KEY_PKWH",
                          "kwh_period":    30}, 
                    debug=True)
    tests.assertEqual(1,1)

except Exception as e:
    tests.assertEqual(0,1, failtext=str(e))

ana.print_opts()
tests.announceTest("AnaPKwh - check accumulation and redis usage")
ana.overwrite_last_ts(0)
ana.forceTS(0)
ana.update(1000)
tests.assertEqual(red.getLastKey(), None, "redis key not set yet")
tests.assertEqual(red.getLastVal(), None, "redis val not set yet")
sys.exit()
ana.forceTS(30)
ana.update(1500)
tests.assertEqual(red.getLastKey(), "RED_KEY_PKWH")
tests.assertEqual(red.getLastVal(), 0.5)
ana.forceTS(60)
ana.update(1700)
tests.assertEqual(red.getLastVal(), 0.7)
ana.forceTS(95)
ana.update(2700)
tests.assertEqual(red.getLastVal(), 1.7)
ana.force_dm(0)
ana.forceTS(140)
ana.update(3700)
tests.assertEqual(red.getLastVal(), 0.0)
ana.forceTS(170)
ana.update(4000)
tests.assertEqual(red.getLastVal(), 0.3)
ana.forceTS(180)
ana.update(4100)
tests.assertEqual(red.getLastVal(), 0.3)
ana.forceTS(200)
ana.update(4200)
tests.assertEqual(red.getLastVal(), 0.5)


