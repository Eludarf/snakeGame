from turtle import Turtle
import random


class Food:

    def __init__(self):
        self.food = Turtle("circle")
        self.food.shapesize(0.5, 0.5)
        self.food.penup()
        self.food.color("red")
        self.spawn_food()

    def spawn_food(self):
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.food.goto(random_x, random_y)

    def reset(self):
        self.food.clear()
        self.spawn_food()



