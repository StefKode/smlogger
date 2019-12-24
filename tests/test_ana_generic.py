
from wrap_ana_generic import TestAnaGeneric
from rediscon_emu  import RedisConEmu

red = RedisConEmu(name="test", host="testhost")
ana = TestAnaGeneric(redObj=red, redKey="RED_KEY", opts=None, name="test_ana", debug=True)
ana.update(4)
print(ana.getTS())
ana.forceTS(123)
print(ana.getTS())
ana.forceTS(None)
print(ana.getTS())

