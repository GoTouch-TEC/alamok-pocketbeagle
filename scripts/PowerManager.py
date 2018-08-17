import Adafruit_BBIO.GPIO as GPIO
import serial
import time
import os
import json

# Pins setup
GPIO.setup("P1_35", GPIO.IN)
GPIO.setup("P1_33", GPIO.OUT)
GPIO.output("P1_33", GPIO.LOW)
GPIO.add_event_detect("P1_35", GPIO.FALLING)

# Flags for the reset/turnoff button
lastState = False
buttonPressed = False
lastTimePressed = time.time()


Serial port Setup
ser = serial.Serial(port = "/dev/ttyO2", baudrate=9600)
ser.close()
ser.open()

# checks for the system's initial state
while(True):
    if ser.isOpen():
        try:
            ser.write(b'USB')
            datos =str(ser.readline())
            print(datos)
            data = json.loads(datos[datos.index("{"):datos.index("}")+1])
            lastState = data['value']
            break

        except Exception as error:
            print("Error",error)
            time.sleep(1)


while(True):
    # checks if the button has been pressed
    if(GPIO.event_detected("P1_35")):
        lastTimePressed = time.time();
        buttonPressed = True;

    # checks if the button has been released
    elif(buttonPressed and GPIO.input("P1_35")):
        buttonPressed = False;
        if(time.time() - lastTimePressed > 4):
            print("shutdown")
            GPIO.output("P1_33", GPIO.HIGH)
            ser.close()
            os.system("poweroff")
            break
        else:
            print("reboot")
            GPIO.output("P1_33", GPIO.HIGH)
            ser.close()
            os.system("reboot")
            break

    if ser.isOpen():
        try:
            # checks the system's USB charging status
            ser.write(b'USB')
            datos =str(ser.readline())
            print(datos)
            data = json.loads(datos[datos.index("{"):datos.index("}")+1])
            if(lastState != data['value']):
                lastState = data['value']
                if(data['value']==0 ):
                    print("shutdown")
                    GPIO.output("P1_33", GPIO.HIGH)
                    ser.close()
                    os.system("poweroff")
                    break
                    shutdown_pending=True
        except Exception as error:
            print("Error",error)
            time.sleep(2)
