import turtle
screen = turtle.Screen()
my_turtle = turtle.Turtle()
sides = 5
angle = 360 / sides
size = int(input("enter the size of the shape's side:"))
for _ in range(sides):
    my_turtle.forward(size)
    my_turtle.right(angle)
screen.mainloop()