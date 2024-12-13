from turtle import Turtle, Screen
from random import choice, randint


def main():
    turtle = Turtle()
    screen = Screen()


    screen.colormode(255)
    speed = 1
    pen_size = 4
    
    
    

    #Random walk
    for i in range(100):
        turtle.pencolor(randint(0,255),randint(0,255),randint(0,255))
        turtle.pensize(pen_size)
        turtle.setheading(90*randint(0,4))
        turtle.forward(20)
        turtle.speed(speed)
        speed += 0.1
        pen_size += 0.05
    
    
    #Draw circles 360 degrees
    for _ in range(0,368,6):
        turtle.pencolor(randint(0,255),randint(0,255),randint(0,255))
        turtle.speed(0)
        turtle.setheading(_)
        turtle.circle(180)
        
    screen.exitonclick()
    
if __name__ == "__main__":
    main()
