import turtle
import colorsys

# Setup screen
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Happy Birthday Mamma")

# Setup turtle
pen = turtle.Turtle()
pen.speed(0)
pen.width(2)
pen.hideturtle()

# Draw colorful flower
hue = 0
for i in range(200):
    color = colorsys.hsv_to_rgb(hue, 1, 1)
    pen.color(color)
    pen.forward(i)
    pen.left(59)
    hue += 0.005

# Write birthday message
pen.penup()
pen.goto(0, -200)
pen.color("pink")
pen.write("🎉 Happy Birthday Mamma 🎉\nI Love You So Much 💖",
          align="center", font=("Arial", 20, "bold"))

# Keep the window open
turtle.done()
