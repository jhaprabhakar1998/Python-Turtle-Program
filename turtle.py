from operator import le
from turtle import *
import math
import time


def writeText(txt="Prabhakar Jha"):
    write(txt, font=(
        "Verdana", 12, "bold"))


def init(col="red"):
    color(col)
    begin_fill()
    pensize(3)
    penup()
    backward(200)


def degreeToRadian(degree):
    return ((math.pi * degree) / 180)


def curve(r=1):
    print("r  ", r)
    for i in range(200):
        right(1)
        forward(r)


def heart(heartColor="red", fontSize=113):
    pendown()
    fillcolor(heartColor)
    begin_fill()

    curveRangeVal = fontSize / 113

    left(140)
    forward(fontSize)
    curve(curveRangeVal)
    left(120)
    curve(curveRangeVal)
    forward(fontSize - 1)
    end_fill()
    left(50 + 90)  # 50 to make turtle vertical downwards and 90 to point towards right


def spaceBetweenChar(space=20):
    penup()
    forward(20)


def makeCharH(fontSize=60, col="red"):
    color(col)
    pendown()
    left(90)
    forward(fontSize)
    left(180)
    forward(fontSize / 2)
    left(90)
    forward(fontSize / 2)
    left(90)
    forward(fontSize / 2)
    left(180)
    forward(fontSize)
    left(90)


# angleWithBase represents that with the base line what will be the angle of char.
def makeCharA(fontSize=60, angleWithBase=45, col="green"):
    color(col)
    pendown()
    left(angleWithBase)
    forward(fontSize)
    right(2*angleWithBase)
    forward(fontSize)
    backward(fontSize / 2)
    right(180 - angleWithBase)
    forward(fontSize * math.cos(degreeToRadian(angleWithBase)))
    left(angleWithBase)
    forward(fontSize / 2)
    backward(fontSize / 2)
    left(180 - angleWithBase)
    forward(fontSize * math.cos(degreeToRadian(angleWithBase)))
    right(angleWithBase)
    forward(fontSize/2)
    left(angleWithBase)


def makeCharP(fontSize=60, col="blue"):
    color(col)
    pendown()
    left(90)
    forward(fontSize / 3)
    right(90)
    circle(fontSize / 3, 180)
    left(90)
    forward(fontSize)
    left(90)
    penup()
    forward(fontSize / 3)


def makeCharY(fontSize=60, angleWithBase=45, col="yellow"):
    color(col)
    pendown()
    left(90)
    forward(fontSize/2)
    right(90 - angleWithBase)
    forward(fontSize / (2 * math.sin(degreeToRadian(angleWithBase))))
    backward(fontSize / (2 * math.sin(degreeToRadian(angleWithBase))))
    left(180 - 2*angleWithBase)
    forward(fontSize / (2 * math.sin(degreeToRadian(angleWithBase))))
    backward(fontSize / (2 * math.sin(degreeToRadian(angleWithBase))))
    left(90 + angleWithBase)
    forward(fontSize / 2)
    left(90)
    penup()
    forward(fontSize / (2 * math.sin(degreeToRadian(angleWithBase))))


def makeCharO(fontSize=60, col="grey"):
    color(col)
    forward(fontSize/2)
    pendown()
    circle(fontSize / 2)
    penup()
    forward(fontSize / 2)


def makeCharL(fontSize=60, col="gold"):
    color(col)
    pendown()
    left(90)
    forward(fontSize)
    backward(fontSize)
    right(90)
    forward(fontSize / 2)


def makeCharI(fontSize=60, col="purple"):
    color(col)
    left(90)
    pendown()
    forward(fontSize)
    backward(fontSize)
    right(90)


init()

left(90)
penup()
right(90)
heart("red", 200)
update()
penup()
right(90)
forward(150)
left(90)


makeCharH()
spaceBetweenChar(20)
makeCharA(60, 75)
spaceBetweenChar(20)
makeCharP()
spaceBetweenChar(20)
makeCharP()
spaceBetweenChar(20)
makeCharY(60, 60)
spaceBetweenChar(20)

spaceBetweenChar(40)

makeCharH()
spaceBetweenChar(20)
makeCharO()
spaceBetweenChar(20)
makeCharL()
spaceBetweenChar(20)
makeCharI()

hideturtle()

left(90)
penup()
forward(200)

left(90)
forward(200)
right(180)
writeText("Made by love and with colors Prabhakar Jha. \n Happy Holi to you and your loved ones!!!!!")

time.sleep(10)
