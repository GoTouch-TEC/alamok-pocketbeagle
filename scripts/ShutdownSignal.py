import serial

ser = serial.Serial(port = "/dev/ttyO2", baudrate=9600)
ser.close()
ser.open()
if ser.isOpen():
        print ("Serial is open!")
        ser.write(b'OFF10')
ser.close()
