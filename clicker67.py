import tkinter as  tk
root = tk.Tk()
root.title("Clicker V1")
title = tk.Label(root, text="Clicker", font=("Arial", 18))
title.grid(row=0, column=0, columnspan=2, pady=10)
score = tk.IntVar(value=0)
score_label = tk.Label(root, text="Score:0", font=("Arial", 14))
score_label.grid(row=1, column=0, columnspan=2, pady=5)
def add_click():
    score.set(score.get() + 1)
    score_label.config(text=f"Score: {score.get()}")
click_btn = tk.Button(root, text="+1", width=20, height=5,command=add_click)
click_btn.grid(row=2, column=0, pady=8, padx=5)
def reset():
    score.set(0)
    score_label.config(text="Score: 0")
reset_btn = tk.Button(root, text="Reset", width=12, command=reset)
reset_btn.grid(row=2, column=1, pady=8, padx=5)


for c in range(2):
    root.grid_columnconfigure(c, weight=1)
root.mainloop()