from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 24, "normal")


class Scoreboard:

    def __init__(self):
        self.score = 0
        self.game_over = Turtle()
        self.game_over.color("white")
        self.game_over.hideturtle()
        self.game_over.penup()

        self.scoreboard = Turtle()
        self.scoreboard.color("white")
        self.scoreboard.hideturtle()
        self.scoreboard.penup()
        self.draw_scoreboard()

    def update_scoreboard(self):
        self.score += 1
        self.refresh_score_visual()

    def refresh_score_visual(self):
        self.scoreboard.clear()
        self.draw_scoreboard()

    def draw_scoreboard(self):
        self.scoreboard.goto(0, 265)
        self.scoreboard.write(f"Score: {self.score}", True, ALIGNMENT, FONT)

    def draw_game_over(self):
        self.scoreboard.goto(0, 0)
        self.scoreboard.write("GAME OVER!", True, ALIGNMENT, FONT)
