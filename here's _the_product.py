from tkinter import *

window = Tk()

window.title('Getting Started with Widgets')
window.geometry('400x300')

label = Label(window, text="Label widget is used to display text or images on the screen. It is a simple widget that can be used to create headings, instructions, or any other static content.")

label = Label(window,text="")

label = Label(window,text="")

entry = Entry(window)# pink
entry = Entry(window)# blue

button = Button(window, text="Button widget is used to create clickable buttons in the GUI. It can be used to trigger actions or events when clicked by the user.")

textbox=Text(window, height=5, width=40)