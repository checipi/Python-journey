from turtle import Turtle, Screen
import colorgram
from random import choice

def main():    
    turtle = Turtle()
    screen = Screen()
    # colors = colorgram.extract("03_polka_dots.jpg",12)
    # extracterd_colours = []
    # for _ in range(0, len(colors)):
    #     color = colors[_]
    #     rgb = color.rgb
    #     extracterd_colours.append((rgb.r,rgb.g,rgb.b))

    
    color_list = [
        (245, 234, 241),
        (232, 167, 61),
        (52, 110, 156),
        (119, 149, 202),
        (211, 122, 163),
        (17, 128, 95),
        (149, 20, 59),
        (4, 176, 143),
        (177, 45, 85),
        (223, 202, 119),
    ]
    
    # TODO: 10 rows 10 columns
    # TODO: dot size 20, space 50
    
    turtle.penup()
    screen.colormode(255)
    turtle.hideturtle()
    

    
    # turtle.dot(20)
    # for i in range(1, 11):
    #     for _ in range(9):
    #         turtle.forward(50)
    #         turtle.dot(20, random.choice(color_list))
    #     if i%2 == 0 and i<10:
    #         turtle.right(90)
    #         turtle.forward(50)
    #         turtle.right(90)            
    #         turtle.dot(20, random.choice(color_list))
    #     else:
    #         turtle.left(90)
    #         turtle.forward(50)
    #         turtle.left(90)            
    #         turtle.dot(20, random.choice(color_list))
    for row in range(1, 11):
        
        teleport_y = -250
        turtle.teleport(x=-250,y=teleport_y+(row*50))
        for _ in range(9):
            turtle.dot(40, choice(color_list))
            turtle.forward(50)
            turtle.dot(40, choice(color_list))

    
    
    
    screen.exitonclick()


if __name__ == "__main__":
    main()
