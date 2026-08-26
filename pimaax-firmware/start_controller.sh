#!/bin/bash

sudo killall gpsd >/dev/null 2>&1
sudo rm -f /var/run/gpsd.sock
sudo gpsd -n /dev/ttyACM0 -F /var/run/gpsd.sock

gpspipe -w -n 10 > /dev/null &

sleep 10

source /home/chirag/pimaax-firmware/.pimaax_env/bin/activate
python /home/chirag/pimaax-firmware/main.py
