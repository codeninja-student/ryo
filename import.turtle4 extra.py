import turtle
screen = turtle.Screen()
my_turtle = turtle.Turtle()
sides = int(input("enter how many sides:"))
size = int(input("enter the size of the shape"))
for _ in range(sides):
    my_turtle.forward(size)
    my_turtle.right(360/sides)
screen.mainloop()