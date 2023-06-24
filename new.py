from turtle import Screen, Turtle

SIDES = 6

COLORS = ("blue", "red", "green", "white", "yellow", "purple")

screen = Screen()
screen.bgcolor("black")

turtle = Turtle()

for x in range(360):
    turtle.pencolor(COLORS[(x % SIDES) % len(COLORS)])
    turtle.forward(x*3 / SIDES + x)
    turtle.left(360 / SIDES+1)
    turtle.width(x * SIDES/200)

screen.exitonclick()