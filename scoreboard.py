from turtle import Turtle

SCOREBOARD_FONT = ("Arial", 16, 'bold')


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        self.penup()
        self.speed('fastest')
        self.goto(0, 280)
        self.color('white')
        self.hideturtle()
        self.update_score_board()

    def update_score_board(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}",
                   align="center",
                   font=SCOREBOARD_FONT
                   )

    def increase_score(self):
        self.score += 1
        self.update_score_board()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        self.update_score_board()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME Over !", font=SCOREBOARD_FONT, align="center")
