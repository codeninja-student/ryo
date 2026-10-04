import tkinter as tk
root = tk.Tk()
root.title("Drawing pad")
controls = tk.Frame(root)
controls.grid(row=0, column=0, sticky="ew", padx=8, pady=8)
canvas = tk.Canvas(root, bg="white", width=760, height=480)
canvas.grid(row=1, column=0, sticky="nsew", padx=8, pady=8)
root.grid_rowconfigure(1, weight=1)
root.grid_columnconfigure(0, weight=1)
current_colour = "black"
pen_size = 50
last_x, last_y = None, None
def start_draw(event):
    global last_x ,last_y
    last_x, last_y = event.x, event.y
def draw(event):
    global last_x, last_y
    if last_x is not None and last_y is not None:
        canvas.create_line(last_x, last_y, event.x, event.y, fill=current_colour, width=pen_size, capstyle=tk.ROUND)
    last_x, last_y, = event.x, event.y
def end_draw(event):
    global lastX, last_y
    last_x, last_y = None, None
canvas.bind("<Button-1>", start_draw)
canvas.bind("<B1-Motion>", draw)
canvas.bind("<ButtonRelease-1>", end_draw)
def set_black():
    global current_colour
    current_colour = "Black"
def set_red():
    global current_colour
    current_colour = "red"
def set_blue():
    global current_colour
    current_colour = "Blue"
def set_green():
    global current_colour
    current_colour = "green"
def set_white():
    global current_colour
    current_colour = "white"
btn_black = tk.Button(controls, text="Black", command=set_black)
btn_black.grid(row=0, column=0, padx=2)
btn_red = tk.Button(controls, text="Red", command=set_red)
btn_red.grid(row=0, column=1, padx=2)
btn_blue = tk.Button(controls, text="Blue", command=set_blue)
btn_blue.grid(row=0, column=2, padx=2)
btn_green = tk.Button(controls, text="Green", command=set_green)
btn_green.grid(row=0, column=3, padx=2)
btn_white = tk.Button(controls, text="Eraser", command=set_white)
btn_white.grid(row=0, column=4, padx=2)
def change_size(value):
    global pen_size
    pen_size = int(value)
size_label = tk.Label(controls, text="Pen size")
size_label.grid(row=0, column=5, padx=6)
size_scale = tk.Scale(controls, from_=1, to=20, orient="horizontal", command=change_size)
size_scale.set(5)
size_scale.grid(row=0, column=6)
def clear_canvas():
    canvas.delete("all")
clear_btn = tk.Button(controls, text="Clear", command=clear_canvas)
clear_btn.grid(row=0, column=7, padx=6)

root.mainloop()