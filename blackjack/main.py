import random

def choose_random_card():
    mylist=[11,2,3,4,5,6,7,8,9,10,10,10,10]
    card= random.choice(mylist)
    return card

def lost(playercards):
    ok=True
    if sum(playercards)<=21:
        return False
    if sum(playercards)>21:
        for i in range(0,len(playercards)-1):
            if playercards[i]==11:
                playercards[i] = 1
    if sum(playercards)>21:
        True

def equal(a,b):
    if a==b:
        return True
    return False

def run():
    print("welcome to blackjack")
    playercards = []
    computercards = []
    want_to_draw=True
    while want_to_draw:
        consent= input("Want to draw card? y/n")
        if consent=="n":
            want_to_draw=False
        else:
            playercards.append(choose_random_card())
            computercards.append(choose_random_card())
            print("Your cards are:")
            print(playercards)
            print(sum(playercards))
            print("Computer cards are:")
            print(computercards)
            print(sum(computercards))
            if lost(playercards):
                print("You lost")
                return
            elif lost(computercards):
                print("You win")
                return


    if sum(playercards) > sum(computercards):
        while sum(computercards)+10 <21:
            computercards.append(choose_random_card())
        if lost(computercards):
            print("You win")
        else:
            if sum(playercards) > sum(computercards):
                print("you win")
            else:
                print("you lose")




run()