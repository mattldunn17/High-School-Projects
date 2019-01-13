"""
File: AstroRacer.py

Author: Matt Dunn

Purpose: Simple button mashing game that can be played with one or two players
"""

from tkinter import *
from tkinter.font import *
import turtle
import random
import time

class AstroRacer(Frame):

    def __init__(self):
        #Sets up the window and widgets
        Frame.__init__(self)
        self.master.title("AstroRacer")
        self.grid()

        #Creates Header
        font = Font(family = "Verdana",
                    size = 20, slant = "italic")
        self._label = Label(self, font = font,
                            text = "AstroRacer")
        self._label.grid()

        #Creates buttons
        self._button1 = Button(self,
                               text = "1 Player",
                               command = self._start)
        self._button1.grid()

        self._button2 = Button(self,
                               text = "2 Players",
                               command = self._start2)
        self._button2.grid()

    def _start(self):
        #variables
        playerScore = 0
        start = 0
        end = 0
        n = 0

        #moves rocket forward until it crosses finish line
        def _moveForward():
            if rocket.ycor() > 360:
                print("Play again to get a better time!")
            elif rocket.ycor() == 360:
                _done()
                rocket.forward(5)
            else:
                rocket.forward(5)

        #finishes clock and shows time
        def _done():
            print("FINISHED!")
            end = time.clock()
            playerScore = end - start
            print("Your Time: " + str(playerScore))

        #starts clock
        def _go():
            print("Mash 'P' and 'Q' to move forward!")
            print("GOOOOOOOO!")
            start = time.clock()

        #creates screen
        wn = turtle.Screen()
        wn.setworldcoordinates(-200, -400, 200, 400)
        wn.bgcolor("black")

        #forms rocket
        rocket = turtle.Turtle()
        rocket.hideturtle()
        rocket.color("white")
        rocket.shape("classic")
        rocket.shapesize(2, 2)
        rocket.left(90)
        rocket.speed("fast")
        rocket.up()

        #forms stars
        rocket.color("white")
        for i in range(101):
            rocket.goto(random.randrange(-200, 200), random.randrange(-400, 400))
            rocket.dot(random.randrange(2, 6))

        #creates finish line
        rocket.pencolor("green")
        rocket.goto(250, 350)
        rocket.left(90)
        rocket.down()
        rocket.pensize(3)
        rocket.forward(500)
        rocket.right(90)
        rocket.up()

        #positions rocket to start race
        rocket.goto(0, -350)
        rocket.showturtle()
        rocket.down()
        rocket.pensize(2)
        rocket.pencolor("orange")

        #starts race and allows user input
        wn.ontimer(_go, 15)
        wn.onkey(_moveForward, "q")
        wn.onkey(_moveForward, "p")
        wn.listen()

        #exits on click
        wn.exitonclick

    def _start2(self):
        #variables
        player1Score = 0
        player2Score = 0
        start = 0
        end = 0

        #moves rocket forward until it crosses finish line
        def _moveForward():
            if rocket.ycor() > 360:
                print("Player 1 can stop spamming!")
            elif rocket.ycor() == 360:
                _done()
                rocket.forward(5)
            else:
                rocket.forward(5)
        def _moveForward2():
            if rocket2.ycor() > 360:
                print("Player 2 can stop spamming!")
            elif rocket2.ycor() == 360:
                _done2()
                rocket2.forward(5)
            else:
                rocket2.forward(5)

        #finishes clock and shows time for player 1
        def _done():
            print("PLAYER 1 FINISHED!")
            end = time.clock()
            player1Score = end - start
            print("Your Time: " + str(player1Score))

        #finishes clock and shows time for player 2
        def _done2():
            print("PLAYER 2 FINISHED!")
            end = time.clock()
            player2Score = end - start
            print("Your Time: " + str(player2Score))

        #starts clock
        def _go():
            print("GOOOOOOOO!")
            start = time.clock()

        print("PLAYER 1: MASH 'Q'. PLAYER 2: MASH 'P'")
        #creates screen
        wn = turtle.Screen()
        wn.setworldcoordinates(-200, -400, 200, 400)
        wn.bgcolor("black")

        #forms rocket
        rocket = turtle.Turtle()
        rocket.hideturtle()
        rocket.color("white")
        rocket.shape("classic")
        rocket.shapesize(2, 2)
        rocket.left(90)
        rocket.speed("fast")
        rocket.up()

        #forms stars
        rocket.color("white")
        for i in range(101):
            rocket.goto(random.randrange(-200, 200), random.randrange(-400, 400))
            rocket.dot(random.randrange(2, 6))

        #creates finish line
        rocket.pencolor("green")
        rocket.goto(250, 350)
        rocket.left(90)
        rocket.down()
        rocket.pensize(3)
        rocket.forward(500)
        rocket.right(90)
        rocket.up()

        #positions rockets to start race
        rocket.goto(-75, -350)
        rocket2 = rocket.clone()
        rocket2.goto(75, -350)
        rocket.showturtle()
        rocket2.showturtle()
        rocket.down()
        rocket2.down()
        rocket.pensize(2)
        rocket2.pensize(2)
        rocket.pencolor("orange")
        rocket2.pencolor("red")

        #starts race and allows user input
        wn.ontimer(_go, 15)
        wn.onkey(_moveForward, "q")
        wn.onkey(_moveForward2, "p")
        wn.listen()

        #exits on click
        wn.exitonclick

def main():
    #Initiates game and pop ups window
    AstroRacer().mainloop()

main()

