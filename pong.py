import turtle
win = turtle.Screen()
win.title('Pong')
win.setup(height=600,width=800)
win.tracer(0)
win.bgcolor('blue')

score_a = 0
score_b = 0

pad_a = turtle.Turtle()
pad_a.speed(0)
pad_a.shape('square')
pad_a.shapesize(stretch_wid=5, stretch_len=1)
pad_a.color('white')
pad_a.penup()
pad_a.goto(-350,0)

pad_b = turtle.Turtle()
pad_b.speed(0)
pad_b.shape('square')
pad_b.shapesize(stretch_wid=5, stretch_len=1)
pad_b.color('white')
pad_b.penup()
pad_b.goto(350,0)


ball = turtle.Turtle()
ball.speed(0)
ball.shape('square')
ball.color('white')
ball.penup()
ball.goto(0,0)
ball.dx = 0.09
ball.dy = 0.09

pen = turtle.Turtle()
pen.speed(0)
pen.color('white')
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write(f'Player A: {score_a}  Player B: {score_b}', align='center', font=('Courier', 24, 'bold'))

def pad_a_up():
    y = pad_a.ycor()
    pad_a.sety(y+20)

def pad_a_down():
    y = pad_a.ycor()
    pad_a.sety(y-20)

def pad_b_up():
    y = pad_b.ycor()
    pad_b.sety(y+20)

def pad_b_down():
    y = pad_b.ycor()
    pad_b.sety(y-20)

win.listen()
win.onkeypress(pad_a_up,'w')
win.onkeypress(pad_a_down,'s')
win.onkeypress(pad_b_up,'Up')
win.onkeypress(pad_b_down,'Down')






while True:
    win.update()
    
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    if ball.ycor() > 280:
        ball.sety(280)
        ball.dy *= -1
    if ball.ycor() < -280:
        ball.sety(-280)
        ball.dy *= -1
    if ball.xcor() > 390:
        ball.goto(0,0)
        ball.dx *= -1
        score_a +=1
        pen.clear()
        pen.write(f'Player A: {score_a}  Player B: {score_b}', align='center', font=('Courier', 24, 'bold'))
    if ball.xcor() < -390:
        ball.goto(0,0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write(f'Player A: {score_a}  Player B: {score_b}', align='center', font=('Courier', 24, 'bold'))

    if ball.xcor() > 340 and ball.xcor() < 350 and ball.ycor() < (pad_b.ycor()+50) and ball.ycor() > (pad_b.ycor()-50):
        ball.setx(340)
        ball.dx *= -1
 
    if ball.xcor() < -340 and ball.xcor() > -350 and ball.ycor() < (pad_a.ycor()+50) and ball.ycor() > (pad_a.ycor()-50):
        ball.setx(-340)
        ball.dx *= -1

    

    
