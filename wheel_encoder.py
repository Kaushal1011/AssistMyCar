import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
import time
GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BCM) # Use physical pin numbering
GPIO.setup(4, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
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
            proctime=newtime
            count+=1
            dist+=1.083
            speed=1.083/curtimeint
        prev=curr
        print(speed)
except KeyboardInterrupt:
    print(count)
    print(dist)
