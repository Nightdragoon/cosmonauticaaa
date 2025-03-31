import serial
import requests
import time
direccion = "98:D3:21:F7:5A:17"

arduino = serial.Serial(port="/dev/ttyUSB0", baudrate=9600 ,timeout=.1)

arduino.write(bytes("hola" , 'utf-8'))
time.sleep(2)

vuelto = arduino.readline().decode("utf-8")
print(vuelto)



