from turtle import Turtle

class Score(Turtle):
    
    def __init__(self, position):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.score = 0
        self.goto(position)
        self.write(self.score, align="center", font=("Courier", 70, "normal"))
    
    def increase_score(self):
        self.score += 1
        self.clear()
        self.write(self.score, align="center", font=("Courier", 70, "normal"))
