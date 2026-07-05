import turtle

screen = turtle.Screen()
my_turtle = turtle.Turtle()
for i in range(3):
    my_turtle.forward(50)
    my_turtle.right(45)
    my_turtle.forward(50)
    my_turtle.left(90)
    my_turtle.forward(50)
    my_turtle.right(45)
screen.mainloop()