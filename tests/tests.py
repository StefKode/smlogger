import sys

try:
    open(".bold-output").close()
    bold_out = True
except:
    bold_out = False

if bold_out:
    from colorama import Fore, Back, Style
    _cAN = Fore.BLUE  + Style.BRIGHT 
    _cOK = Fore.GREEN + Style.BRIGHT
    _cER = Fore.RED   + Style.BRIGHT
    _RST = Style.RESET_ALL
else:
    _cAN = ""
    _cOK = ""
    _cER = ""
    _RST = ""

_count = 0

def announceTest(name):
    global _count
    _count += 1
    print(_cAN + "[%2d] %s%s" % (_count, name, _RST))
    

def assertEqual(a,b, descr=None, failtext=None):
    if a == b:
        if bold_out:
            if descr is not None:
                print(_cOK + "[%2d] Info: %s" % (_count, str(descr)))
            print(_cOK + "[%2d] A = %s"       % (_count, str(a)))
            print(       "[%2d] B = %s"       % (_count, str(b)))

        print(       "[%2d] PASS %s" % (_count, _RST))
    else:
        if bold_out:
            if descr is not None:
                print(_cER + "[%2d] Info: %s" % (_count, str(descr)))
            print(_cER +     "[%2d] A = %s"   % (_count, str(a)))
            print(           "[%2d] B = %s"   % (_count, str(b)))

        if failtext is not None:
            print("%s" % str(failtext))
        print("[%2d] FAIL%s" % (_count, _RST))

        sys.exit(1)

def log(text):
    print("[%2d] %s" % (_count, text))
