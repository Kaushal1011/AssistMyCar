
#!/usr/bin/env python3
import serial
import requests
import mmap
import os

filename = 'sensormapfile'
filename2 = 'safemapfile'

## create and initialize file with code like this
#fd = os.open(filename, os.O_CREAT | os.O_TRUNC | os.O_RDWR)
#os.write(fd, '\x00' * mmap.PAGESIZE)

fd = os.open(filename, os.O_RDWR)
buf = mmap.mmap(fd, 0, mmap.MAP_SHARED, mmap.PROT_WRITE)

fd2 = os.open(filename2, os.O_RDWR)
buf2 = mmap.mmap(fd2, 0, mmap.MAP_SHARED, mmap.PROT_WRITE)


if __name__ == '__main__':
    try:
        ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
        val_arr=[]
        numofsens=4
        while True:
            print(val_arr)
            if len(val_arr)==numofsens:
                buf.seek(0)
                ## use pickle to store complicated data
                buf.write(str(val_arr[0])+"\n") #front
                buf.write(str(val_arr[1])+"\n") #back
                buf.write(str(val_arr[2])+"\n") #left
                buf.write(str(val_arr[3])+"\n") #right

                buf2.seek(0)
                for i in val_arr:
                    if i<30:
                        buf2.write("0"+"\n")
                    else:
                        buf2.write("1"+"\n")


                # send to things speak
                PARAMS = {'api_key':'898XWPNP7UTY1AEB','field1':val_arr[0],'field2':val_arr[1],'field3':val_arr[2],'field4':val_arr[3]}
                r = requests.get(url = URL, params = PARAMS)
                data=r.json()
                print(data)
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
    except Exception as e:
        print(e)
        buf.seek(0)
        ## use pickle to store complicated data
        buf.write("1"+"\n") #front_safe
        buf.write("1"+"\n") #back_safe
        buf.write("1"+"\n") #left_safe
        buf.write("1"+"\n") #right_safe
        #buf.flush()
        raw_input('ENTER')
        buf.close()
        os.close(fd)
        buf2.close()
        os.close(fd2)
