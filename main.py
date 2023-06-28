import turtle
from turtle import Turtle, Screen
import pandas

FONT = ("Arial", 6, "normal")
WIN_FONT = ("Arial", 20, "normal")
ALIGNMENT = "center"
screen_title = "U.S. States Game"

screen = Screen()
screen.title(screen_title)
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
states = data["state"].to_list()

turtle = Turtle()
turtle.hideturtle()
turtle.penup()
correct_states = 0
guessed_states = []


def show_states_on_map(found_state, x, y):
    turtle.goto(x, y)
    turtle.write(f"{found_state}", align=ALIGNMENT, font=FONT)


def show_end_message():
    turtle.goto(0, 0)
    turtle.write("Congratulations, you have found all states!", align=ALIGNMENT, font=WIN_FONT)


# states to learn.csv
unknown_states = []

text_input_title = "Guess the State"
game_is_on = True

while game_is_on:
    answer_state = screen.textinput(title=text_input_title, prompt="What's another state's name?")
    if answer_state.lower() == "exit":

        # With List Comprehension:
        unknown_states = [state for state in states if state not in guessed_states]
        unknown_states_dict = {
            "state": unknown_states,
        }
        unknown_data = pandas.DataFrame(unknown_states_dict)
        unknown_data.to_csv("learn.csv")
        game_is_on = False
    for state in states:
        if state in guessed_states:
            pass
        elif answer_state.lower() == state.lower():
            found_state_data = data[data["state"] == state]
            found_state_x_cor = int(found_state_data["x"])
            found_state_y_cor = int(found_state_data["y"])
            show_states_on_map(state, found_state_x_cor, found_state_y_cor)
            correct_states += 1
            guessed_states.append(state)
            text_input_title = f"{correct_states}/50 States Correct"
        if correct_states == 50:
            game_is_on = False
            show_end_message()

# Get coordinates from image
# def get_mouse_click_coor(x, y):
#     print(x, y)
#
#
# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()
