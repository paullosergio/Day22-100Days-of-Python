from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Score


screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

l_paddle = Paddle((-350, 0))
r_paddle = Paddle((350, 0))
ball = Ball()
score_l = Score((-100, 200))
score_r = Score((100, 200))


screen.listen()
screen.onkey(fun=r_paddle.go_up,key= "Up")
screen.onkey(fun=r_paddle.go_down,key= "Down")
screen.onkey(fun=l_paddle.go_up,key= "w")
screen.onkey(fun=l_paddle.go_down,key= "s")


game_is_on = True
while game_is_on:
    screen.update()
    ball.move()
    time.sleep(ball.move_speed)

    # Detect collision with wall.
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    
    # Detect collision with paddle.
    if ball.distance(l_paddle) < 50 and ball.xcor() < -320 or ball.distance(r_paddle) < 50 and ball.xcor() > 320:
        ball.bounce_x()
    
    # Detect R paddle misses
    if ball.xcor() > 380:
        ball.reset_position()
        score_l.increase_score()

    # Detect L paddle misses
    if ball.xcor() < -380:
        ball.reset_position()
        score_r.increase_score()
        


screen.exitonclick()