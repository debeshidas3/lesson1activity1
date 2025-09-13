import turtle

# Setup screen
screen = turtle.Screen()
screen.bgcolor("black")   # background color

# Create turtle
pen = turtle.Turtle()
pen.color("red")
pen.pensize(3)

# Draw square
for i in range(4):
    pen.forward(100)   # move forward
    pen.right(90)      # turn right

# Hide turtle
pen.hideturtle()

# Keep the window open
screen.mainloop()
