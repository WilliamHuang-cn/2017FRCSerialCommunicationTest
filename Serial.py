import serial

ser = serial.Serial()
ser.port = '/dev/ttyAMA0'

print ser

ser.open()
print 'The port is open: '+set.is_open

ser.write('Hello from Rpi! :)\n')

ser.close()
print 'The port is open: '+set.is_open