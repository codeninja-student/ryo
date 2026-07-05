import turtle
screen = turtle.Screen()
my_turtle = turtle.Turtle()
size = int(input("enter the size of the shape:"))
for _ in range(4):
    my_turtle.forward(size)
    my_turtle.right(90)
size = int(input("enter the size of the triangle's side:"))
for _ in range(3):
    my_turtle.forward(size)
    my_turtle.right(120)
screen.mainloop()
