"""Turtle tutorial."""


from turtle import Turtle, colormode, done
colormode(255)
leo: Turtle = Turtle()
bob: Turtle = Turtle()


leo.color(255, 51, 156)
bob.color(90, 42, 42)

leo.begin_fill()

leo.speed(50)
bob.speed(150)


leo.penup()
leo.goto(-150, -50)
leo.pendown()

bob.penup()
bob.goto(-150, -50)
bob.pendown

side_length: int = 300
i: int = 0
while (i < 3):
    leo.forward(side_length)
    leo.left(120)
    i = i + 1

while (i < 100):
    bob.forward(side_length)
    bob.left(122)
    i = i + 1
    side_length = side_length * 0.97

leo.end_fill()

done()