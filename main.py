import turtle

def draw_heart():
    turtle.begin_fill()
    turtle.color("red")
    
    # Drawing the heart shape
    turtle.left(50)
    turtle.forward(133)
    turtle.circle(50, 200)
    turtle.right(140)
    turtle.circle(50, 200)
    turtle.forward(133)

    turtle.end_fill()

def draw_message():
    # Move turtle to write the message
    turtle.penup()
    turtle.goto(-150, 200)
    turtle.pendown()
    turtle.color("white")
    turtle.write("Can you friendship me?", font=("Arial", 16, "bold"))
    
def ask_friendship():
    # Draw the heart and message
    draw_message()
    draw_heart()

    # Stay in the program until the user closes the window
    turtle.hideturtle()

# Set up the screen
turtle.setup(500, 500)
turtle.bgcolor("black")

# Call the function to draw the message and heart
ask_friendship()

# Keep the window open until the user closes it
turtle.done()
