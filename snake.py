from gamescreen import *
from data import *

class Snake:
    def __init__(self, speed, shape, color):
        self.speed = speed
        self.shape = shape
        self.color = color
    
    def determineSpeed(self):
        return snake.speed(self.speed)
    
    def determineShape(self):
        return snake.shape(self.shape)
    
    def determineColor(self):
        return snake.color(self.color)

    def determineCoord(self, x, y):
        return snake.goto(x, y)

try:
    Snakeo = Snake(0, 'square', 'black')
    Snakeo.determineSpeed()
    Snakeo.determineShape()
    snake.penup()
    Snakeo.determineCoord(0, 0)
except:
    print("Done loading the snake")