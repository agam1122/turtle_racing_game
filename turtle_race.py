from turtle import *
import random
screen = Screen()

screen.setup(width=900, height=600)
is_race_on = False
play = True
while play:
    user_bet = screen.textinput(title="Make a bet", prompt="Which turtle will win the race? Enter a color: ").lower()
    colors = ['blue', 'green', 'red', 'orange', 'pink']
    y = 200
    all_turtles = []
    for turtle_index in range(0, 5):
        new_turtle = Turtle()
        new_turtle.penup()
        new_turtle.shape('turtle')
        new_turtle.color(colors[turtle_index])
        new_turtle.goto(x=-430, y=y)
        y -= 100
        all_turtles.append(new_turtle)

    if user_bet:
        is_race_on = True

    while is_race_on:

        for turtle in all_turtles:
            if turtle.xcor() > 430:
                winning_color = turtle.pencolor()
                if winning_color == user_bet:
                    Input = screen.textinput(title=f"You won! {winning_color} turtle won!",
                                             prompt="Play again?[Y/N]").lower()
                else:
                    Input = screen.textinput(title=f"You lost! {winning_color} turtle won!",
                                             prompt="Play again?[Y/N]").lower()
                if Input == 'y':
                    play = True
                    screen.clear()
                else:
                    play = False
                is_race_on = False
            random_distance = random.randint(0, 10)
            turtle.forward(random_distance)
