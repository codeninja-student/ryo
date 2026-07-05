import turtle
screen = turtle.Screen()
my_turtle = turtle.Turtle()
my_turtle.pensize(3)
my_turtle.color("blue")
for i in range(4):
    my_turtle.forward(100)
    my_turtle.right(90)
screen.mainloop()