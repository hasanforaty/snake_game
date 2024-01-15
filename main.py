import turtle
from turtle import Screen, Turtle
import time
from snake import Snake

screen = Screen()
screen.setup(600, 600)
screen.bgcolor('black')
screen.title("Snake Game ")

game_is_on = True
screen.tracer(0)

snake = Snake()
screen.listen()
screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.left, 'Left')
screen.onkey(snake.right, 'Right')


while game_is_on:
    screen.update()
    time.sleep(1.1)
    snake.move()
screen.exitonclick()
