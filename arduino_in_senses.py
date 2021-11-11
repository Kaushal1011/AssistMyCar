
#!/usr/bin/env python3
import serial
import requests

if __name__ == '__main__':
    ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
    val_arr=[]
    numofsens=2
    while True:
        print(val_arr)
        if len(val_arr)==numofsens:
            # send to things speak
            #flush array
            val_arr=[]
        resp = ser.read()
        char=resp.decode('utf-8')
        if char==',':
            int_arr=[]
            resp = ser.read()
            char=resp.decode('utf-8')
            int_arr.append(char)
            while char!=',':
                resp = ser.read()
                char=resp.decode('utf-8')
                if char==',':
                    break
                int_arr.append(char)
            val_arr.append(''.join(int_arr))
