import turtle
import random
# from turtle import *

# Screen setup
screen = turtle.Screen()
# pencolor("#ff0a0a")
screen.bgcolor("#070000") 
screen.title("I love my sister")

pen = turtle.Turtle()
pen.speed(0)
pen.hideturtle()

def draw_text(message, pos, font_size=30, color="white"):
    pen.penup()
    pen.goto(pos)
    pen.color(color)
    pen.write(message, align="center", font=("Arial", font_size, "bold"))
def draw_heart():
    heart = turtle.Turtle()
    heart.hideturtle()
    heart.color("red")
    heart.pensize(3)
    heart.penup()
    heart.goto(0, -140)
    heart.pendown()
    heart.begin_fill()
    heart.left(140)
    heart.forward(113)
    heart.circle(-57, 200)
    heart.left(120)
    heart.circle(-57, 200)
    heart.forwarheart.end_fill()

def draw_balloons():
    balloon = turtle.Turtle()
    balloon.speed(0)
    balloon.hideturtle()
    colors = ["red", "yellow", "cyan", "magenta", "orange"]

    positions = [(-140, 100), (140, 100), (-140, 0), (140, 0)]
    for i, pos in enumerate(positions):
        balloon.penup()
        balloon.goto(pos)
        balloon.color(colors[i % len(colors)])
        balloon.begin_fill()
        balloon.circle(20)
        balloon.end_fill()
        balloon.goto(pos[0], pos[1] - 20)
        balloon.pendown()
        balloon.color("white")
        balloon.right(90)
        balloon.forward(30)
        balloon.left(90)

def draw_sparkles():
    sparkle = turtle.Turtle()
    sparkle.hideturtle()
    sparkle.speed(0)
    colors = ["white", "yellow", "violet", "lightblue"]
    for _ in range(30):
        x = random.randint(-140, 140)
        y = random.randint(-180, 180)
        sparkle.penup()
        sparkle.goto(x, y)
        sparkle.dot(random.randint(2, 5), random.choice(colors))

# Draw everything
draw_heart()
draw_text("I love my", (0, 160), font_size=50, color="#fcbef4")
draw_text()
draw_text("sister", (0, 60), font_size=25, color="#ec8888")
draw_heart()
draw_balloons()
draw_sparkles()

turtle.done()