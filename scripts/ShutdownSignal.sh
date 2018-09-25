#! /bin/bash
INSTALL_PATH="/opt/Alamok-Setup/scripts"
lsof -t /dev/ttyO2 | xargs --no-run-if-empty kill -9
/bin/systemctl list-jobs | egrep -q 'reboot.target.*start' || echo "shutdown"|python3 "${INSTALL_PATH}/ShutdownSignal.py"
config-pin p1.33 lo
config-pin p1.34 lo
config-pin p1.36 lo
config-pin  p2.18 lo
config-pin  p2.6 lo
