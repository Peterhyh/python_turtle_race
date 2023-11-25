from turtle import Turtle, Screen


screen = Screen()
screen.setup(width=500, height=400)

color_arr = ["red", "blue", "green", "purple", "black", "pink"]

y_coord = -70

for color_index in range(0, 6):
    racer = Turtle(shape="turtle")
    racer.color(color_arr[color_index])
    racer.penup()
    racer.goto(x=-230, y=y_coord)
    y_coord += 30


screen.exitonclick()
