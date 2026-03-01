import turtle
import random
import time

# --- Setup the Screen and Turtle ---
screen = turtle.Screen()
screen.setup(width=900, height=700)
screen.bgcolor("#1A0033")  # Deep purple background
screen.title("Happy Diwali - A Festival of Lights")
screen.tracer(0) # Turn off screen updates for smoother animation

t = turtle.Turtle()
t.speed(0)
t.hideturtle()

# --- Colors ---
GOLD = "#FFD700"
DIYA_CLAY = "#CC6600"
WICK_COLOR = "#6B4423"
FLAME_OUTER = "#FF6600" # Orange
FLAME_INNER = "#FFCC00" # Bright Yellow/Orange
FLAME_CORE = "#FFFF66"  # Light Yellow
SPARKLE_COLORS = ["#FFFFFF", "#FFD700", "#FFCC99"] # White, Gold, Light Gold

# --- Utility Functions ---

def move_to(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()

def draw_diya(x, y, scale=1.0):
    """Draws a Diya with a layered flame."""
    move_to(x, y)
    t.setheading(0)

    # Diya Bowl
    t.color(DIYA_CLAY)
    t.fillcolor(DIYA_CLAY)
    t.begin_fill()
    t.right(90)
    t.circle(70 * scale, 180)
    t.left(90)
    t.forward(120 * scale)
    t.end_fill()

    # Wick
    wick_width = 8 * scale
    wick_height = 12 * scale
    move_to(x - wick_width / 2, y + 5)
    t.setheading(90)
    t.color(WICK_COLOR)
    t.pensize(wick_width)
    t.forward(wick_height)
    t.pensize(1)

    # Flame (layered dots)
    flame_base_y = y + wick_height + 5 * scale
    move_to(x, flame_base_y + 15 * scale)
    t.dot(35 * scale, FLAME_OUTER)
    move_to(x, flame_base_y + 25 * scale)
    t.dot(25 * scale, FLAME_INNER)
    move_to(x, flame_base_y + 35 * scale)
    t.dot(15 * scale, FLAME_CORE)

def draw_sparkle(x, y, size=5, color="white"):
    """Draws a simple star-like sparkle."""
    move_to(x, y)
    t.color(color)
    t.setheading(random.randint(0, 359))
    t.pensize(1)
    
    # Randomly choose between a dot or small cross
    if random.random() < 0.7: # Mostly dots
        t.dot(size)
    else: # Occasionally small crosses
        for _ in range(2):
            t.forward(size)
            t.backward(size * 2)
            t.forward(size)
            t.left(90)

def generate_random_sparkles(count, area_x, area_y, area_width, area_height):
    """Generates random sparkles within a defined area."""
    for _ in range(count):
        sx = random.randint(area_x, area_x + area_width)
        sy = random.randint(area_y, area_y + area_height)
        ssize = random.randint(3, 7)
        scolor = random.choice(SPARKLE_COLORS)
        draw_sparkle(sx, sy, ssize, scolor)

def write_quote(quote_lines):
    """Writes a multi-line quote on the screen."""
    start_y = 180 # Starting Y position for the first line
    line_height = 40 # Space between lines
    
    t.color(GOLD)
    t.pensize(1) # Ensure pen is thin for text
    
    for i, line in enumerate(quote_lines):
        move_to(0, start_y - i * line_height)
        t.write(line, align="center", font=("Georgia", 28, "italic"))

# --- Main Drawing ---

# 1. Draw the Diya
draw_diya(0, -180, scale=1.3) # Slightly larger diya at the bottom

# 2. Add a glow behind the Diya for extra effect
move_to(0, -170)
t.dot(250, "#330066") # Darker purple glow
move_to(0, -170)
t.dot(200, "#5500AA") # Medium purple glow
move_to(0, -170)
t.dot(150, "#8800FF") # Lighter purple glow

# 3. Generate sparkles around the Diya and the top of the screen
generate_random_sparkles(70, -400, -300, 800, 600) # Entire screen area

# 4. The Diwali Quote
diwali_quote = [
    "May the millions of lamps of Diwali",
    "illuminate your life with joy,",
    "prosperity, health, and wealth.",
    "Happy Diwali!"
]
write_quote(diwali_quote)

# --- Finish ---
screen.update() # Update the screen to show all drawings
screen.mainloop()