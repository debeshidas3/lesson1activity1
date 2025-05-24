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
