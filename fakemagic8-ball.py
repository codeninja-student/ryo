import tkinter as tk
import random
root=tk.Tk()
root.title("Magic 8-ball")
root.geometry("400x300")
title_label = tk.Label(root, text="Magic 8-ball", font=("Arial",20))
title_label.pack(pady=10)
question_label = tk.Label(root, text="Ask a yes/no question:")
question_label.pack(pady=5)
aaah = tk.Entry(root, width=30, justify="center")
aaah.pack(pady=5)
poo = tk.Label(root, text="",font=("Arial", 16))
poo.pack(pady=20)
answers = [
    "Yes",
    "No",
    "Maybe...",
    "Ask LATER",
    "Definitely",
    "I dont think so",
    "Try again",
    "Absolutely",
    "I will eat you",
    "I will kill you",
    "tuff"
]
def give_answer():
    question = aaah.get().strip
    if question =="":
        poo.config(text="Please type a question")
        return
    reply = random.choice(answers)
    poo.config(text=reply)
ask_btn = tk.Button(root, text="Ask", width=12)
ask_btn.pack(pady=5)
def ask_pressed():
    give_answer()
ask_btn.config(command=ask_pressed)
def clear_all():
    aaah.delete(0,tk.END)
    poo.config(text="")
clear_btn = tk.Button(root, text="Clear", width=12, command=clear_all)
clear_btn.pack(pady=5)
root.mainloop()