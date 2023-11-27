from turtle import Turtle, Screen
import random


screen = Screen()
screen.setup(width=500, height=400)

color_arr = ["red", "blue", "green", "purple", "black", "orange"]

user_bet = screen.textinput(
    title="Make your bet", prompt="Enter the color turtle that you think will win the race: ")

y_coord = -70
is_on = False

all_turtles = []

for color_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(color_arr[color_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_coord)
    y_coord += 30
    all_turtles.append(new_turtle)

if user_bet:
    is_on = True

while is_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_on = False
            winning_color = turtle.pencolor()
            if user_bet == winning_color:
                print(f"You won! {winning_color} turtle won the race!")
            else:
                print(f"You lost! {winning_color} turtle won the race!")
        distance = random.randint(0, 10)
        turtle.fd(distance)


screen.exitonclick()
