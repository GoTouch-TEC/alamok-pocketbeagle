#!/bin/bash
/usr/bin/killall gpsd
/usr/bin/config-pin P2.09 uart
/usr/bin/config-pin P2.11 uart
/usr/bin/config-pin P2.07 uart
/usr/bin/config-pin P2.05 uart
/usr/sbin/gpsd /dev/ttyO1 -F /var/run/gpsd.sock
/usr/bin/pon fona
/bin/sleep 2
python3 -O /home/debian/alamok/Alamok.py -c /home/debian/mqtt_defaults.json -o /home/debian/Alamok.db
