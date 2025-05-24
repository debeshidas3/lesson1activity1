import math
from turtle import *

# Parametric equations for the heart
def hearta(k):
    return 15 * math.sin(k) ** 3

def heartb(k):
    return 12 * math.cos(k) - 5 * math.cos(2 * k) - 2 * math.cos(3 * k) - math.cos(4 * k)

# Setup Turtle
speed(0)
bgcolor("black")
penup()

# Define rainbow colors
rainbow_colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]

# Draw the heart
for i in range(1000):  # Reduced for better rendering speed
    k = math.radians(i)  # Convert to radians
    x = hearta(k) * 20    y = heartb(k) * 20goto(x, y)
    pendown()
    pencolor(rainbow_colors[i % len(rainbow_colors)])
    dot(10)  # Small dot to give heart a smooth look
    penup()
goto(x,y)


