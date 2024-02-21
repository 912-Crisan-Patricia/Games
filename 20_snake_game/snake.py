from turtle import Turtle,Screen

class Snake:
    def __init__(self):
        self.starting_positions = [(0,0),(-20,0),(-40,0)] # starting positions
        self.segments=[] #each square taken as a turtle
        self.createsnake()
        self.distance = 20 #distance set

    def createsnake(self):
        for i in range(3):
            segment = Turtle()
            segment.shape("square")
            segment.color("white")
            segment.penup()
            segment.goto(self.starting_positions[i])
            self.segments.append(segment)


    def extend(self):
        new_segment=Turtle()
        new_segment.shape("square")
        new_segment.color("white")
        new_segment.penup()
        new_x = self.segments[-1].xcor()
        new_y = self.segments[-1].ycor()
        new_segment.goto(new_x,new_y)
        self.segments.append(new_segment)



    def move(self):
        for seg_num in range(len(self.segments)-1 ,0,-1):
            new_x= self.segments[seg_num-1].xcor()
            new_y= self.segments[seg_num-1].ycor()
            self.segments[seg_num].goto(new_x,new_y)
        self.segments[0].forward(self.distance)

    def up(self):
        if self.segments[0].heading() != 270:
            self.segments[0].setheading(90)
            #self.move()

    def down(self):
        if self.segments[0].heading() != 90:
            self.segments[0].setheading(270)
            #self.move()

    def left(self):
        if self.segments[0].heading() != 0:
            self.segments[0].setheading(180)
            #self.move()

    def right(self):
        if self.segments[0].heading() != 180:
            self.segments[0].setheading(0)
            #self.move()

    def reset(self):
        for seg in self.segments:
            seg.goto(1000,1000)
        self.segments.clear()
        self.createsnake()




