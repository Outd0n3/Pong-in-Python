
from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.x_move = 3
        self.y_move = 3
        self.move_speed = 0.02

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1


    def bounce_x_r_paddle(self):
        self.x_move = -(abs(self.x_move))
        self.move_speed *= 0.6

    def bounce_x_l_paddle(self):
        self.x_move = (abs(self.x_move))
        self.move_speed *= 0.6

    def reset_position_r(self):
        self.goto(0, 0)
        self.move_speed = 0.02
        self.bounce_x_r_paddle()

    def reset_position_l(self):
        self.goto(0, 0)
        self.move_speed = 0.02
        self.bounce_x_l_paddle()
