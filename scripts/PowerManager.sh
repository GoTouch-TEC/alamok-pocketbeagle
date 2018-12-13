#!/bin/bash
config-pin P1.08 uart
config-pin P1.10 uart
config-pin p1.33 gpio
config-pin p1.34 gpio
config-pin p1.36 gpio
config-pin p1.35 in
config-pin  p2.18 hi
config-pin  p2.6 hi
config-pin  p2.4 in
INSTALL_PATH="/opt/Alamok-Setup/scripts"
python3 -O "${INSTALL_PATH}/PowerManager.py"
