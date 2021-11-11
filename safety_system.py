from globalstates import front_safe, back_safe, left_safe, right_safe
import RPi.GPIO as GPIO

def main():
    while True:
        if !front_safe:
            GPIO.output(m11 , 0)
            GPIO.output(m21 , 0)
            print("front not safe")
        if !back_safe:
            GPIO.output(m12 , 0)
            GPIO.output(m22 , 0)
            print("back not safe")
        if !right_safe:
            GPIO.output(m11 , 0)
            print("right not safe")
        if !left_safe:
            GPIO.output(m21 , 0)
            print("left not safe")
