from turtle import *

screen = Screen()
screen.title("Write Your Name")
screen.bgcolor("turquoise")
screen.setup(width = 500, height = 500)

yertle = Turtle()
yertle.color("white")
yertle.shape("turtle")

# for j in range(4):
#     for i in range(5):
#         yertle.forward(10)
#         yertle.penup()
#         yertle.forward(10)
#         yertle.pendown()
#     yertle.left(90)

yertle.penup()
yertle.left(180)
yertle.forward(200)
yertle.left(90)
#D
yertle.forward(50)
yertle.left(180)
yertle.pendown()
yertle.forward(100)
yertle.left(270)
yertle.circle(-50, 180)
#E
yertle.penup()
yertle.right(180)
yertle.forward(55)
yertle.pendown()
yertle.forward(25)
yertle.left(180)
yertle.forward(25)
yertle.right(90)
yertle.forward(50)
yertle.right(90)
yertle.forward(15)
yertle.left(180)
yertle.forward(15)
yertle.right(90)
yertle.forward(50)
yertle.right(90)
yertle.forward(25)











screen.exitonclick()