from turtle import Turtle, Screen
import random

s = Screen()
is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-70, -40, -10, 20, 50, 80]
all_turtles = []

#Create 6 turtles
for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(x=-230, y=y_positions[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        #230 is 250 - half the width of the turtle.
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")

        #Make each turtle move a random amount.
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

# # TODO Etch sketch
#
# def move_forwards():
#     t.forward(10)
#
#
# def move_backward():
#     t.backward(10)
#
#
# def counter_clockwise():
#     t.left(10)
#
#
# def clockwise():
#     t.right(10)
#
#
# def clear():
#     t.clear()
#     t.penup()
#     t.home()
#     t.pendown()
#
# s.listen()
# s.onkey(key="w", fun=move_forwards)
# # onkey is a higher order function because its take another function move_forward as an input.
# s.onkey(key="s", fun=move_backward)
# s.onkey(key="a", fun=counter_clockwise)
# s.onkey(key="d", fun=clockwise)
# s.onkey(key="c", fun=clear)


s.exitonclick()
