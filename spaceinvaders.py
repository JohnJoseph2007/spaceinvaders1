import turtle as t
import random
import time

screen = t.Screen()
screen.setup(width=600, height=600)
screen.title("Space Invaders")
screen.bgcolor("black")

ship = t.Turtle()
ship.shape("square")
ship.color("white")
ship.speed(0)
ship.penup()
ship.goto(0,-200)
ship.setheading(90)

screen.tracer(0)

def left():
    xcoordinate = ship.xcor()
    ship.setx(xcoordinate-5)

def right():
    xcoordinate = ship.xcor()
    ship.setx(xcoordinate+5)

screen.listen()
screen.onkeypress(left, "Left")
screen.onkeypress(right, "Right")

# def spawnalien():
#     time.sleep(0.5)
#     alien = t.Turtle()
#     alien.shape("square")
#     alien.color("white")
#     alien.speed(0)
#     alien.penup()
#     randxpos = random.randint(10, 590)
#     alien.goto(0,650)
#     ypos = alien.ycor()
#     ynewpos = ypos + 20
#     alien.goto(0, ynewpos)

while True:
    screen.update()

    #spawnalien()