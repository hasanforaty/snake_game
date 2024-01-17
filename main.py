import time
from turtle import Screen
from food import Food
from scoreboard import Scoreboard
from snake import Snake

screen = Screen()
screen.setup(600, 600)
screen.bgcolor('black')
screen.title("Snake Game ")

game_is_on = True
screen.tracer(0)

snake = Snake()
food = Food()
score = Scoreboard()
screen.listen()
screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.left, 'Left')
screen.onkey(snake.right, 'Right')


while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

#     collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        score.increase_score()


screen.exitonclick()
