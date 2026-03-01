import turtle

# Set up the screen
screen = turtle.Screen()
screen.title("Block the Ball Game")
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.tracer(0)  # Disable automatic screen updates

# Create the paddle
paddle = turtle.Turtle()
paddle.shape("square")
paddle.color("white")
paddle.shapesize(stretch_wid=1, stretch_len=6)
paddle.penup()
paddle.goto(0, -250)

# Create the ball
ball = turtle.Turtle()
ball.shape("circle")
ball.color("red")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.15
ball.dy = -0.15

# Paddle movement functions
def move_left():
    x = paddle.xcor()
    if x > -350:
        paddle.setx(x - 20)

def move_right():
    x = paddle.xcor()
    if x < 350:
        paddle.setx(x + 20)

# Keyboard bindings
screen.listen()
screen.onkeypress(move_left, "Left")
screen.onkeypress(move_right, "Right")

# Main game loop
while True:
    screen.update()

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Ball collision with walls
    if ball.xcor() > 390 or ball.xcor() < -390:
        ball.dx *= -1

    if ball.ycor() > 290:
        ball.dy *= -1

    # Ball falls below the screen
    if ball.ycor() < -290:
        ball.goto(0, 0)
        ball.dy *= -1

    # Ball hits the paddle
    if (ball.ycor() > -240 and ball.ycor() < -230) and (ball.xcor() > paddle.xcor() - 60 and ball.xcor() < paddle.xcor() + 60):
        ball.dy *= -1