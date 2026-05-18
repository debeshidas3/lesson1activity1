from tkinter import *
import random

window = Tk()
window.title("RPS Game")
window.geometry("250x250")

label = Label(window, text="Pick One")
label.pack()

def game(user):
    items = ["Rock", "Paper", "Scissor"]
    computer = random.choice(items)

    if user == computer:
        result = "Tie"
    else:
        result = "Done!"

    label.config(text=user + "\n" + computer + "\n" + result)

Button(window, text="Rock", command=lambda: game("Rock")).pack()
Button(window, text="Paper", command=lambda: game("Paper")).pack()
Button(window, text="Scissor", command=lambda: game("Scissor")).pack()

window.mainloop()