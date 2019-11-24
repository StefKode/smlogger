# smlogger
Smart Meter SML Logger is an application to read Smart Meter Language (SML) from a serial port and log the measurements to a Redis Server for further processing.

# Supported Environment
The following environment has been tested:
- eHZ Smart Meter with SML status on IR port
- HW is Raspberry PI Zero
- OS is Raspbian Buster-Lite
- Ansible playbook run from Ubuntu 18.04 LTS

# Software Overview
The software consists of two major components:
- Forked libsml from Volkszaehler (https://github.com/volkszaehler/libsml)
- smlogger application
- ansible remote deploymnent
## Forked LibSML
The libsml implementation from Volkszahler is the best implementation to read the SML protocol from a serial device. It contains a sample sml-server which decodes all received SML objects and writes them to stdout. In the fork this sample server has been modifed to print this data for easy parsing.

Also a script *smlmon* has been added which publishes the current power consumption and the total power counter to a mqtt broker. None of the core libsml functions has been modifed. I decided for the fork because I re-use he build system to create the modified server.
## smlogger application
This is a python script which subscribes to the mqtt messages from libsml. It does averaging and publishes the two power values to a Redis server based on a time trigger. In order to configure the program there is a config file *smlogger.conf*. This json file has the following keys:

| Config Key    | Example value | Description |
| ------------- | ------------- | ----- |
| redis_server  | 192.168.178.10   | redis server hostname or IP address |
| power_current_key | PowerCurrent | redis key to store the current power (Watt) |
| power_day_key | PowerCurrentDay  | redis key to store the daily power usage (kWh) |
| mqtt_topic | powlog (default!) | this is the topic to which libsml logs the data, this should not be changed |
| update_period | 30 | time interval in seconds at which redis values are updated (must be > 4s and < 20min) |
| avg_window_size | 5 | size of the sliding average window |

# Hardware Overview
to come
