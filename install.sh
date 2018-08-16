#! /bin/bash

INSTALL_PATH="/opt/Alamok-Setup"

#remove current installation
rm -rf "${INSTALL_PATH}"
mkdir "${INSTALL_PATH}"

#fona conf
echo "Copying fona PPP Configuration"
cp fona/fona  /etc/ppp/peers/fona

#copy scripts
mkdir "${INSTALL_PATH}/scripts"
SCRIPTS=scripts/*
for f in $SCRIPTS
do
	echo "Copying ${f##*/}"
	chmod +x $f
	cp $f "$INSTALL_PATH/${f}"
done

#copy and eneable services
SERVICES=services/*
for f in $SERVICES
do
        echo "Copying ${f##*/}  "
        cp $f "/etc/systemd/system/${f##*/}"
	systemctl enable ${f##*/}
	echo "Enabling ${f##*/}"
#	systemctl start  ${f##*/}
done


echo "Done"
