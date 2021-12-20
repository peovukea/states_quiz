import turtle

import pandas

screen = turtle.Screen()
screen.title("U.S States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

writer = turtle.Turtle()
writer.penup()
writer.hideturtle()

data = pandas.read_csv("50_states.csv")
guessed_correct = []
states = data.state.tolist()

while len(guessed_correct) < 50:
    answer_state = screen.textinput(title="Guess the state", prompt="What's another state's name").capitalize()

    if answer_state == 'Exit':
        missing_states = []
        for state in states:
            if state not in guessed_correct:
                missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states-to_learn.csv")
        break

    if answer_state in states and answer_state not in guessed_correct:
        x = int(data[data['state'] == answer_state]['x'])
        y = int(data[data['state'] == answer_state]['y'])
        guessed_correct.append(answer_state)
        writer.goto(x, y)
        writer.write(answer_state)



