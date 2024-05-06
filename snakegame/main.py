from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from score  import Score
import time

sc =Screen()
sc.bgcolor("black")
sc.setup(width=800, height=600)
sc.title("Pong")
sc.tracer(0)

rp =Paddle((390,0))
lp =Paddle((-390,0))
b=Ball()

sc.listen()
sc.onkey(rp.go_up,"w")
sc.onkey(rp.go_down,"s")
sc.onkey(lp.go_up,"a")
sc.onkey(lp.go_down,"d")





gio=True
while gio:
    time.sleep(0.05)
    sc.update()
    b.move()

    if (b.ycor()>290 or b.ycor()<-290):
        b.bounce()

    if (b.distance(rp)<50 and b.xcor()>340 or  b.distance(lp) < 50 and b.xcor() < -340):
        b.colide()

    if b.xcor()>380:
        b.reset_position()
    if b.xcor()<-380:
        b.reset_position()


sc.exitonclick()