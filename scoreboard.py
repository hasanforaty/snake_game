from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.speed('fastest')
        self.goto(0, 280)
        self.color('white')
        self.hideturtle()
        self.update_score_board()

    def update_score_board(self):
        self.clear()
        self.write(f"Score: {self.score}",
                   align="center",
                   font=("Arial", 16, 'bold')
                   )

    def increase_score(self):
        self.score += 1
        self.update_score_board()
