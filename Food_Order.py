import tkinter as tk

from tkinter import messagebox

from PIL import Image, ImageTk

import urllib.request

window = tk.Tk()

window.title("Food Order App")

window.geometry("500x600")

# Online image

url = "https://cdn-icons-png.flaticon.com/512/3075/3075977.png"

urllib.request.urlretrieve(url, "food.png")

img = Image.open("food.png")

img = img.resize((120, 120))

photo = ImageTk.PhotoImage(img)

tk.Label(window, image=photo).pack(pady=10)

tk.Label(window, text="Restaurant Order App", font=("Arial", 20, "bold")).pack()

menu = {

"Burger": 50,

"Pizza": 100,

"Fries": 40,

"Drink": 30

}

entries = {}

for item, price in menu.items():
    tk.Label(window, text=item + " ₹" + str(price), font=("Arial", 14)).pack()
    box = tk.Entry(window)
    box.pack()
    entries[item] = box

def order():
    total = 0
    bill = "Your Order:\n\n"
    
    for item, box in entries.items():
        qty = box.get()
        if qty == "":
            qty = 0

        else:
            qty = int(qty)
        if qty > 0:
           cost = qty * menu[item]
           total = total + cost
           bill = bill + item + " x " + str(qty) + " = ₹" + str(cost) + "\n"

   bill = bill + "\nTotal = ₹" + str(total)

   if total == 0:
      messagebox.showerror("Error", "Please enter quantity")

   else:
       messagebox.showinfo("Bill", bill)

tk.Button(window, text="Place Order", font=("Arial", 14), command=order).pack(pady=20)

window.mainloop()