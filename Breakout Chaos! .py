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
paddle.shapesize(stretch_wid=1, stretch_len=6)
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
#ball = turtle.Turtle()
#ball.shape('circle')
#ball.color('white')
#ball.penup()
#ball.dx = 2.5
#ball.dy = -2.5

def make_ball(x = 0, y = 0, dx = 2.5, dy = -2.5, original = False):
    ball = turtle.Turtle()
    ball.shape('circle')
    ball.color('white')
    ball.penup()
    ball.goto(x, y)
    ball.shapesize(1, 1)
    ball.dx = dx
    ball.dy = dy
    ball.is_original = original
    return ball

ball = make_ball(0,0,2.5,-2.5, original = True)
balls = []
balls.append(ball)

pen = turtle.Turtle()
pen.speed(0)
pen.color('white')
pen.penup()
pen.hideturtle()
pen.goto(0,0)

# Add this before the main loop
brick_colors = ['red','orange','yellow','green', 'blue', 'teal', 'purple']
bricks = [] # An empty list to hold our bricks

for row_number in range(3):

    # This is your original code, just indented
    # This loop runs 3 times to draw the 7 bricks
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
        y = 260 - (row_number * 70)

        brick.goto(x, y)
        bricks.append(brick) # Add the new brick to our list!

def reset():
    # Remove the extra balls, if any
    global balls, ball
    
    for b in balls[:]:
        if not getattr(b, 'is_original', False):
            b.hideturtle()
            balls.remove(b)

    # Reset the original ball
    ball.goto(0,0)
    ball.dx = 2.5
    ball.dy = -2.5
    ball.is_original = True
    ball.shapesize(1, 1)


    # Reset paddle
    paddle.goto(0, -250)
    paddle.shapesize(stretch_wid=1, stretch_len=6)

    # Clear win message
    pen.clear()

    # Rebuild bricks
    for brick in bricks:
        brick.hideturtle()
    bricks.clear()

    for row_number in range(3):
        for i, color in enumerate(brick_colors):
            brick = turtle.Turtle()
            brick.speed(0)
            brick.shape('square')
            brick.color(color)
            brick.shapesize(stretch_wid=1, stretch_len=4)
            brick.penup()

            x = -320 + (i * 100)
            y = 260 - (row_number * 70)

            brick.goto(x, y)
            bricks.append(brick)

    # Re-enable movement of the ball
    window.onkeypress(paddle_left, 'Left')
    window.onkeypress(paddle_right, 'Right')

# Main game loop
while True:
    window.update()

    # Move all balls
    for b in balls[:]:

        # Move the ball
        b.setx(b.xcor() + b.dx)
        b.sety(b.ycor() + b.dy)

        if b.ycor() > 290:
            b.sety(290) # Prevents getting stuck
            b.dy *= -1  # Reverse the y direction

        if b.xcor() < -390 or b.xcor() > 390:
            b.dx *= -1
            
        # Paddle Bouncing
        if (-250 < b.ycor() < -240) and \
            (paddle.xcor() - 100 < b.xcor() < paddle.xcor() + 100):
            b.sety(-240) # Prevents getting stuck
            b.dy *= -1
        
        # Game Over
        if b.ycor() < -290:
            # reset the original ball
            if getattr(b, 'is_original', False):
                b.goto(0,0) # Resets the ball
            else:
                b.hideturtle()
                if b in balls:
                    balls.remove(b)


    # Brick Collision
    for brick in bricks[:]:
        for b in balls[:]:

            if b.distance(brick) < 40:

                brick_color = brick.color()[0]

                # If the brick is red, shrink the ball a little each time
                if brick_color == 'red':
                    current_wid = b.shapesize()[0]
                    current_len = b.shapesize()[1]
                    shrink_factor = 0.65  # shrink 35% each hit
                    b.shapesize(current_wid * shrink_factor,
                                current_len * shrink_factor)

                # If the brick is teal, grow the ball a little each time
                if brick_color == 'purple':
                    current_wid = b.shapesize()[0]
                    current_len = b.shapesize()[1]
                    grow_factor = 1.5  # grow 50% each hit
                    b.shapesize(current_wid * grow_factor,
                                current_len * grow_factor)
                    
                # If the brick is yellow, make the pad bigger
                if brick_color == 'yellow':
                    paddle.shapesize(stretch_wid=1, stretch_len=10)
                
                # If the brick is blue, make the pad smaller
                if brick_color == 'blue':
                    paddle.shapesize(stretch_wid=1, stretch_len=4)

                # If the brick is green, double the balls
                if brick_color == 'green':
                    newBalls = []
                    # clone each ball in balls[]
                    for current in balls:
                        clone = make_ball(current.xcor(), current.ycor(), -current.dx, current.dy, original = False)
                        newBalls.append(clone)

                    balls.extend(newBalls)

                # Bounce and remove brick
                b.dy *= -1
                brick.goto(1000, 1000)
                bricks.remove(brick)

                # Speed increase
                b.dx *= 1.0275
                b.dy *= 1.0275

    if not bricks: # This checks if the list is empty
        # You could show a 'You Win!' message here
        pen.clear()
        pen.write(f'You win, press r to restart.', align='center', font=('Courier', 24, 'normal'))
        window.onkeypress(reset,'r')
        for b in balls:
            b.goto(1000,1000)
            b.dx = 0
            b.dy = 0