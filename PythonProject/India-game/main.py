# import turtle
# import pandas
#
# screen = turtle.Screen()
# screen.title("india States Game")
# screen.setup(width=430,height=450)
# image = "india_state.gif"
# screen.addshape(image)
# turtle.shape(image)
# data = pandas.read_csv("states_data.csv")
# all_states = data.states.to_list()
# guessed_states = []
#
# while len(guessed_states) <29 :
#     answer_state = screen.textinput(title=f"{len(guessed_states)}/29 states correct", prompt="What another states's name ?(type Exit to close)").title()
#
#     if answer_state == "Exit":
#         missing_states = [state for state in all_states if state not in guessed_states]
#         new_data = pandas.DataFrame(missing_states, columns=["State"])
#         new_data.to_csv("states_to_learn.csv", index=False)
#         print("File saved: states_to_learn.csv")
#         break
#
#     if answer_state in all_states and answer_state not in guessed_states:
#         t= turtle.Turtle()
#         t.hideturtle()
#         t.up()
#         state_data = data[data.states == answer_state]
#         t.goto(int(state_data.x.item()), int(state_data.y.item()))
#         t.write(answer_state)
#
# screen.exitonclick()

import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("india States Game")
image = "india_state.gif"
screen.addshape(image)
turtle.shape(image)

data = pd.read_csv("states_data.csv")
all_states = data.state.to_list()
guessed_states = []

while len(guessed_states) < 29:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/29 states correct",
                                    prompt="What's another state's name ?")

    if answer_state is None:  # Handle if the user cancels input
        continue

    answer_state = answer_state.title()  # Convert input to title case

    if answer_state == "Exit":
        missing_states = []
        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)
        new_data = pd.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break

    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)

screen.exitonclick()
