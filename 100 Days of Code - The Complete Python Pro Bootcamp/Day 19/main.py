from turtle import Turtle , Screen

tim = Turtle()
screen = Screen()
tim.shape("turtle")

def move_forward():
    tim.fd(10)
def move_backward():
    tim.back(10)
def turn_right():
    tim.rt(10)
def turn_left():
    tim.lt(10)
def clear():
    tim.clear()
    tim.up()
    tim.home()
    tim.down()

screen.listen()
screen.onkey(move_forward ,"w")
screen.onkey(move_backward ,"s")
screen.onkey(turn_right ,"d")
screen.onkey(turn_left ,"a")
screen.onkey(clear ,"c")

screen.exitonclick()