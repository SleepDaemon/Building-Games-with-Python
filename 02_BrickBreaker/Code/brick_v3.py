# arr=[
#     [[1,2],[2,3]],
#     [[14,25],[26,37]],
# ]


# for i in range(len(arr)):
#     row=arr[i]
    
#     for j in range(len(row)):
#         x,y=row[j]
#         print(x,y)

import time
import turtle as t
import os
import keyboard
import sys
import numpy as np

win_width = 800
win_height = 600


half_height=win_height//2
gap_between_rows=20
width_brick=20
max_rows_possibble=half_height//(gap_between_rows+width_brick)

gap_between_columns=5
length_brick=100
max_column_possible=win_width//(gap_between_columns+length_brick)

nrows=int(input("Enter number of rows"))
if nrows > max_rows_possibble:
    print("Max Rows Exceeded")
    print(max_rows_possibble)
    sys.exit()

ncols=int(input("Enter number of columns"))
if ncols > max_column_possible:
    print("Max Columns Exceeded")
    print(max_column_possible)
    sys.exit()

win = t.Screen() # creating a window
win.title("Ping-Pong Game") # Giving name to the game.
win.bgcolor('black') # providing color to the HomeScreen
win.setup(width=win_width,height=win_height) # Size of the game panel 
win.tracer(0) # which speed up's the game.
roof=win_height//2-10
floor=-(win_height//2-10)
left_wall=-(win_width//2-10)
right_wall=win_width//2-10

ball = t.Turtle()
ball.speed(0)
ball.shape('circle')
ball.color('yellow')
ball.penup()
ball.goto(0,0)
ball_dx = 3 # Setting up the pixels for the ball movement.
ball_dy = 3

print("roof", roof)
print("half_height", half_height)
xs=np.linspace(left_wall+50, right_wall-50, ncols)
ys=np.linspace(roof, 0, nrows)
print("xs,ys", xs,ys)
list_cord=[]

for i in xs:
    row=[]
    for j in ys:
        row.append([i,j])
    list_cord.append(row)

print(list_cord)
# list_cord=[
#     [[-330,roof-10], [-225,roof-10], [-120,roof-10], [120,roof-10], [225,roof-10],[330,roof-10]],
#     [[-330,roof-50], [-225,roof-50], [-120,roof-50], [120,roof-50], [225,roof-50],[330,roof-50]],
#     [[-330,roof-90], [-225,roof-90], [-120,roof-90], [120,roof-90], [225,roof-90],[330,roof-90]],
# ]

for i in range(len(list_cord)):
    row=list_cord[i]
    
    for j in range(len(row)):
        x,y=row[j]
        brick = t.Turtle()
        brick.shape("square")
        brick.shapesize(stretch_wid=1, stretch_len=5)
        brick.color('green')
        brick.penup()
        brick.goto(x,y)

paddle_stretch_wid=1
paddle = t.Turtle()
paddle.speed(0)
paddle.shape('square')
paddle.shapesize(stretch_wid=paddle_stretch_wid,stretch_len=5)
paddle.color('red')
paddle.penup()
paddle.goto(0,floor)
paddle_dx = 7 # Setting up the pixels for the paddle movement.
paddle_score=0

def paddle_left():
    x=paddle.xcor()
    x=x-paddle_dx
    paddle.setx(x)
def paddle_right():
    x=paddle.xcor()
    x=x+paddle_dx
    paddle.setx(x)

win.listen()
win.onkeypress(paddle_left,"Left")
win.onkeypress(paddle_right,"Right")


while True:
    win.update()
    ball.setx(ball.xcor()+ball_dx)
    ball.sety(ball.ycor()+ball_dy)
    paddle_left_margin=paddle.xcor()-50
    paddle_right_margin=paddle.xcor()+50
    
    # print("x",paddle_left_margin,ball.xcor(),paddle_right_margin)
    # print("y",paddle.ycor(),ball.ycor(),paddle.ycor()+20)

    if ball.ycor()>paddle.ycor() and ball.ycor()<paddle.ycor()+20:

        if ball.xcor()>paddle_left_margin and ball.xcor()<paddle_left_margin+10:
            print("hit paddle left edge")
            ball.sety(ball.ycor()+5)
            ball_dy=-1*ball_dy
            ball_dx=-1*ball_dx

        elif ball.xcor()<paddle_right_margin and ball.xcor()>paddle_right_margin-10:
            print("hit paddle right edge")
            ball.sety(ball.ycor()+5)
            ball_dy=-1*ball_dy
            ball_dx=-1*ball_dx

        elif ball.xcor()>paddle_left_margin and ball.xcor()<paddle_right_margin:
            ball.sety(ball.ycor()+5)
            ball_dy=-1*ball_dy
            print("paddle hit")

    # print("brick", brick.xcor())
    # print("brick_1", brick_1.xcor())
    # print("brick_2", brick_2.xcor())

    brick_row_num=-1
    brick_col_num=-1

    for i in range(len(list_cord)):
        row=list_cord[i]
        for j in range(len(row)):
            x,y=row[j]

            if ball.xcor()>x-50 and ball.xcor()<x+50:
                if ball.ycor()>y-10 and ball.ycor()<y+10:
                    print("hit brick", i,j)
                    ball_dy=-1*ball_dy
                    ball.sety(ball.ycor()-5)
                    brick_row_num=i
                    brick_col_num=j
                    break
    
    if brick_row_num!=-1 and brick_col_num!=-1:
        x,y=list_cord[brick_row_num][brick_col_num]
        
        brick = t.Turtle()
        brick.shape("square")
        brick.shapesize(stretch_wid=1, stretch_len=5)
        # brick.color('black')
        # brick.setfillopacity(100)
        brick.penup()
        brick.goto(x,y)

        del list_cord[brick_row_num][brick_col_num]

    if ball.ycor()>roof:
        ball.sety(roof-0.5)
        ball_dy=-1*ball_dy
        print("roof touched")
    if ball.ycor()<floor:
        ball.goto(0,0)
        # ball.sety(floor+0.5)
        # ball_dy=-1*ball_dy
    if ball.xcor()>right_wall:
        ball.setx(right_wall-0.5)
        ball_dx=-1*ball_dx
    if ball.xcor()<left_wall:
        ball.setx(left_wall+0.5)
        ball_dx=-1*ball_dx

    time.sleep(0.001)