from fastapi import FastAPI
from fastapi.responses import HTMLResponse
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

app = FastAPI()

is_running = False

# returns the page with the up, down, right, and left buttons to control the robot
@app.get("/")
async def root():
    html = """
    <html>
        <head>
            <title>Robot Control</title>
        </head>
        <body>
            <h1>Robot Control</h1>
            <p>Use the buttons below to control the robot:</p>
            <br>
            <fom action="/init" method="post">
                <button type="submit">Initialize</button>
            </form>
            <form action="/stop" method="post">
                <button type="submit">Stop</button>
            </form>
            <br>
            <form action="/move" method="post">
                <button type="submit" name="direction" value="f">Forward</button>
                <br>
                <button type="submit" name="direction" value="l">Left</button>
                <button type="submit" name="direction" value="r">Right</button>
                <br>
                <button type="submit" name="direction" value="b">Backward</button>
                <br>
                <button type="submit" name="direction" value="s">Stop</button>
            </form>
            <form action="/speed" method="post">
                <button type="submit" name="speed" value="l">Low</button>
                <button type="submit" name="speed" value="m">Medium</button>
                <button type="submit" name="speed" value="h">High</button>
            </form>
        </body>
    </html>
    """

    return HTMLResponse(content=html, status_code=200)

# moves the robot in the direction specified by the button pressed
@app.post("/move")
async def move(direction: str):
    if direction == 'f':
        print("forward")
        GPIO.output(l_in1, GPIO.HIGH)
        GPIO.output(l_in2, GPIO.LOW)
        GPIO.output(r_in1, GPIO.HIGH)
        GPIO.output(r_in2, GPIO.LOW)
    elif direction == 'l':
        print("left")
        GPIO.output(l_in1, GPIO.LOW)
        GPIO.output(l_in2, GPIO.LOW)
        GPIO.output(r_in1, GPIO.HIGH)
        GPIO.output(r_in2, GPIO.LOW)
    elif direction == 'r':
        print("right")
        GPIO.output(l_in1, GPIO.HIGH)
        GPIO.output(l_in2, GPIO.LOW)
        GPIO.output(r_in1, GPIO.LOW)
        GPIO.output(r_in2, GPIO.LOW)
    elif direction == 'b':
        print("backward")
        GPIO.output(l_in1, GPIO.LOW)
        GPIO.output(l_in2, GPIO.HIGH)
        GPIO.output(r_in1, GPIO.LOW)
        GPIO.output(r_in2, GPIO.HIGH)
    elif direction == 's':
        print("stop")
        GPIO.output(l_in1, GPIO.LOW)
        GPIO.output(l_in2, GPIO.LOW)
        GPIO.output(r_in1, GPIO.LOW)
        GPIO.output(r_in2, GPIO.LOW)

    return {"direction": direction}

# initializes the robot
@app.post("/init")
async def init():
    print("initializing")

    return {"status": "initialized"}

# stops the robot
@app.post("/stop")
async def stop():
    print("stopping")
    GPIO.output(l_in1, GPIO.LOW)
    GPIO.output(l_in2, GPIO.LOW)
    GPIO.output(r_in1, GPIO.LOW)
    GPIO.output(r_in2, GPIO.LOW)
    GPIO.cleanup()

    return {"status": "stopped"}

# changes the speed of the robot
@app.post("/speed")
async def speed(sp: str):
    if sp == 'l':
        print("low")
        r_p.ChangeDutyCycle(25)
        l_p.ChangeDutyCycle(25)
    elif sp == 'm':
        print("medium")
        r_p.ChangeDutyCycle(50)
        l_p.ChangeDutyCycle(50)
    elif sp == 'h':
        print("high")
        r_p.ChangeDutyCycle(75)
        l_p.ChangeDutyCycle(75)

    return {"speed": sp}


