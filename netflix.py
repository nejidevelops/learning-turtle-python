import turtle

t = turtle.Turtle()
t.speed(5)
turtle.bgcolor("black")
turtle.title('Netflix Logo In Python')

t.color("#b1060f")
t.fillcolor("#b1060f")
t.begin_fill()
t.forward(30)
t.setheading(90)
t.forward(180)
t.setheading(180)
t.forward(30)
t.setheading(270)
t.forward(180)
t.end_fill()
t.setheading(0)
t.up()
t.forward(75)
t.down()

t.color("#b1060f")
t.fillcolor("#b1060f")
t.begin_fill()
t.forward(30)
t.setheading(90)
t.forward(180)
t.setheading(180)
t.forward(30)
t.setheading(270)
t.forward(180)
t.end_fill()

t.color("#e50914")
t.fillcolor("#e50914")
t.begin_fill()
t.setheading(112)
t.forward(194)
t.setheading(0)
t.forward(30)
t.setheading(292)
t.forward(195)
t.end_fill()
t.hideturtle()


turtle.done()
