import turtle

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("pink")
screen.title("Happy Teacher's Day")

pen = turtle.Turtle()
pen.color("red")
pen.fillcolor("red")
pen.begin_fill()

# Draw a heart
pen.left(50)
pen.forward(200)
pen.circle(100, 180)
pen.right(100)
pen.circle(100, 180)
pen.forward(200)
pen.end_fill()

# Write the main message
pen.up()
pen.setpos(-130, 20)
pen.color("black")
pen.write("Happy Teacher's Day", font=("Arial", 18, "bold"))

# Write the dedication
pen.setpos(-160, -30)
pen.color("blue")
pen.write("To my favorite coding teacher,", font=("Arial", 14, "italic"))

pen.setpos(-110, -60)
pen.color("purple")
pen.write("kavana Mam❤️", font=("Arial", 16, "bold"))

pen.hideturtle()
turtle.done()