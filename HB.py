import time
import time
import turtle

for i in range(10):
    time.sleep(1)
    print("\U0001F49A " + "Анатолий, с днем рождения!!!" + " \U0001F49A")

    if i == 9:
        break




turtle.bgcolor("black")
turtle.pensize(3)

def curve():
    for i in range(200):
        turtle.right(1)
        turtle.forward(1)

turtle.speed(0)
turtle.color("red", "red")

turtle.begin_fill()
turtle.left(140)
turtle.forward(111)
curve()

turtle.left(120)
curve()
turtle.forward(111)
turtle.end_fill()
turtle.hideturtle()
time.sleep(5)
