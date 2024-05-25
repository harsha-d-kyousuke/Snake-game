from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score}", align="center", font=("Arial", 24, "normal"))

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

    def display_final_score(self):
        self.goto(0, 0)
        self.write("Game Over", align="center", font=("Arial", 36, "bold"))
        self.goto(0, -50)
        self.write(f"Final Score: {self.score}", align="center", font=("Arial", 24, "normal"))

    def reset(self):
        # Reset the score to 0
        self.score = 0

    def game_over(self):
        # No popup here, just display the game over message
        print("Game Over")
        

