from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:

    def __init__(self):
        self.all_cars = []
        self.carspeed=STARTING_MOVE_DISTANCE

    def move(self):
        for car in self.all_cars:
            car.backward(self.carspeed)


    def new_car(self):
        i= random.randint(1,6)
        if i==1:
            car = Turtle("square")
            car.shapesize(stretch_wid=1, stretch_len=2)
            car.penup()
            car.color(random.choice(COLORS))
            random_y = random.randint(-250, 250)
            car.goto(300, random_y)
            self.all_cars.append(car)

    def collision(self,player):
        for car in self.all_cars:
            if car.distance(player)<20 :
                return True
        return False

    def increase_speed(self):
        self.carspeed+=MOVE_INCREMENT
