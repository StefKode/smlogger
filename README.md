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
This is a python script which subscribes to the mqtt messages from libsml. It does some averaging and publishes the two power values to a configurable Redis server and key based on a time trigger. In order to configure smlogger there is a config file *smlogger.conf*. This json file has the following key to control smlogger:

# Hardware Overview
to come
