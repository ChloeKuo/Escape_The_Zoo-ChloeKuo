import turtle
import os
import time
import random

wn = turtle.Screen()
bob = turtle.Turtle()
fred = turtle.Turtle()
write = turtle.Turtle()
one = turtle.Turtle()
two = turtle.Turtle()
three = turtle.Turtle()
present = turtle.Turtle()
#end = turtle.Turtle()

#def black():
    #end.pensize(40)

def hide():
    #end.hideturtle()
    one.hideturtle()
    two.hideturtle()
    fred.penup()
    bob.penup()
    three.hideturtle()
    present.hideturtle()
    present.penup()

def text(x, sec):
    write.penup()
    write.hideturtle()
    write.goto(0, 400)
    write.write(x, move=False, align="center", font=("Arial", 30, "normal"))
    time.sleep(sec)
    write.clear()

def cage(x, y):
    one.penup()
    one.goto(x, y)
    one.pendown()
    one.color("red")
    one.pensize(3)
    for x in range(4):
        one.fd(200)
        one.left(90)
    one.left(90)
    for x in range(10):
        one.fd(200)
        one.right(90)
        one.fd(10)
        one.right(90)
        one.fd(200)
        one.left(90)
        one.fd(10)
        one.left(90)
    one.right(90)

def pengs():
    wn.bgcolor("White")
    wn.addshape(os.path.expanduser("confet.gif"))
    three.shape(os.path.expanduser("confet.gif"))
    three.speed(100)
    three.penup()
    for x in range(20):
        three.goto(random.randrange(-700, 700), random.randrange(-700, 300))
        three.stamp()

def sky():
    two.color("cyan")
    two.speed(100)
    two.penup()
    two.goto(-1000, 800)
    two.pendown()
    two.begin_fill()
    for x in range(2):
        two.fd(2000)
        two.right(90)
        two.fd(500)
        two.right(90)
    two.end_fill()

def death():
    wn.addshape(os.path.expanduser("rip.gif"))
    bob.shape(os.path.expanduser("rip.gif"))

def question(word):
    write.penup()
    write.write(word, move=False, align="center", font=("Arial", 30, "normal"))

def answer(t, message, x, y):
    t.penup()
    t.goto(x,y)
    t.write(message, move=False, align="center", font=("Arial", 30, "normal"))

def clear():
    one.clear()
    two.clear()

#a choices

def a(): #choice1a
    write.clear()
    text("Now you have to figure out how to escape from your cage.", 2)
    text("You have no tools at your disposal other than yourself.", 2)
    question("What do you do?")

def aa(): #choice1aa
    write.clear()
    text("Yay! You successfully unlocked and escaped the cage!", 2)
    bob.goto(-200, 0)
    text("Now you are having second thoughts about taking Fred.", 2)
    text("Is it really worth it?", 1.5)
    text("He eats a lot, so he might deplete your food supply on the journey.", 2)
    text("Also, he's kind of obnoxious.", 1.75)
    question("What do you do?")

def aaa(): #choice1aaa
    write.clear()
    bob.goto(500, -20)
    text("Fred screams at you for being the bad friend that you are.", 2)
    text("The zookeeper, upon hearing Fred, puts you back into the cage.", 1.5)
    bob.goto(0, 0)
    text("Now the zookeeper always keeps close watch over you.", 1.5)
    text("You die of hopelessness.", 1)
    bob.goto(100, 20)
    death()
    question("GAME OVER")
    wn.exitonclick()

def aab(): #choice1aab
    write.clear()
    fred.hideturtle()
    one.clear()
    text("You have abandoned Fred.", 2)
    text("There is a store nearby. You are hungry, but it might be safer to just leave the zoo now.", 2)
    question("What do you do?")

def aaba(): #choice1aaba
    write.clear()
    wn.addshape(os.path.expanduser("store.gif"))
    fred.shape(os.path.expanduser("store.gif"))
    fred.goto(-300, 200)
    fred.showturtle()
    bob.goto(-240, 100)
    text("The human visitors see you.", 1.75)
    text("They freak out and attack you.", 1.75)
    text("You are now a dead penguin.", 1.75)
    bob.goto(0,0)
    death()
    question("GAME OVER.")
    wn.exitonclick()                                #dead end

def aabb():
    write.clear()
    text("Smart choice.", 1)
    text("Now you are out of the zoo.", 1.75)
    text("But you have no sense of direction without Google Maps.", 1.75)
    question("What is your next course of action?")

def aabaa():
    write.clear()
    wn.addshape(os.path.expanduser("god.gif"))
    fred.shape(os.path.expanduser("god.gif"))
    fred.goto(-300, 200)
    fred.showturtle()
    text("The almighty has arrived!!!!!", 1.5)
    text("You stand paralyzed by Its Greatness.", 1.75)
    text("After twenty minutes, you finally regain you ability to function.", 1.75)
    question("What do you do?")

def aabaaa():
    write.clear()
    text("The penguin god sees that you are worthy of Its help.", 1.75)
    text("He teleports you to the South Pole.", 1.75)
    pengs()
    text("Congratulations!!!!!", 1)
    question("You won the game!")

def aabaab():
    write.clear()
    text("You just insulted It.", 2)
    fred.left(100)
    text("It rises towards the heavens, only to come back down", 1.5)
    text("And crush you into oblivion.", 1.5)
    for arc in range(200):
        fred.fd(1)
        fred.right(1)
    wn.addshape(os.path.expanduser("rip.gif"))
    bob.shape(os.path.expanduser("rip.gif"))
    question("GAME OVER")
    wn.exitonclick()  # dead end

def aabab():
    write.clear()
    wn.addshape(os.path.expanduser("santa.gif"))
    fred.shape(os.path.expanduser("santa.gif"))
    fred.goto(-300, 400)
    fred.showturtle()
    text("Santa arrives.", 1)
    text("He drops off a care package.", 1.5)
    present.goto(-300, 200)
    present.showturtle()
    wn.addshape(os.path.expanduser("present.gif"))
    present.shape(os.path.expanduser("present.gif"))
    present.goto(bob.xcor(), bob.ycor())
    death()
    text("The care package falls on your face.", 1.5)
    text("You are now a very flat, very dead penguin.", 1.5)
    question("GAME OVER.")
    bob.goto(0, 0)          #dead end
    wn.exitonclick()


def aac(): #choice1aac
    write.clear()
    fred.goto(-500, 0)
    text('Fred screams, "FREEDOM!"', 1.75)
    text("However, that freedom is short-lived.", 1.75)
    text("The zookeeper hears Fred and stuffs both of you back into your cages.", 1.75)
    bob.goto(0,0)
    fred.goto(-300, 0)
    text("You live out the rest of your life in oppression,", 1.5)
    text("regretting that you didn't kill Fred when you had the chance.", 1.75)
    bob.goto(100, 20)
    death()
    question("GAME OVER.")
    wn.exitonclick()


def ab(): #choice1ab
    write.clear()
    text("What in the world were you thinking?", 2)
    text("Fred realizes how incompetent you are.", 1.75)
    text("Fred frees himself from his cage with his magic skills.", 1.75)
    text("Out of pity, he unlocks your cage for you.", 1.75)
    fred.goto(0, 0)
    time.sleep(1)
    bob.goto(200, 0)
    text("You are completely useless, so Fred leaves you behind.", 1.75)
    fred.goto(-1000, 0)
    question("What do you do now?")

def aba():
    write.clear()
    one.clear()
    for x in range(4):
        bob.left(random.randrange(0, 90))
        bob.fd(90)
    text("After 30 seconds, you see Fred in the distance.", 1.5)
    text("You call out to him. Fred approaches you, angry", 1.25)
    fred.goto(bob.xcor() - 200, bob.ycor())
    text("The zookeeper sees both of you trying to escape.", 1.5)
    text("Fred throws a banana at you and flees the zoo.", 1.75)
    three.penup()
    three.goto(fred.xcor(), fred.ycor())
    three.showturtle()
    wn.addshape(os.path.expanduser("banana.gif"))
    three.shape(os.path.expanduser("banana.gif"))
    three.goto(bob.xcor(), bob.ycor())
    fred.goto(-1000, 0)
    text("Suprised by Fred's attack, you stand in place, unsure of what to do.", 1.75)
    text("The zookeper grabs you and puts you back where you belong: in a cage.", 1.75)
    bob.goto(100, 20)
    cage(0, -50)
    text("Now the zookeeper always keeps close watch over you.", 1.5)
    text("You die of hopelessness.", 1)
    death()
    question("GAME OVER")
    wn.exitonclick()




def ac(): #choice1ac
    write.clear()
    text("You lose all of your blubber.", 2)
    text("Then, of course, you die.", 2)
    bob.goto(100, 20)
    death()
    question("GAME OVER.")                               #dead end
    wn.exitonclick()

#b choices

def b(): #first choice2                                 #dead end
    write.clear()
    aaa()

#c choices

def c(): #first choice3
    write.clear()
    text("You die from indecisiveness.", 2)
    bob.goto(100, 20)
    death()
    question("GAME OVER.")
    fred.goto(-1000, 0)
    wn.exitonclick()                            #dead end



def main():
    wn.bgcolor("Seagreen")
    one.speed(100)
    hide()
    sky()
    wn.addshape(os.path.expanduser("minion.gif"))
    fred.shape(os.path.expanduser("minion.gif"))
    fred.goto(-300, 0)
    wn.addshape(os.path.expanduser("giphy (1).gif"))
    bob.shape(os.path.expanduser("giphy (1).gif"))
    cage(0, -50)
    cage(-410, -120)
    text("Escape the Zoo: A Choose Your Own Adventure!", 2)
    text("You are Bob, a penguin in captivity.", 1.75)
    text("Oppressed by life in the zoo, you decide to escape.", 1.75)
    text("Fred the minion wants to join you in your quest for freedom.", 1.75)
    question("Do you agree to take him along?")
    print("")
    print("1.Yes. He's my friend.")
    print("2.Nah. He's dead weight.")
    print("3.I don't know.")
    print("")
    abc = input("Press 1, 2, or 3: ")                           #choice1
    abc = int(abc)
    if abc == 1:
        a()
        print("")
        print("1.Peck the lock.")
        print("2.Repeatedly headbutt the cage.")
        print("3.Lose weight so you can fit through the bars.")
        print("")
        abc = input("Press 1, 2, or 3: ")                       #choice1a
        if abc == 1:
            aa()
            print("")
            print("1.Bail on Fred and leave him to die in his cage.")
            print("2.Lie to him that you will come back for him after you scout out the escape route.")
            print("3.Unlock his cage and let him follow you anyway.")
            print("")
            abc = input("Press 1, 2 or 3:")                   #choice1aa
            if abc == 1:
                aaa()
            elif abc == 2:
                aab()
                print("")
                print("1.Go to the store.")
                print("2.Waddle out of the zoo.")
                print("")
                abc = input("Press 1 or 2: ")               #choice1aab
                if abc == 1:
                    aaba()
                else:
                    aabb()
                    print("")
                    print("1.Praise the almighty penguin god.")
                    print("2.Pray to Santa.")
                    print("")
                    abc = input("Press 1 or 2:")
                    if abc == 1:
                        aabaa()
                        print("")
                        print("1.Pay your respects.")
                        print("2.Laugh at the penguin's deformed eyes.")
                        print("")
                        abc = input("Press 1 or 2:")
                        if abc == 1:
                            aabaaa()
                        else:
                            aabaab()
                    else:
                        aabab()
            else:
                aac()

        elif abc == 2:
            ab()
            print("")
            print("1.Try to find Fred.")
            print("2.Waddle out of the zoo.")
            print("")
            abc = input("Press 1 or 2: ")
            if abc == 1:
                aba()
            else:
                aabb()
                print("")
                print("1.Praise the almighty penguin god.")
                print("2.Pray to Santa.")
                print("")
                abc = input("Press 1 or 2:")
                if abc == 1:
                    aabaa()
                    print("")
                    print("1.Pay your respects.")
                    print("2.Laugh at the penguin's deformed eyes.")
                    print("")
                    abc = input("Press 1 or 2:")
                    if abc == 1:
                        aabaaa()
                    else:
                        aabaab()
                else:
                    aabab()
        else:
            ac()
    elif abc == 2:
        b()
    else:
        c()


main()

wn.exitonclick()