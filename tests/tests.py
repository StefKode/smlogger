from colorama import Fore, Back, Style

_cAN = Fore.BLUE  + Style.BRIGHT 
_cOK = Fore.GREEN + Style.BRIGHT
_cER = Fore.RED   + Style.BRIGHT
_RST = Style.RESET_ALL

_count = 0

def announceTest(name):
    global _count
    print(_cAN + "[%2d] TESTCASE: %s%s" % (_count, name, _RST))
    _count += 1
    

def assertEqual(a,b):
    if a == b:
        print(_cOK + "[%2d] Test PASS %s" %(_count, _RST))
    else:
        print(_cER + "[%2d] Test FAIL" % _count)
        print("[%2d] A = %s"   % (_count, str(a)))
        print("[%2d] B = %s%s" % (s_count, str(b), _RST))
