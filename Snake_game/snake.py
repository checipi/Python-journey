from turtle import Turtle


MOVE_DISTANCE = 20
START_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]

class Snake():

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in START_POSITIONS:
            self.add_segment(position)
            
    def add_segment(self, position):
        segment = Turtle(shape="square")
        segment.color("white")
        segment.penup()
        segment.setposition(position)
        self.segments.append(segment)       


    def extend(self):
        self.add_segment(self.segments[-1].position())


    def advance(self):
        for segm_num in range(len(self.segments)-1, 0, -1):
            new_x_poz = self.segments[segm_num-1].xcor()
            new_y_poz = self.segments[segm_num-1].ycor()
            self.segments[segm_num].goto(new_x_poz, new_y_poz)
        self.head.forward(MOVE_DISTANCE)


    def up(self):
        if self.segments[0].xcor()>self.segments[1].xcor():
            self.segments[0].left(90)
        elif self.segments[0].xcor()<self.segments[1].xcor():
            self.segments[0].right(90)
        

    def down(self):
        if self.segments[0].xcor()>self.segments[1].xcor():
            self.segments[0].right(90)
        elif self.segments[0].xcor()<self.segments[1].xcor():
            self.segments[0].left(90)


    def left(self):
        if self.segments[0].ycor()>self.segments[1].ycor():
            self.segments[0].left(90)
        elif self.segments[0].ycor()<self.segments[1].ycor():
            self.segments[0].right(90)


    def right(self):
        if self.segments[0].ycor()>self.segments[1].ycor():
            self.segments[0].right(90)
        elif self.segments[0].ycor()<self.segments[1].ycor():
            self.segments[0].left(90)




