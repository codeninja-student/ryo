import turtle
import time
import random
delay=0.2
body = []
win = turtle.Screen()
win.setup(width=500,height=500)
win.bgcolor("grey")
win.tracer(0)
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0,0)
head = turtle.Turtle()
head.shape("square")
head.color("yellow")
head.penup()
head.goto(0,100)
head.direction = "down"
score = 0
high_score = 0
pen = turtle.Turtle()
pen.penup()
pen.hideturtle()
pen.goto(0,200)
pen.clear()
pen.write("Score: {} High score: {}".format(score, high_score),
align = "center", font=("Consolas", 20, "normal"))
def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)
    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)
    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)
    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)
def go_up():
    head.direction = "up"
def go_down():
    head.direction = "down"
def go_right():
    head.direction = "right"
def go_left():
    head.direction = "left"
win.listen()
win.onkey(go_up, "w")
win.onkey(go_down, "s")
win.onkey(go_right, "d")
win.onkey(go_left, "a")
while True:
    win.update()
    if head.distance(food) <15:
        x = random.randint(-200, 200)
        y = random.randint(-200, 200)
        food.goto(x, y)
        new_body = turtle.Turtle()
        new_body.speed(0)
        new_body.shape("square")
        new_body.color("Azure")
        new_body.penup()
        body.append(new_body)
        score = score + 10
        if score>high_score:
            high_score 
        pen.clear()
    if len(body)>0:
        for index in range(len(body)-1, 0, -1):
            x = body[index-1].xcor()
            y = body[index-1].ycor()
            body[index].goto(x,y)
        x = head.xcor()
        y = head.ycor()
        body[0].goto(x,y)
    if head.xcor() > 240 or head.xcor() <-240 or head.ycor() > 240 or head.ycor() < -240:
        time.sleep(1)
        head.goto(0,0)
        head.direction = "stop"
        for item in body:
            item.goto(1000, 1000)
        body = []
        score = 0
    for item in body[2:]:
        if item.distance(head) <15:
            time.sleep(1)
            head.goto (0,0)
            head.direction = "stop"
            for item in body:
                item.goto(1000,1000)
            body = []
            score = 0
    pen.write("Score: {}  High score: {} ".format(score, high_score),
    align = "center", font=("Consolas", 20, "normal"))
    move()
    time.sleep(delay)
