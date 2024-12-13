from turtle import Turtle
import random

class Food(Turtle):
    
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.penup()
        self.color("green")
        self.speed("fastest")
        self.refresh()
        
    def refresh(self):
        self.goto(random.randint(-360,360), random.randint(-360, 360))