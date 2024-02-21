from turtle import Screen,Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard



import time
def run():

    screen = Screen()
    screen.setup(width=800,height=600)
    screen.bgcolor("black")
    screen.title("Arcade game")
    screen.tracer(0)
    paddleright= Paddle(350)
    paddleleft= Paddle(-350)
    ball= Ball()
    scoreboard=Scoreboard()


    screen.listen()
    screen.onkey(paddleright.go_up,"Up")
    screen.onkey(paddleright.go_down,"Down")

    screen.onkey(paddleleft.go_up,"w")
    screen.onkey(paddleleft.go_down,"s")


    gameon=True
    while gameon:
        screen.update()
        time.sleep(ball.move_speed)
        ball.move()

        #detect collision with walls
        if ball.ycor()>280 or ball.ycor()<-280:
            #bounce
            ball.bounce_y()

        #detect collision with right paddle
        if ball.distance(paddleright)<50 and ball.xcor()>320 or \
                ball.distance(paddleleft)<50 and ball.xcor()<-320:
            ball.bounce_x()

        #detect right paddle miss
        if ball.xcor() >380:
            ball.reset_position()
            scoreboard.increase_l()

        #detect left paddle miss
        if ball.xcor()<-380 :
            ball.reset_position()
            scoreboard.increase_r()



    screen.exitonclick()

run()