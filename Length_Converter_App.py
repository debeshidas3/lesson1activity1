from tkinter import *

window = Tk()
window.title("Python")
window.geometry("400x400")

def check():
    p = e.get()
    if len(p) <= 5:
        l.config(text="Weak", fg="red")
        
        elif len(p) <= 8:
            l.config(text="Medium", fg="yellow")
            
        elif len(p) <= 12:
            l.config(text="Strong", fg="light green")
            
        else:
            l.config(text="Very Strong", fg="dark green")
        
Label(w, text="Password Checker").pack()

e = Entry(w, show="*")
e.pack()
        
Button(w, text="Check", command=check).pack()

l = Label(w, text="")
l.pack()

window.mainloop()
