import RPi.GPIO as GPIO

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


def move(direction):
    if direction == "f":
        print("forward")
        GPIO.output(l_in1, GPIO.HIGH)
        GPIO.output(l_in2, GPIO.LOW)
        GPIO.output(r_in1, GPIO.HIGH)
        GPIO.output(r_in2, GPIO.LOW)
    elif direction == "b":
        print("backward")
        GPIO.output(l_in1, GPIO.LOW)
        GPIO.output(l_in2, GPIO.HIGH)
        GPIO.output(r_in1, GPIO.LOW)
        GPIO.output(r_in2, GPIO.HIGH)
    elif direction == "l":
        print("left")
        GPIO.output(l_in1, GPIO.LOW)
        GPIO.output(l_in2, GPIO.LOW)
        GPIO.output(r_in1, GPIO.HIGH)
        GPIO.output(r_in2, GPIO.LOW)
    elif direction == "r":
        print("right")
        GPIO.output(l_in1, GPIO.HIGH)
        GPIO.output(l_in2, GPIO.LOW)
        GPIO.output(r_in1, GPIO.LOW)
        GPIO.output(r_in2, GPIO.LOW)
    elif direction == "s":
        print("stop")
        GPIO.output(l_in1, GPIO.LOW)
        GPIO.output(l_in2, GPIO.LOW)
        GPIO.output(r_in1, GPIO.LOW)
        GPIO.output(r_in2, GPIO.LOW)

def speed(direction):
    if direction == "l":
        print("low")
        r_p.ChangeDutyCycle(25)
        l_p.ChangeDutyCycle(25)
    elif direction == "m":
        print("medium")
        r_p.ChangeDutyCycle(50)
        l_p.ChangeDutyCycle(50)
    elif direction == "h":
        print("high")
        r_p.ChangeDutyCycle(75)
        l_p.ChangeDutyCycle(75)

def e():
    GPIO.cleanup()

