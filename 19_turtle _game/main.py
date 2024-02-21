from turtle import Turtle,Screen
import random

colorlist=["red","yellow","green","orange","blue"]
allturltes=[]
def run():

    screen = Screen()
    screen.setup(width=500,height=400)
    bet = screen.textinput(title="Make your bet", prompt="which turle will win?")
    print(bet)
    for i in range(0,5):
        newturtle=Turtle(shape="turtle")
        newturtle.color(colorlist[i])
        newturtle.penup()
        newturtle.goto(x=-230,y=-150+i*75)
        allturltes.append(newturtle)

    if bet:
        isbet=True

    while isbet:
        for turtle in allturltes:
            random.randint(0,10)
            turtle.forward(random.randint(0,10))
            if turtle.xcor()>230:
                isbet=False
                if turtle.pencolor()==bet:
                    print(f"you win! the {turtle.pencolor()} turtle won")
                else:
                    print(f"you lose! the {turtle.pencolor()} turtle won")
                break



    screen.exitonclick()

run()