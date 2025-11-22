import turtle
import random
# screen setup
screen = turtle.Screen()
# pencolor("#ff0a0a")
screen.bgcolor("#070000")
screen.title("happy children's day")

pen = turtle.Turtle()
pen.speed(0)
pen.hideturtle()

def draw_text(message, pos, font_size=30, color="white"):
    pen.penup()
    pen.goto(pos)
    pen.color(color)
    pen.write(message, align="center", font=("Arial", font_size, "bold"))

def draw_card_border():
    border = turtle.Turtle()
    border.hideturtle()
    border.color("gold")
    border.pensize(10)
    border.penup()
    border.goto(-150, -200)
    border.pendown()
    for _ in range(2):
        border.forward(300)
        border.left(90)
        border.forward(400)
        border.left(90)

def draw_card():
    card = turtle.Turtle()
    card.hideturtle()
    card.penup()
    card.goto(-60, -50)
    card.pendown()
    card.color("deeppink", "lightyellow")
    card.begin_fill()
    for _ in range(2):
        card.forward(120)
        card.left(90)
        card.forward(60)
        card.left(90)
    card.end_fill()

    card.penup()
    card.goto(-60, 10)
    card.pendown()
    card.color("pink", "pink")
    card.begin_fill()
    for _ in range(2):
        card.forward(120)
        card.left(90)
        card.forward(120)
        card.left(90)
    card.end_fill()

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
    heart.end_fill()

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
draw_card_border()
draw_text("HAPPY", (0, 160), font_size=50, color="yellow")
draw_card()
draw_text("CHILDREN'S DAY", (0, 60), font_size=25, color="yellow")
draw_heart()
draw_balloons()
draw_sparkles()

turtle.done()

