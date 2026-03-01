from turtle import *
import colorsys

# Setup turtle screen
speed(0)
bgcolor("black")
h = 0

# Draw colorful rotating flower pattern
for i in range(16):
    for j in range(18):
        c = colorsys.hsv_to_rgb(h, 1, 1)
        color(c)
        h += 0.005
        rt(90)
        circle(150 - j * 6, 90)
        lt(90)
        circle(150 - j * 6, 90)
        rt(180)
    circle(40, 24)

# Show message after drawing the flower
penup()
goto(0, -250)
color("white")
write("Happy Father's Day", align="center", font=("Arial", 28, "bold"))

goto(0, -290)
color("red")
write("Love you Papa", align="center", font=("Arial", 24, "bold"))

hideturtle()
done()