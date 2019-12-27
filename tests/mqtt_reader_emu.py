from time import sleep

_func_update = None

#
# (mqtt callback)
# called for every message on mqtt topic
# here we convert the json to python-dictionary
# any conversion error leads to ignore the message
#
def _mqtt_message(data):
        if _func_update is not None:
            _func_update(data)
        else:
            print("Warning: no mqtt update function registered")

def mqtt_run_forever(host, topic, update_cb):
    global _func_update
    print("connect MQTT..")
    _func_update = update_cb
    _mqtt_message({"ptot": 300000, "pmon": 100})
    sleep(20)
    _mqtt_message({"ptot": 300100, "pmon": 100})
    sleep(20)
    _mqtt_message({"ptot": 300200, "pmon": 100})
    sleep(20)
    _mqtt_message({"ptot": 300300, "pmon": 100})
    sleep(20)
    _mqtt_message({"ptot": 300400, "pmon": 100})
    sleep(20)
    _mqtt_message({"ptot": 300600, "pmon": 200})
    sleep(20)
    _mqtt_message({"ptot": 300650, "pmon": 50})
    sleep(20)
    _mqtt_message({"ptot": 300700, "pmon": 50})

# vim: set expandtab ts=4:
