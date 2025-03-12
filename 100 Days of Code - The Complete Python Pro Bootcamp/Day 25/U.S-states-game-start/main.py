import turtle
import pandas

# Set up the screen
screen = turtle.Screen()
screen.title("U.S. States Game")

# Load the background image of the U.S. map
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# Read state data
data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(
        title=f"{len(guessed_states)}/50 States Correct",
        prompt="Enter a state's name (or type 'Exit' to quit):"
    )

    if answer_state is None:  # Handle if the user cancels input
        continue

    answer_state = answer_state.title()  # Convert input to title case

    if answer_state == "Exit":
        # Find the missing states and save them to a CSV file
        missing_states = [state for state in all_states if state not in guessed_states]
        new_data = pandas.DataFrame(missing_states, columns=["State"])
        new_data.to_csv("states_to_learn.csv", index=False)
        print("File saved: states_to_learn.csv")
        break

    if answer_state in all_states and answer_state not in guessed_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x.item()), int(state_data.y.item()))
        t.write(answer_state)

# Keep the screen open until the user closes it
turtle.mainloop()