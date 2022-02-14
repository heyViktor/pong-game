from turtle import Turtle


class Ball(Turtle):
    def __init__(self, starting_position):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.goto(starting_position)

        self.x_move = 10
        self.y_move = 10

        self.current_speed = 0.1

    def move(self):
        x_position = self.xcor() + self.x_move
        y_position = self.ycor() + self.y_move
        self.goto(x_position, y_position)

    def bounce_top(self):
        self.y_move *= -1

    def bounce_sides(self):
        self.x_move *= -1
        self.current_speed *= 0.8

    def restart(self):
        self.goto(0, 0)

        self.x_move *= -1
        self.y_move *= -1
        self.current_speed = 0.1
