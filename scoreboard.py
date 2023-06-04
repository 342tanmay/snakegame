import turtle
ALIGNMENT = "center"
FONT = ("Courier", 20, "normal")

class Scoreboard(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("blue")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update()

    def update(self):
        self.clear()
        self.write(f"Score: {self.score}", align = ALIGNMENT, font = FONT)

    def reset(self):
        self.score = 0
        self.update()

    #def game_over(self):
        #self.goto(0, 0)
        #self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    def increase(self):
        self.score = self.score + 1
        self.update()

