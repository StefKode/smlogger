# smlogger
Smart Meter SML Logger is an application to read Smart Meter Language (SML) from a serial port and log the measurements to a Redis Server for further processing.

Please feel free to ask questions for to provide feedback by opening a new issue or by commenting an existing one.

# Supported Environment
The following environment has been tested:
- eHZ Smart Meter with SML status on IR port
- HW is Raspberry PI Zero
- OS is Raspbian Buster-Lite
- Ansible playbook run from Ubuntu 18.04 LTS

# Software Overview
The software consists of the following components:
- Forked libsml from Volkszaehler (https://github.com/volkszaehler/libsml)
- smlogger application
- ansible remote deploymnent
- redis connection manager (https://github.com/StefKode/rediscon)

## Forked LibSML
The libsml implementation from Volkszahler is the best implementation to read the SML protocol from a serial device. It contains a sample sml-server which decodes all received SML objects and writes them to stdout. In the fork this sample server has been modifed to print this data for easy parsing.

Also a script *smlmon* has been added which publishes the current power consumption and the total power counter to a mqtt broker. None of the core libsml functions has been modifed. I decided for the fork because I re-use he build system to create the modified server.

## smlogger application
This is a python script which subscribes to the mqtt messages from libsml. It does averaging and publishes the two power values to a Redis server based on a time trigger. In order to configure the program there is a config file *smlogger.conf*. This json file has the following keys:

| Config Key    | Example value | Description |
| ------------- | ------------- | ----- |
| redis_server  | 192.168.178.10   | redis server hostname or IP address |
| power_current_key | PowerCurrent | redis key to store the current power (Watt) |
| power_day_key | PowerCurrentDay  | redis key to store the daily power usage (kWh). This value increments on the day and resets afer 0:00 |
| ts_key | PowerTS | redis key to store capture time stamp |
| mqtt_topic | powlog | this is the topic to which libsml logs the data, this should not be changed |
| update_period | 30 | time interval in seconds at which redis values are updated (must be > 4s) |
| avg_window_size | 5 | size of the sliding average window |

## Install using ansible deployment
The complete system configuration and the application deployment and configuration is performed using ansible. Make sure ansible has been installed (apt-get install ansible). The ánsible playbook uses a configuration file *config.yml*:

| Config Key    | Description |
| ------------- | ----- |
| SERVER_HOST   | target hostname or IP address where the installation is to be performed |
| TIMEZONE | standardized timezone string (e.g. Europe/Berlin) |
| ASK_PASSWD | set to *yes* to aks for user password on target or use *no* if you copied your ssh public key |

Note: as the development has been done on Raspberry PI the user is hardcoded to "pi". You need to change *smlogger.yml* if you use a different name.

### Installation instructions
- download rapsbian buster, then configure and enable Wifi and ssh
- setup your Raspberry PI and make sure it is running and reachable
- clone this repository
- in directory *deployment* create *config.yml* based on the example file *config.yml-example* and apply changes as needed
- copy the file *smlogger.conf-example* to *smlogger.conf* and apply all settings
- cd into *deployment*
- type *make*

# Hardware Overview
The following section outlines some facts of the hardware design.
## Schematics of IR sensor
![Schematics Picture](schmatics/schematics.png?raw=true "IR Sensor Schematics")
## Prototype IR Sensor attached to Smart Meter
![IR PCB Picture](images/sch.jpg?raw=true width=100)
## RPI-Z with Magnet-Mount
![RPI-Z Picture](images/sch.jpg?raw=true "RPI-Z with magnet mount")
