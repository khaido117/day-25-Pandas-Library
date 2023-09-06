import turtle
import os 
import pandas 

ALL_STATES = 50
CORRECT_ANSWER = 0
#Change directory
os.chdir("/Users/khaido/Library/CloudStorage/GoogleDrive-khaitroyy@gmail.com/My Drive/Code/day-25-Pandas-Library/Game")
print(os.getcwd())

#Create a screen
screen = turtle.Screen()
screen.title("U.S States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
screen.tracer(0)
game_is_on = True 

#Read data. 
data = pandas.read_csv("50_states.csv")
state_list = data["state"].to_list()

guessed_states = []

#Start the question
while len(guessed_states) < 50:

    answer_state = (screen.textinput(title=f" {CORRECT_ANSWER}/{ALL_STATES}States Correct", prompt="What's another state name?")).title()
    if answer_state == "Exit":
        learn_states = []
        for state in state_list:
            if state not in guessed_states:
                learn_states.append(state)
        new_data = pandas.DataFrame(learn_states)
        new_data.to_csv("states_to_learn.csv")
        break

    if answer_state in state_list:
        guessed_states.append(answer_state)

        #Change score & title
        CORRECT_ANSWER += 1

        #Find the answer row.
        state_row = data[data.state == answer_state]

        #Create answer object.
        anwer = turtle.Turtle()
        anwer.goto(int(state_row.x), int(state_row.y))
        anwer.write(f"{answer_state}")

learn_states = []
for state in guessed_states:
    if state not in state_list:
        learn_states.append(state)
        print(learn_states)



