import turtle

screen = turtle.Screen()  # create a screen object
tr = turtle.Turtle()  # create a turtle object
screen.bgcolor("#90ee90")
tr.pensize(5)
tr.shape("turtle")
tr.stamp()


def turtle_circle():
    angle = 30
    tp = (0, 0)
    for _ in range(360 // angle):
        tr.penup()
        tr.forward(90)
        tr.pendown()
        tr.fd(10)
        tr.penup()
        tr.fd(20)
        tr.stamp()
        tr.setpos(tp)
        tr.left(angle)


turtle_circle()
screen.exitonclick()
