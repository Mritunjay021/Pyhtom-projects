from turtle import Turtle
STP=[(0, 0),(-20,0),(-40,0)]
MVD=20
UP=90
DOWN=270
RT=0
LT=180
class Snake:
    def __init__(self):
        self.segments=[]
        self.create_snake()
        self.head= self.segments[0]
    def create_snake(self):
        for position in STP:
            tim = Turtle("square")
            tim.color("white")
            tim.penup()
            tim.goto(position)
            self.segments.append(tim)

    def move(self):
         for seg_num in range(len(self.segments)-1,0,-1):
            new_x=self.segments[seg_num-1].xcor()
            new_y=self.segments[seg_num-1].ycor()
            self.segments[seg_num].goto(new_x,new_y)
         self.head.forward(MVD)

    def up(self):
         self.head.seth(UP)
    def down(self):
        self.head.seth(DOWN)


    def left(self):
        self.head.seth(LT)


    def right(self):
        self.head.seth(RT)
























































            



