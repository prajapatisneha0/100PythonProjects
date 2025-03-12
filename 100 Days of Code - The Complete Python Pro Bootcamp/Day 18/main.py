import turtle as t
import random

tom = t.Turtle()
tom.shape("turtle")

#Draw random shapes
# colours = ["CornflowerBlue" , "DarkOrchid" , "IndianRed" , "DeepSkyBlue" , "LightSeaGreen" , "wheat" , "SlateGray", "SeaGreen"]
# def draw_shape(num_sides):
#     angle = 360 / num_sides
#     for _ in range(num_sides):
#         t.fd(100)
#         t.rt(angle)
#
# for shape_sides_n in range(3 ,11):
#     t.color(random.choice(colours))
#     draw_shape(shape_sides_n)

# Draw random walk
t.colormode(255)

def random_color():
    r = random.randint(0 , 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g ,b)
    return random_color

directions = [0,90,180,270]
t.pensize(10)
t.speed("fastest")
for _ in range(100):
    t.color(random_color())
    t.fd(40)
    t.seth(random.choice(directions))
