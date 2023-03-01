from turtle import Turtle

ALIGNMENT = "center"
FONT = ('Courier', 12, 'normal')


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.current_score = 0
        with open("data.txt") as file:
            high_score = int(file.read())
        self.high_score = high_score
        self.penup()
        self.hideturtle()
        self.setpos(0, 280)

    def show_score(self):
        self.clear()
        self.write(f"Score: = {self.current_score} High Score {self.high_score}", align=ALIGNMENT, font=FONT)

    def add_score(self):
        self.current_score += 1
        self.show_score()

    def reset(self):
        if self.current_score > self.high_score:
            self.high_score = self.current_score
            with open("data.txt", mode="w") as file:
                file.write(f"{self.high_score}")
        self.current_score = 0
        self.show_score()



