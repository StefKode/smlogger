
from wrap_ana_generic import TestAnaGeneric
from rediscon_emu  import RedisConEmu
import tests
import time

red = RedisConEmu(name="test", host="testhost")

tests.announceTest("AnaGeneric instantiation")
try:
    ana = TestAnaGeneric(redObj=red, redKey="RED_KEY", opts=None, name="test_ana", debug=True)
    tests.assertEqual(1,1)
except:
    tests.assertEqual(0,1)

tests.announceTest("AnaGeneric TS")
t1 = ana.getTS()
time.sleep(1)
t2 = ana.getTS()
tests.assertEqual(t1, t2 - 1)

tests.announceTest("AnaGeneric TS Force")
ana.forceTS(123)
t1 = ana.getTS()
ana.forceTS(120)
time.sleep(1)
t2 = ana.getTS()
tests.assertEqual(t1, t2 + 3)

tests.announceTest("AnaGeneric TS reset force")
ana.forceTS(None)
t1 = ana.getTS()
time.sleep(1)
t2 = ana.getTS()
tests.assertEqual(t1, t2 - 1)


