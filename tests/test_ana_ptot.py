import sys
sys.path.append("..")

from modules.ana_ptot import AnaPTot
from rediscon_emu  import RedisCon
import tests
import time

red = RedisCon(name="PTOT", host="testhost")
red.setConMonInterval(1)
red.connect()

tests.announceTest("AnaPTot instantiation")
try:
    ana = AnaPTot(redObj=red, 
                    opts={"power_day_key":   "RED_KEY_PTOT",
                          "update_period":   30}, 
                    debug=True)
    tests.assertEqual(1,1)

except Exception as e:
    tests.assertEqual(0,1, failtext=str(e))

ana.print_opts()
tests.announceTest("AnaPTot - check accumulation and redis usage")
ana.overwrite_last_dm(100)
ana.force_dm(200)
ana.overwrite_last_ts(0)
ana.forceTS(0)
ana.update(1000)
tests.assertEqual(red.getLastKey(), None, "redis key not set yet")
tests.assertEqual(red.getLastVal(), None, "redis val not set yet")
ana.forceTS(30)
ana.update(1500)
tests.assertEqual(red.getLastKey(), "RED_KEY_PTOT")
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

tests.announceTest("AnaPTot check day marker")
from datetime import datetime
h = datetime.now(tz=datetime.now().astimezone().tzinfo).hour
m = datetime.now(tz=datetime.now().astimezone().tzinfo).minute
marker = (h * 100) + m
tests.log(marker)
ana.force_dm(None)
tests.assertEqual(ana._get_day_mark(), marker)

