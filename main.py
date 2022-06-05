
from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()
GAME_OVER = 6

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")
screen.onkeypress(r_paddle.go_up, "Up")
screen.onkeypress(r_paddle.go_down, "Down")
screen.onkeypress(l_paddle.go_up, "w")
screen.onkeypress(l_paddle.go_down, "s")
screen.onkeypress(l_paddle.go_up, "W")
screen.onkeypress(l_paddle.go_down, "S")
screen.onkey(l_paddle.go_up, "W")
screen.onkey(l_paddle.go_down, "S")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    #Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    #Detect collision with paddle


    if ball.distance(r_paddle) < 50 and ball.xcor() > 320:
        ball.bounce_x_r_paddle()
         

    if ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x_l_paddle()

    # Detect R paddle misses

    if ball.xcor() > 380:
        ball.reset_position_r()
        scoreboard.l_point()

    #Detect L paddle misses:

    if ball.xcor() < -380:
        ball.reset_position_l()
        scoreboard.r_point()

    if scoreboard.l_score == GAME_OVER:
        winner = "left player"
        scoreboard.end(winner)
        game_over = True
        # game_is_on = False

    elif scoreboard.r_score == GAME_OVER:
        winner = "right player"
        scoreboard.end(winner)
        game_over = True
        # game_is_on = False

screen.exitonclick()