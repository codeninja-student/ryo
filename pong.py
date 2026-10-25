import tkinter as tk
import random
root = tk.Tk()
root.title('Pong')
W = 600
H = 400
canvas = tk.Canvas(root, width=W, height=H, bg='black')
canvas.pack()
for y in range(0, H, 20):
    canvas.create_rectangle(W//2 - 2, y, W//2 + 2, y + 10, fill='grey30', outline='')
PAD_W   = 12
PAD_H   = 70
PAD_OFF = 20
p1_y = H // 2
p1 = canvas.create_rectangle(
    PAD_OFF,            p1_y - PAD_H//2,
    PAD_OFF + PAD_W,    p1_y + PAD_H//2,
    fill='cyan', outline='')
p2_y = H // 2
p2 = canvas.create_rectangle(
    W - PAD_OFF - PAD_W, p2_y - PAD_H//2,
    W - PAD_OFF,         p1_y + H//2,
    fill='orange', outline='')
BALL_R = 8
ball_x = W // 2
ball_y = H // 2
ball_dx = random.choice([-4, 4])
ball_dy = random.choice([-3, 3])
ball = canvas.create_oval( ball_x - BALL_R, ball_y - BALL_R, 
                          ball_x + BALL_R, ball_y + BALL_R, 
                          fill='white', outline='')
score_p1 = 0
score_p2 = 0
WIN_SCORE = 5
score_test = canvas.create_text(
    W // 2, 24,
    text='0 : 0',
    font=('Arial', 22, 'bold'), fill='white') 
def update_score():
    canvas.itemconfig(score_test,
                      text=f'{score_p1}     :       {score_p2}')
P1_SPEED = 18
def p1_up(event):
    global p1_y
    p1_y -= P1_SPEED
    if p1_y < PAD_H // 2:
        p1_y = PAD_H // 2
    canvas.coords(p1,
        PAD_OFF,         p1_y - PAD_H // 2,
        PAD_OFF + PAD_W, p1_y + PAD_H // 2)
def p1_down(event):
    global p1_y
    p1_y += P1_SPEED
    if p1_y > H - PAD_H // 2:
        p1_y = H - PAD_H // 2
    canvas.coords(p1,
        PAD_OFF,         p1_y - PAD_H // 2,
        PAD_OFF + PAD_W, p1_y + PAD_H // 2)
root.bind('<w>', p1_up)
root.bind('<s>', p1_down)
root.mainloop()