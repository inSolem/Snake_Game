from turtle import Turtle, Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width = 600, height = 600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
score_board = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_on = True

while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    #Detect collision with food
    if snake.head.distance(food) < 15:
        snake.extend()
        food.refresh()
        score_board.increase_score()

    #Dectect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        score_board.reset()
        snake.reset()

    # #Go through other side of wall
    # if snake.head.xcor() > 280:
    #     snake.head.goto(-280, snake.head.ycor())  
    
    # elif snake.head.xcor() < -280:
    #     snake.head.goto(280, snake.head.ycor()) 
    
    # elif snake.head.ycor() > 280:
    #     snake.head.goto(snake.head.xcor(), -280) 
        
    # elif snake.head.ycor() < -280:
    #     snake.head.goto(snake.head.xcor(), 280)

    #Dectect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            score_board.reset()
            snake.reset()

screen.exitonclick()