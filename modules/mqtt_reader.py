import paho.mqtt.client as mqtt
import json

_func_update = None
_mqtt_topic  = "#"

#
# (mqtt callback)
# called for every message on mqtt topic
# here we convert the json to python-dictionary
# any conversion error leads to ignore the message
#
def _mqtt_message(client, userdata, msg):
    if (_mqtt_topic == msg.topic):
        try:
            data = json.loads(msg.payload.decode("utf-8"))
        except:
            print("error json decode")
            print(str(msg.payload))
            return
        if _func_update is not None:
            _func_update(data)
        else:
            print("Warning: no mqtt update function registered")

#
# (mqtt callback)
# connection indicator, were we subscribe to the powlog mqtt topic
#
def _mqtt_connect(client, userdata, flags, rc):
    print("OK " + str(rc))
    client.subscribe(_mqtt_topic)


def mqtt_run_forever(host, topic, update_cb):
    global _func_update
    global _mqtt_topic
    print("connect MQTT..")
    client = mqtt.Client()
    _func_update = update_cb
    _mqtt_topic  = topic
    client.on_connect = _mqtt_connect
    client.on_message = _mqtt_message
    client.connect(host, 1883, 60)
    client.loop_forever()

# vim: set expandtab ts=4:
