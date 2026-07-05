import turtle
screen = turtle.Screen()
my_turtle = turtle.Turtle()
color = input("enter the color for the turtle:")
my_turtle.color(color)
distance = int(input("Enter how far to move:"))
my_turtle.forward(distance)
screen.mainloop()