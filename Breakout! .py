import turtle

# 1. Create the screen
window = turtle.Screen()
window.bgcolor('black')
window.setup(width=800, height=600)
window.tracer(0)
window.title('Breakeout!')

# 2. Create the Paddle
paddle = turtle.Turtle()
paddle.shape('square')
paddle.color('cyan')
paddle.shapesize(stretch_wid=1, stretch_len=5)
paddle.penup()
paddle.goto(0, -250)

# 3. Paddle Movement Functions
def paddle_left():
    x = paddle.xcor()
    if x > -340: x -= 40
    paddle.setx(x)

def paddle_right():
    x = paddle.xcor()
    if x < 340: x += 40
    paddle.setx(x)

# 4. Keyboard Bindings
window.listen()
window.onkeypress(paddle_left, 'Left')
window.onkeypress(paddle_right, 'Right')

# Create the ball like the paddle
ball = turtle.Turtle()
ball.shape('circle')
ball.color('white')
ball.penup()
ball.dx = 2.75
ball.dy = 2.75

pen = turtle.Turtle()
pen.speed(0)
pen.color('white')
pen.penup()
pen.hideturtle()
pen.goto(0,0)

# Add this before the main loop
brick_colors = ['red','orange','yellow','green', 'blue', 'teal', 'purple']
bricks = [] # An empty list to hold our bricks

for row_number in range(5):

    # This is your original code, just indented
    # This loop runs 5 times to draw the 7 bricks
    # It handles the BRICKS in a single row.
    for i, color in enumerate(brick_colors):
        brick = turtle.Turtle()
        brick.speed(0)
        brick.shape('square')
        brick.color(color)
        brick.shapesize(stretch_wid=1, stretch_len=4)
        brick.penup()
        
        # Calculate the X position
        # This is the same as your code
        x = -320 + (i * 100) # Space them out

        # Calculate th Y position
        # This is the new, important part!
        # W start at y=200 and move down 25 pixels for eack new row
        y = 200 - (row_number * 70)

        brick.goto(x, y)
        bricks.append(brick) # Add the new brick to our list!

# Main game loop
while True:
    window.update()

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    if ball.ycor() > 290:
        ball.sety(290) # Prevents getting stuck
        ball.dy *= -1  # Reverse the y direction

    if ball.xcor() < -390 or ball.xcor() > 390:
        ball.dx *= -1
        
    # Paddle Bouncing
    if (-250 < ball.ycor() < -240) and \
        (paddle.xcor() - 50 < ball.xcor() < paddle.xcor() + 50):
        ball.sety(-240) # Prevents getting stuck
        ball.dy *= -1
    
    # Game Over
    if ball.ycor() < -290:
        ball.goto(0,0) # Resets the ball

    # Brick Collision
    for brick in bricks:
        if ball.distance(brick) < 40:
            ball.dy *= -1 # Bounce
            brick.goto(1000,1000) # Hide the brick
            bricks.remove(brick) # Remove from list

    if not bricks: # This checks if the list is empty
        # You could show a 'You Win!' message here
        pen.clear()
        pen.write(f'You win!', align='center', font=('Courier', 24, 'normal'))
        ball.goto(1000,1000)
        ball.dx = 0
        ball.dy = 0