rom tkinter import *

window = Tk()
window.title('Interest Calculator')
window.geometry('400x400')

# Title
Label(window, text='Interest Calculator', font=('Arial', 16)).pack()

# Inputs
Label(window, text='Principal').pack()
p_entry = Entry(window)
p_entry.pack()

Label(window, text='Time (years)').pack()
t_entry = Entry(window)
t_entry.pack()

Label(window, text='Rate (%)').pack()
r_entry = Entry(window)
r_entry.pack()

# Result label
result = Label(window, text='')
result.pack()

# Function
def calculate():
    p = float(p_entry.get())
    t = float(t_entry.get())
    r = float(r_entry.get())

    # Simple Interest
    si = (p * t * r) / 100

    # Compound Interest
    ci = p * (1 + r/100) ** t - p

    result.config(text=f"SI = {si:.2f}\nCI = {ci:.2f}")

# Button
Button(window, text='Calculate', command=calculate).pack()

window.mainloop()