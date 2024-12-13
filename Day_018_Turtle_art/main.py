from turtle import Turtle, Screen
from random import randint

my_turtle = Turtle()
screen = Screen()
# Draw a rectangle
# for _ in range(4):
#     my_turtle.forward(100)
#     my_turtle.rt(90)
# Draw a dash line
# for times in range(25):
#     my_turtle.forward(5)
#     my_turtle.penup()
#     my_turtle.forward(5)
#     my_turtle.pendown()
# Draw different shapes in different colours
def main():
    def draw_shape(sides):
        for _ in range(sides):
            my_turtle.forward(100)
            my_turtle.right(360/sides)

        
    for no_sides in range(3, 11):
        screen.colormode(255)
        my_turtle.pencolor(randint(100,255),
                            randint(100,255),
                            randint(100, 255))
        draw_shape(no_sides)


    screen.exitonclick()


if __name__ == "__main__":
    main()

print(0.1*10)