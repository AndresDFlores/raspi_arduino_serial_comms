import serial
import time


ser = serial.Serial('/dev/ttyACM0', 115200, timeout=1.0)
time.sleep(3)
ser.reset_input_buffer()
print('Serial OK')

ard2pi=True

if ard2pi:

    #  send data from arduino to raspnberry pi
    try:
        while True:
            time.sleep(0.01)
            if ser.in_waiting>0:
                line=ser.readline().decode('utf-8').rstrip()
                print(line)

    except KeyboardInterrupt:
        print("Close Serial Communication")
        ser.close()

else:
    
    #  send data from raspberry pi to arduino
    try:
        while True:
            time.sleep(1)
            print("Sending data from Raspberry Pi to Arduino")
            ser.write("Hello from Raspberry Pi\n".encode('utf-8'))

    except KeyboardInterrupt:
        print("Close Serial Communication")
        ser.close()