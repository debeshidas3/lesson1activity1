from tkinter import *

window = Tk()
window.title("Age Calculator App")
window.geometry("400x400")

# Label
label = Label(window, text="Enter your birth year:")
label.pack()

# Entry
entry = Entry(window)
entry.pack()

# Function
def calculate_age():
    birth_year = int(entry.get())
    age = 2026 - birth_year
    result_label.config(text="Your Age is: " + str(age))

# Button
button = Button(window, text="Calculate Age", command=calculate_age)
button.pack()

# Result Label
result_label = Label(window, text="")
result_label.pack()

window.mainloop()



