import turtle

# Screen setup
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Happy Birthday Papa")

pen = turtle.Turtle()
pen.speed(0)
pen.hideturtle()

def draw_text(message, pos, font_size=30, color="white"):
    pen.penup()
    pen.goto(pos)
    pen.color(color)
    pen.write(message, align="center", font=("Arial", font_size, "bold"))

def draw_cake():
    cake = turtle.Turtle()
    cake.hideturtle()
    cake.penup()
    cake.goto(0, -50)
    cake.pendown()
    cake.color("red", "deeppink")
    cake.begin_fill()
    for _ in range(2):
        cake.forward(120)
        cake.left(90)
        cake.forward(60)
        cake.left(90)
    cake.end_fill()

    cake.penup()
    cake.goto(0, 10)
    cake.pendown()
    cake.color("pink")
    cake.begin_fill()
    for _ in range(2):
        cake.forward(120)
        cake.left(90)
        cake.forward(40)
        cake.left(90)
    cake.end_fill()

    cake.penup()
    cake.goto(60, 50)
    cake.dot(11, "red")

def draw_heart():
    heart = turtle.Turtle()
    heart.hideturtle()
    heart.color("red")
    heart.pensize(3)
    heart.penup()
    heart.goto(0, -180)
    heart.pendown()
    heart.begin_fill()
    heart.left(140)
    heart.forward(113)
    heart.circle(-57, 200)
    heart.left(120)
    heart.circle(-57, 200)
    heart.forward(113)
    heart.end_fill()

# Drawing the design
draw_text("PAPA", (0, 200), font_size=50, color="violet")
draw_cake()
draw_text("HAPPY BIRTHDAY", (0, 80), font_size=30, color="cyan")
draw_heart()

turtle.done()
