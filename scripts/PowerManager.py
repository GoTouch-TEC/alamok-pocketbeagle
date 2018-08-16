import Adafruit_BBIO.GPIO as GPIO
import serial
import time
import os
import json

GPIO.setup("P1_35", GPIO.IN)
GPIO.setup("P1_33", GPIO.OUT)
GPIO.output("P1_33", GPIO.LOW)
GPIO.add_event_detect("P1_35", GPIO.FALLING)
running = True
lastState = False
buttonPressed = False
lastTimePressed = time.time()
ser = serial.Serial(port = "/dev/ttyO2", baudrate=9600)
ser.close()
ser.open()
shutdown_pending=False

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
    # reescribir la funcion de deteccion de apagado

    # if(GPIO.event_detected("P1_35")):
    #     GPIO.output("P1_33", GPIO.HIGH)
    #     cont = 0
    #     for n in range(40):
    #         time.sleep(0.1)
    #         if(not GPIO.input("P1_35")):
    #             cont+=1
    #         else:
    #             break
    #     # GPIO.cleanup()
    #     if(cont>=20):
    #         print("shutdown")
    #         os.system("shutdown -P now")
    #         break
    #     else:
    #         print("reboot:")
    #         os.system("shutdown -r now")
    #         break
    #     running=False
    if(GPIO.event_detected("P1_35")):
        lastTimePressed = time.time();
        buttonPressed = True;
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
                # elif(data['value'] and shutdown_pending):
                #     print("canceled")
                #     os.system("shutdown -c")
                #     GPIO.output("P1_33", GPIO.LOW)
        except Exception as error:
            print("Error",error)
            time.sleep(2)
