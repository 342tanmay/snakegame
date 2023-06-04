import turtle

STARTING_POS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DIST = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180


class Snake:
    def __init__(self):
        self.snake = []
        self.create_snake()
        self.head = self.snake[0]

    def create_snake(self):
        for position in STARTING_POS:
            self.add_piece(position)

    def move_snake(self):
        for piece in range(len(self.snake) - 1, 0, -1):
            new_x = self.snake[piece - 1].xcor()
            new_y = self.snake[piece - 1].ycor()
            self.snake[piece].goto(new_x, new_y)
        self.head.forward(MOVE_DIST)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def add_piece(self, position):
        new_piece = turtle.Turtle("square")
        new_piece.color("yellow")
        new_piece.penup()
        new_piece.goto(position)
        self.snake.append(new_piece)

    def extend(self):
        self.add_piece(self.snake[-1].position()) #adds piece at end of snake, hence the "-1"

    def reset(self):
        for piece in self.snake:
            piece.hideturtle()
        self.snake.clear()
        self.create_snake()
        self.head = self.snake[0]