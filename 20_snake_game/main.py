from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time
def run():

    screen = Screen()
    screen.setup(width=600,height=600)
    screen.bgcolor("black")
    screen.title("Snake Game")
    screen.tracer(0)
    snake = Snake()
    food= Food()
    score=Scoreboard()

    screen.listen()
    screen.onkey(snake.up,"Up")
    screen.onkey(snake.down,"Down")
    screen.onkey(snake.left,"Left")
    screen.onkey(snake.right,"Right")
    gameon=True
    while gameon:
        screen.update()
        time.sleep(0.1)
        snake.move()
        #DETECT COLLISION WITH FOOD
        if snake.segments[0].distance(food)<15:
            food.refresh()
            snake.extend()
            score.increase()

        #DETECT COLLISION WITH WALL
        if snake.segments[0].xcor()>280 or snake.segments[0].xcor()<-280 or snake.segments[0].ycor()<-280 or snake.segments[0].ycor()>280:
            print("Oh no, you hit a wall, you lose ")
            score.reset()
            snake.reset()


        #DETECT COLLISION WITH TAIL
        for tail in snake.segments[1:]:
            if snake.segments[0].distance(tail) <10:
                print("Oh no, you hit yout tail, you lose ")
                score.reset()
                snake.reset()

    screen.exitonclick()
run()