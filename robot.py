import RPi.GPIO as GPIO
from time import sleep

r_in1 = 24
r_in2 = 23
r_en = 25

l_in1 = 20
l_in2 = 16
l_en = 21

temp1 = 1

GPIO.setmode(GPIO.BCM)

GPIO.setup(r_in1, GPIO.OUT)
GPIO.setup(r_in2, GPIO.OUT)
GPIO.setup(r_en, GPIO.OUT)
GPIO.output(r_in1, GPIO.LOW)
GPIO.output(r_in2, GPIO.LOW)
l_p = GPIO.PWM(r_en, 1000)
l_p.start(25)

GPIO.setup(l_in1, GPIO.OUT)
GPIO.setup(l_in2, GPIO.OUT)
GPIO.setup(l_en, GPIO.OUT)
GPIO.output(l_in1, GPIO.LOW)
GPIO.output(l_in2, GPIO.LOW)
r_p = GPIO.PWM(l_en, 1000)
r_p.start(21)

print("\n")
print("The default speed & direction of motor is LOW & Forward.....")
print("r-run s-stop f-forward b-backward l-left r-right | l-low m-medium h-high e-exit")
print("\n")

while (1):

    x = input()

    # if x=='r':
    #     print("run")
    #     if(temp1==1):
    #      GPIO.output(l_in1,GPIO.HIGH)
    #      GPIO.output(l_in2,GPIO.LOW)
    #      GPIO.output(r_in1,GPIO.HIGH)
    #      GPIO.output(r_in2,GPIO.LOW)
    #      print("forward")
    #      x='z'
    #     else:
    #      GPIO.output(l_in1,GPIO.LOW)
    #      GPIO.output(l_n2,GPIO.HIGH)
    #      GPIO.output(r_in1,GPIO.LOW)
    #      GPIO.output(r_in2,GPIO.HIGH)
    #      print("backward")
    #      x='z'

    if x == 'l':
        print("left")
        GPIO.output(l_in1, GPIO.LOW)
        GPIO.output(l_in2, GPIO.LOW)
        GPIO.output(r_in1, GPIO.HIGH)
        GPIO.output(r_in2, GPIO.LOW)
        x = 'z'

    elif x == 'r':
        print("right")
        GPIO.output(l_in1, GPIO.HIGH)
        GPIO.output(l_in2, GPIO.LOW)
        GPIO.output(r_in1, GPIO.LOW)
        GPIO.output(r_in2, GPIO.LOW)
        x = 'z'

    elif x == 's':
        print("stop")
        GPIO.output(l_in1, GPIO.LOW)
        GPIO.output(l_in2, GPIO.LOW)
        GPIO.output(r_in1, GPIO.LOW)
        GPIO.output(r_in2, GPIO.LOW)
        x = 'z'

    elif x == 'f':
        print("forward")
        GPIO.output(l_in1, GPIO.HIGH)
        GPIO.output(l_in2, GPIO.LOW)
        GPIO.output(r_in1, GPIO.HIGH)
        GPIO.output(r_in2, GPIO.LOW)
        temp1 = 1
        x = 'z'

    elif x == 'b':
        print("backward")
        GPIO.output(l_in1, GPIO.LOW)
        GPIO.output(l_in2, GPIO.HIGH)
        GPIO.output(r_in1, GPIO.LOW)
        GPIO.output(r_in2, GPIO.HIGH)
        temp1 = 0
        x = 'z'

    elif x == 'l':
        print("low")
        r_p.ChangeDutyCycle(25)
        l_p.ChangeDutyCycle(25)
        x = 'z'

    elif x == 'm':
        print("medium")
        r_p.ChangeDutyCycle(50)
        l_p.ChangeDutyCycle(50)
        x = 'z'

    elif x == 'h':
        print("high")
        r_p.ChangeDutyCycle(75)
        l_p.ChangeDutyCycle(75)
        x = 'z'


    elif x == 'e':
        GPIO.cleanup()
        break

    else:
        print("<<<  wrong data  >>>")
        print("please enter the defined data to continue.....")
