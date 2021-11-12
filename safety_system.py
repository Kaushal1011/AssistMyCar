from globalstates import front_safe, back_safe, left_safe, right_safe
import RPi.GPIO as GPIO
import mmap
import os
import time
m11=18
m12=23
m21=24
m22=25
filename = 'safemapfile'
fd = os.open(filename, os.O_RDONLY)

buf = mmap.mmap(fd, 0, mmap.MAP_SHARED, mmap.PROT_READ)
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(m11, GPIO.OUT)
GPIO.setup(m12, GPIO.OUT)
GPIO.setup(m21, GPIO.OUT)
GPIO.setup(m22, GPIO.OUT)
i = 0



def main():
    while True:
        buf.seek(0)
        front_safe = int(buf.readline().decode())
        back_safe=int(buf.readline().decode())
        right_safe=int(buf.readline().decode())
        left_safe=int(buf.readline().decode())
        # print(front_safe)
        if front_safe==0:
            GPIO.output(m11 , 0)
            GPIO.output(m21 , 0)
            print("front not safe")
        if back_safe==0:
            GPIO.output(m12 , 0)
            GPIO.output(m22 , 0)
            print("back not safe")
        if right_safe==0:
            GPIO.output(m11 , 0)
            print("right not safe")
        if left_safe==0:
            GPIO.output(m21 , 0)
            print("left not safe")
try:
    main()
except Exception as e:
    print(e)
    buf.close()
    os.close(fd)
