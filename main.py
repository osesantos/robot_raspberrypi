from fastapi import FastAPI
from fastapi import Form
from fastapi.staticfiles import StaticFiles

from fastapi.responses import HTMLResponse

import robot

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

def get_page():
    return"""
<!DOCTYPE html>
<html>
<head>
    <title>Robot Control</title>
</head>
<body>
    <h1>Robot Control</h1>
    <p>Use the buttons below to control the robot:</p>
    <br>
    <form action="/init" method="post">
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
    </form>
    <br>
    <form action="/speed" method="post">
        <button type="submit" name="sp" value="l">Low</button>
        <button type="submit" name="sp" value="m">Medium</button>
        <button type="submit" name="sp" value="h">High</button>
    </form>
    <br>
    <form action="/exit" method="post">
        <button type="submit">Exit</button>
    </form>
</body>
</html
    """


# returns the page with the up, down, right, and left buttons to control the robot
@app.get("/")
async def root():
    return HTMLResponse(content=get_page(), status_code=200)


# moves the robot in the direction specified by the button pressed
@app.post("/move")
async def move(direction: str = Form(...)):
    if direction == 'f':
        print("forward")
        robot.move("f")
    elif direction == 'l':
        print("left")
        robot.move("l")
    elif direction == 'r':
        print("right")
        robot.move("r")
    elif direction == 'b':
        print("backward")
        robot.move("b")
    elif direction == 's':
        print("stop")
        robot.move("s")

    return HTMLResponse(content=get_page(), status_code=200)


# initializes the robot
@app.post("/init")
async def init():
    print("initializing")

    return HTMLResponse(content=get_page(), status_code=200)


# stops the robot
@app.post("/stop")
async def stop():
    print("stopping")
    robot.move("s")

    return HTMLResponse(content=get_page(), status_code=200)


# exits the program
@app.post("/exit")
async def q():
    print("exiting")
    robot.move("s")
    robot.e()

    return HTMLResponse(content=get_page(), status_code=200)


# changes the speed of the robot
@app.post("/speed")
async def speed(sp: str = Form(...)):
    if sp == 'l':
        print("low")
        robot.speed("l")
    elif sp == 'm':
        print("medium")
        robot.speed("m")
    elif sp == 'h':
        print("high")
        robot.speed("h")

    return HTMLResponse(content=get_page(), status_code=200)
