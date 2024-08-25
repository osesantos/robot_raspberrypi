from fastapi import FastAPI
from fastapi.responses import HTMLResponse

import robot

app = FastAPI()

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
    robot.e()

    return {"status": "stopped"}

# changes the speed of the robot
@app.post("/speed")
async def speed(sp: str):
    if sp == 'l':
        print("low")
        robot.speed("l")
    elif sp == 'm':
        print("medium")
        robot.speed("m")
    elif sp == 'h':
        print("high")
        robot.speed("h")

    return {"speed": sp}


