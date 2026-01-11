import turtle

# Can you guess what each line does?
window = turtle.Screen()
window.title('Pong Game by Me!')
window.bgcolor('black')
window.setup(width=800, height=600)
window.tracer(0)

# Let's make the left paddle!
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape('square')
paddle_a.color('white')
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350,0)

# Let's make the right paddle!
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape('square')
paddle_b.color('white')
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350,0) # The X is positive!

scored = False

def paddle_a_up():
    y=paddle_a.ycor()
    y+=20
    paddle_a.sety(y)

# Tell the window to listen
window.listen()
#When "w" is pressed, call our function
window.onkeypress(paddle_a_up, "w")

def paddle_a_down():
    y=paddle_a.ycor()
    y-=20
    paddle_a.sety(y)

#When "s" is pressed, call our function
window.onkeypress(paddle_a_down, "s")

def paddle_b_up():
    y=paddle_b.ycor()
    y+=20
    paddle_b.sety(y)


#When "Up" is pressed, call our function
window.onkeypress(paddle_b_up, "Up")

def paddle_b_down():
    y=paddle_b.ycor()
    y-=20
    paddle_b.sety(y)

#When "Down" is pressed, call our function
window.onkeypress(paddle_b_down, "Down")

# Create the ball(like the paddle)
ball = turtle.Turtle()
ball.shape('circle')
ball.color('white')
ball.penup()
ball.dx = 2.5
ball.dy = 2.5

# Initialize score
score_a = 0
score_b = 0

#Set up the score display
pen = turtle.Turtle()
pen.speed(0)
pen.color('white')
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write('Player A: 0  Player B: 0', \
align='center', font=('Courier', 24, 'normal'))

game_over = False

# Main game loop
while not game_over:
    window.update()

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)


    if ball.ycor() > 290:
        ball.sety(290) # Prevents getting stuck
        ball.dy *= -1  # Reverse the y direction

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    if paddle_a.ycor() > 250:
        paddle_a.sety(250)

    if paddle_a.ycor() < -250:
        paddle_a.sety(-250)

    if paddle_b.ycor() > 250:
        paddle_b.sety(250)

    if paddle_b.ycor() < -250:
        paddle_b.sety(-250)

    # Inside the loop
    # Right paddle bounce
    if (ball.xcor() > 340 and ball.xcor() < 350) and \
    (paddle_b.ycor() - 50 < ball.ycor() < paddle_b.ycor() + 50):
        ball.dx *= -1

    # Left paddle bounce
    #\ is used to combine two lines of code so that it isn't too long
    if (ball.xcor() < -340 and ball.xcor() > -350) and \
        (paddle_a.ycor() - 50 < ball.ycor() < paddle_a.ycor() + 50):
        ball.dx *= -1
    
    # Inside the main loop
    # When ball goes off the screen (right side - Player A scores) 
    if ball.xcor() > 390:
        ball.goto(0,0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write(f"Player A: {score_a}  Player B: {score_b}", align='center', font=('Courier', 24, 'normal'))
        scored = True

    # When ball goes off the screen (left side - Player B scores) 
    if ball.xcor() < -390:
        ball.goto(0,0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write(f"Player A: {score_a}  Player B: {score_b}", align='center', font=('Courier', 24, 'normal'))
        scored = True
    
    if scored:
        ball.dx *= 1.075
        ball.dy *= 1.075
        scored = False

    if score_a > 9:
        window.tracer(0)
        window.clear()
        window.bgcolor('black')
        pen.color('white')
        pen.penup()
        pen.goto(0,0)
        pen.write(f"Player A Wins!", align='center', font=('Courier', 60, 'normal'))
        window.update()
        game_over=True
        window.exitonclick()

    if score_b > 9:
        window.tracer(0)
        window.clear()
        window.bgcolor('black')
        pen.color('white')
        pen.penup()
        pen.goto(0,0)
        pen.write(f"Player B Wins!", align='center', font=('Courier', 60, 'normal'))
        window.update()
        game_over=True
        window.exitonclick()