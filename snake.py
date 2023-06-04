import turtle
import time
import snake_module
import food
import scoreboard
import sys

interface = turtle.Screen()
interface.setup(width=600, height=600)
interface.bgcolor("black")
interface.title("Snake Game")
interface.tracer(0)

snake = snake_module.Snake()
food = food.Food()
scoreboard = scoreboard.Scoreboard()

interface.listen()
interface.onkey(snake.up, "Up")
interface.onkey(snake.down, "Down")
interface.onkey(snake.left, "Left")
interface.onkey(snake.right, "Right")

def quit():
    interface.bye()
    sys.exit("Exit")

interface.onkey(quit, "q")

gameOn = True
while gameOn == True:
    interface.update()
    time.sleep(0.1)
    snake.move_snake()

    #detects collision w/ food:
    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.increase()
        snake.extend()

    #detect collision w/ wall:
    if snake.head.xcor() > 295 or snake.head.xcor() < -295 or snake.head.ycor() > 270 or snake.head.ycor() < -295:
        scoreboard.reset()
        snake.reset()

    #detect collision w/ self:
    for piece in snake.snake:
        if piece == snake.head:
            pass
        elif snake.head.distance(piece) < 10:
            scoreboard.reset()
            snake.reset()

interface.exitonclick()
