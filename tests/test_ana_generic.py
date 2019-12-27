
from wrap_ana_generic import TestAnaGeneric
from rediscon_emu  import RedisConEmu
import tests
import time

red = RedisConEmu(name="test", host="testhost")

tests.announceTest("AnaGeneric instantiation")
try:
    ana = TestAnaGeneric(redObj=red, opts=None, name="test_ana", debug=True)
    tests.assertEqual(1,1,"Instance OK")
except:
    tests.assertEqual(0,1,"Instance failure")

tests.announceTest("AnaGeneric TS")
t1 = ana.getTS()
time.sleep(1)
t2 = ana.getTS()
tests.assertEqual(t1, t2 - 1, "one second advance")

tests.announceTest("AnaGeneric TS Force")
ana.forceTS(123)
t1 = ana.getTS()
ana.forceTS(120)
time.sleep(1)
t2 = ana.getTS()
tests.assertEqual(t1, t2 + 3, "set any TS value")

tests.announceTest("AnaGeneric TS reset force")
ana.forceTS(None)
t1 = ana.getTS()
time.sleep(1)
t2 = ana.getTS()
tests.assertEqual(t1, t2 - 1, "advance TS after un-force")

tests.announceTest("AnaGeneric set input value")
ana.update(345)
tests.assertEqual(ana.getLastVal(), 345, "set update value")
