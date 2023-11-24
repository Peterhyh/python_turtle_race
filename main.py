from turtle import Turtle, Screen

racer = Turtle(shape="turtle")
screen = Screen()
screen.setup(width=500, height=400)

color_arr = ["red", "blue", "green", "purple", "black", "pink",]

racer.color(color_arr[3])

screen.exitonclick()
