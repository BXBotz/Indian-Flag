import turtle

col = ("orange","white","green")

t = turtle.Turtle()

screen = turtle.Screen()
screen.bgcolor("black")

for i in range(300):
    t.color(col[i%3])
    t.forward(i*1)
    t.left(59)
    t.width(3)
