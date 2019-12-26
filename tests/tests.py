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
    

def assertEqual(a,b, descr=None, failtext=None):
    if a == b:
        if descr is not None:
            print(_cOK + "[%2d] Info: %s" % (_count, str(descr)))
        print(_cOK + "[%2d] A = %s"       % (_count, str(a)))
        print(       "[%2d] B = %s"       % (_count, str(b)))
        print(       "[%2d] Test PASS %s" % (_count, _RST))
    else:
        if descr is not None:
            print(_cER + "[%2d] Info: %s" % (_count, str(descr)))
        print(_cER +     "[%2d] A = %s"   % (_count, str(a)))
        print(           "[%2d] B = %s"   % (_count, str(b)))

        if failtext is not None:
            print("%s" % str(failtext))
        print("[%2d] Test FAIL%s" % (_count, _RST))
