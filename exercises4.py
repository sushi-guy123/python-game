import turtle
t = turtle.Turtle()
window = turtle.Screen()
window.tracer(0)
window.setup(width=800, height=600)
window.bgcolor('black')
t.shape('turtle')
t.color('white')
t.penup()
t.goto(0,150)
t.pendown()

for i in range(3):
    t.circle(50)
    t.penup()
    t.forward(125)
    t.pendown()

while True:
    window.update()