import time
import turtle as t
import os
import keyboard

win = t.Screen() 
win.title("Ping-Pong Game")
win.bgcolor('black') 
win.setup(width=800,height=600) 
win.tracer(0) 

pen=t.Turtle()
pen.speed(0)
pen.color("red")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Player Left: 0    Player Right: 0", align="center")

ball = t.Turtle()
ball.speed(0)
ball.shape('circle')
ball.color('yellow')
ball.penup()
ball.goto(0,0)
ball_dx = 3 
ball_dy = 3

paddle_left_stretch_wid=5
paddle_left = t.Turtle()
paddle_left.speed(0)
paddle_left.shape('square')
paddle_left.shapesize(stretch_wid=paddle_left_stretch_wid,stretch_len=1)
paddle_left.color('red')
paddle_left.penup()
paddle_left.goto(-390,0)
paddle_left_dx = 1.5 
paddle_left_dy = 1.5
paddle_left_score=0

paddle_right_stretch_wid=5
paddle_right = t.Turtle()
paddle_right.speed(0)
paddle_right.shape('square')
paddle_right.shapesize(stretch_wid=paddle_right_stretch_wid,stretch_len=1)
paddle_right.color('blue')
paddle_right.penup()
paddle_right.goto(390,0)
paddle_right_dx = 1.5 
paddle_right_dy = 1.5
paddle_right_score=0

def paddle_left_up():
    y=paddle_left.ycor()
    y=y+20
    paddle_left.sety(y)

def paddle_left_down():
    y=paddle_left.ycor()
    y=y-20
    paddle_left.sety(y)  

def paddle_right_up():
    y=paddle_right.ycor()
    y=y+20
    paddle_right.sety(y)

def paddle_right_down():
    y=paddle_right.ycor()
    y=y-20
    paddle_right.sety(y)

win.listen()
win.onkeypress(paddle_left_up,"w")
win.onkeypress(paddle_left_down,"s")
win.onkeypress(paddle_right_up,"Up")
win.onkeypress(paddle_right_down,"Down")


while True:
    win.update()
    ball.setx(ball.xcor()+ball_dx)
    ball.sety(ball.ycor()+ball_dy)
    if paddle_left.ycor() > 250:
        paddle_left.sety(250)
    if paddle_left.ycor() < -250:
        paddle_left.sety(-250)
    
    if paddle_right.ycor() > 250:
        paddle_right.sety(250)
    if paddle_right.ycor() < -250:
        paddle_right.sety(-250)

    if ball.xcor()>=paddle_left.xcor()-1 and ball.xcor()<=paddle_left.xcor()+1 and ball.ycor()<=paddle_left.ycor()+40 and ball.ycor()>=paddle_left.ycor()-40:
        ball_dx=-1*ball_dx

    if ball.xcor()>=paddle_right.xcor()-1 and ball.xcor()<=paddle_right.xcor()+1 and ball.ycor()<=paddle_right.ycor()+40 and ball.ycor()>=paddle_right.ycor()-40:
        ball_dx=-1*ball_dx

    if ball.ycor()>290:
        ball.sety(289.5)
        ball_dy=-1*ball_dy
        print("roof touched")
    if ball.ycor()<-290:
        ball.sety(-289.5)
        ball_dy=-1*ball_dy

    if ball.xcor()>390:
        ball.goto(0,0)
        paddle_left_score+=1
        paddle_left_stretch_wid+=1
        paddle_left.shapesize(stretch_wid=paddle_left_stretch_wid,stretch_len=1)
        paddle_right_stretch_wid-=1
        if paddle_right_stretch_wid==0:
            pen.clear()
            pen.write("Player Left won", align="center")
            time.sleep(1)
            exit
        paddle_right.shapesize(stretch_wid=paddle_right_stretch_wid,stretch_len=1)
        pen.clear()
        pen.write("Player Left: {}    Player Right: {}".format(paddle_left_score,paddle_right_score), align="center")

    if ball.xcor()<-390:
        # negative, hitting left wall
        ball.goto(0,0)
        paddle_right_score+=1
        paddle_right_stretch_wid+=1
        paddle_right.shapesize(stretch_wid=paddle_right_stretch_wid,stretch_len=1)
        paddle_left_stretch_wid-=1
        if paddle_left_stretch_wid==0:
            pen.clear()
            pen.write("Player Right won", align="center")
            time.sleep(1)
            exit
        paddle_left.shapesize(stretch_wid=paddle_left_stretch_wid,stretch_len=1)
        pen.clear()
        pen.write("Player Left: {}    Player Right: {}".format(paddle_left_score,paddle_right_score), align="center")
    time.sleep(0.001)