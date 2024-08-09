import turtle
from _lsprof import profiler_entry

screen = turtle.Screen()
screen.bgcolor("blue")
screen.title("pong game ")
screen.setup(width=1000,height=600)
screen.tracer(0)

#create up paddle
right_pad = turtle.Turtle()
right_pad.speed(0)
right_pad.shape("square")
right_pad.shapesize(stretch_len=1,stretch_wid=5)
right_pad.color("white")
right_pad.penup()
right_pad.goto(480, 0)
#
#create UP paddle
left_pad = turtle.Turtle()
left_pad.shape("square")
left_pad.shapesize(stretch_len=1,stretch_wid=5)
left_pad.color("white")
left_pad.speed(0)
left_pad.penup()
left_pad.goto(-480,0)

#ball creation
ball = turtle.Turtle()
ball.shape("circle")
ball.color("red")
ball.speed(0)
ball.penup()
ball.goto(0,0)
ball.dx = 0.10
ball.dy = .10

def right_pad_up ():
    right_pad.sety(right_pad.ycor()+20)
def right_pad_down():
    right_pad.sety(right_pad.ycor()-20)
def left_pad_up():
    left_pad.sety(left_pad.ycor()+20)
def left_pad_down():
    left_pad.sety(left_pad.ycor()-20)
def quite():
    global game_over
    game_over = False
def reset():
    global player_1_score,player_2_score,ball
    player_1_score = 0
    player_2_score = 0
    ball.goto(0, 0)
    ball.dx = 0.10
    ball.dy = 0.10
    pen.clear()
    pen.goto(0,280)
    pen.write("Player 1: 0 - Player 2: 0", align="center", font=("Arial", 16, "normal"))
def check_play():
    play_again = screen.textinput("game_over","do you want to play again  yes/No")
    if play_again.lower() == "yes" :
        reset()
    else:
        global game_over
        game_over = True
screen.listen()
screen.onkey(right_pad_up, "8")
screen.onkey(right_pad_down, "5")
screen.onkey(left_pad_up, "w")
screen.onkey(left_pad_down, "s")
screen.onkey(quite, "q")
player_1_score = 0
player_2_score = 0
#score
pen = turtle.Turtle()
pen.speed(0)
pen.hideturtle()
pen.color("white")
pen.penup()
pen.goto(0,270)

pen.write("player 1 : 0 - player 2 : 0 ", align="center", font = ("ariel",16,"normal"))
game_over = True
while game_over:
    screen.update()
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)
    if ball.ycor() > 280:
        ball.dy *= -1
    if ball.ycor() < -280:
        ball.dy *= -1
    if ball.xcor() > 480:
        ball.dx *= -1
        player_1_score += 1
        pen.clear()
        pen.write("player 1 : {}  player 2 : {} ".format(player_1_score, player_2_score), align="center", font = ("ariel",16,"normal"))
        if player_1_score > 1:
            pen.write("Player 1 is win", align="center",font=("arial",16,"normal"))
            pen.goto(0,0)
            check_play()
    if ball.xcor() < -480:
        ball.dx *= -1
        player_2_score += 1
        pen.clear()
        pen.write("player 1 : {}  player 2 : {} ".format(player_1_score, player_2_score), align="center", font = ("ariel",16,"normal"))
        if player_2_score > 1:
            pen.write("Player 2 is win", align="center",font=("arial",16,"normal"))
            pen.goto(0, 0)
            check_play()
          #  game_over = False
    if ball.xcor() > 460 and ball.ycor() < right_pad.ycor()+50 and ball.ycor() > right_pad.ycor()-50:
        ball.dx *= -1
    if ball.xcor() < - 460 and ball.ycor() < left_pad.ycor()+ 50  and left_pad.ycor()-50 < ball.ycor():
        ball.dx *= -1



