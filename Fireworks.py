import tkinter as tk
import random
import math

WIDTH, HEIGHT = 700, 500

COLORS = [
    "#ff4d4d",
    "#ffd11a",
    "#33ccff",
    "#66ff66",
    "#ff66cc",
    "#ffffff"
]

root = tk.Tk()
root.title("Fireworks")

canvas = tk.Canvas(
    root,
    width=WIDTH,
    height=HEIGHT,
    bg="#0b0d17"
)
canvas.pack()

MAX_PARTICLES=10e9
particles = []

GRAVITY = 0.25


def spawn_firework(event):
    if len(particles) + 35 > MAX_PARTICLES:
        return

    color = random.choice(COLORS)

    for _ in range(35):
        angle = random.uniform(0, 2 * math.pi)
        speed = random.uniform(2, 7)

        vx = math.cos(angle) * speed
        vy = math.sin(angle) * speed - 2

        dot = canvas.create_oval(
            event.x - 3, event.y - 3,
            event.x + 3, event.y + 3,
            fill=color,
            outline=""
        )

        particles.append({
            "id": dot,
            "vx": vx,
            "vy": vy,
            "life": random.randint(25, 45)
        })


def update():
    alive = []

    for p in particles:
        p["vy"] += GRAVITY

        canvas.move(
            p["id"],
            p["vx"],
            p["vy"]
        )

        p["life"] -= 1

        if p["life"] > 0:
            alive.append(p)
        else:
            canvas.delete(p["id"])

    particles[:] = alive

    root.after(33, update)


canvas.bind("<Button-1>", spawn_firework)

update()

root.mainloop()