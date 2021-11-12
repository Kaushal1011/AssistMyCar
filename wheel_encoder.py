import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
import time
import mmap
import os
GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BCM) # Use physical pin numbering
GPIO.setup(4, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
fd = os.open(filename, os.O_RDWR)
buf = mmap.mmap(fd, 0, mmap.MAP_SHARED, mmap.PROT_WRITE)
# Set pin 10 to be an input pin and set initial value to be pulled low (off)
print("start")
curr=0
prev=0
count=0
dist=0
speed=0
proctime=time.process_time()
curtimeint=1
try:
    while True: # Run forever
        curr=GPIO.input(4)
        if curr==1 and prev==0:
            newtime=time.process_time()
            curtimeint=newtime-proctime
            # save data and send it to things speeks
            count+=1
            dist+=1.083
            speed=1.083/curtimeint

            buf.seek(0)
            ## use pickle to store complicated data
            buf.write(str(dist)+"\n") #front
            buf.write(str(speed)+"\n") #back
            PARAMS = {'api_key':'898XWPNP7UTY1AEB','field1':dist,'field2':speed}
            r = requests.get(url = URL, params = PARAMS)
            data=r.json()
            print(data)

            time.sleep(1)
            proctime=time.process_time()

        prev=curr
except KeyboardInterrupt:
    print(count)
    print(dist)
