import time
from turtle import Screen
from court import Wall
from paddle import Paddle
from ball import Ball
from score import Score
#########################
screen = Screen()
screen.bgcolor("black")
screen.setup(width=900, height=800)
screen.tracer(0)
screen.listen()
the_wall = Wall()
the_wall.center_line()
left_player = Paddle(-350)
right_player = Paddle(350)
ball = Ball()
right_player_score = Score(50, 350)
left_player_score = Score(-50, 350)
#########################
screen.onkey(left_player.move_up, "w")
screen.onkey(left_player.move_down, "s")
screen.onkey(right_player.move_up, "Up")
screen.onkey(right_player.move_down, "Down")
speed = .1
end_game = False
while not end_game:
    time.sleep(speed)
    screen.update()
    ball.move()
    ball.collision_wall()
    right_player_score.the_score()
    left_player_score.the_score()
    #_______________ collision with paddles ___________
    if ball.xcor() >= 330 and right_player.distance(ball) <= 52:
        new_direction = 540 - ball.heading() + right_player.distance(ball)
        ball.setheading(new_direction)
        speed *= .9
    elif ball.xcor() <= -330 and left_player.distance(ball) <= 52:
        new_direction = (180 - ball.heading()) + left_player.distance(ball)
        ball.setheading(new_direction)
        speed *= .9
    #----------------------------------------------
    if left_player_score.score == 5 or right_player_score.score == 5:
        end_game = True
    #-------------------went out--------------------
    if ball.xcor() > 380:
        ball.goto(0, 0)
        ball.setheading(135)
        left_player_score.score += 1
        speed = .1
    elif ball.xcor() < -380:
        ball.goto(0, 0)
        ball.setheading(45)
        right_player_score.score += 1
        speed = .1

the_wall.game_over()
screen.exitonclick()
