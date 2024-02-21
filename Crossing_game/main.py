import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player=Player()
carmanager= CarManager()
screen.listen()
screen.onkey(player.go_up, "Up")
scoreboard=Scoreboard()


game_is_on = True

while game_is_on:

    time.sleep(0.05)
    screen.update()
    carmanager.new_car()
    carmanager.move()

    #detect collision with car
    if carmanager.collision(player):
        scoreboard.gameover()
        game_is_on=False

    #reach finish line
    if player.ycor()>280:
        scoreboard.increaselvl()
        player.restart_position()
        carmanager.increase_speed()




screen.exitonclick()

