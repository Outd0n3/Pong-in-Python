from tkinter import CENTER
from turtle import Turtle
import time


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.l_score, align="center", font=("Courier", 80, "normal"))
        self.goto(100, 200)
        self.write(self.r_score, align="center", font=("Courier", 80, "normal"))
        self.line()

    def l_point(self):
        self.l_score += 1
        self.update_scoreboard()

    def r_point(self):
        self.r_score += 1
        self.update_scoreboard()

    def line(self):
        self.penup()
        self.goto(x=0, y=300)
        self.setheading(270)
        for pos in range(600):
             self.pensize(10)
             self.pendown()
             self.color('white')
             self.forward(10)
             self.penup()
             self.forward(20)

    def end(self, winner):
        self.goto(0, 0)
        self.write(f"End of game.\nThe {winner} wins!", move=False, align=CENTER, font=("Courier", 30, "normal"))
        time.sleep(3)
        


