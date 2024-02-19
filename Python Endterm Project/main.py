from tkinter import *
import tkinter.font as font
import random


playerScore = 0
computerScore = 0
options = [('rock', 0), ('paper', 1), ('scissors', 2)]


# Function to Randomly Select Computer Choice
def get_computer_choice():
    return random.choice(options)


def player_choice(playerInput):
    global playerScore, computerScore

    computerInput = get_computer_choice()

    player_choice_label.config(text = 'Your Selected : ' + playerInput[0])
    computer_choice_label.config(text = 'Computer Selected : ' + computerInput[0])

    if playerInput == computerInput:
        winner_label.config(text = "Tie")
    elif (playerInput[1] - computerInput[1]) % 3 == 1:
        playerScore += 1
        winner_label.config(text="You Won!!!")
        player_score_label.config(text = 'Your Score : ' + str(playerScore))
    else:
        computerScore += 1
        winner_label.config(text="Computer Won!!!")
        computer_score_label.config(text='Your Score : ' + str(computerScore))


game_window = Tk()
game_window.title("Rock-Paper-Scissors Game")

app_font = font.Font(size = 12)

#Displaying Game Title
game_title = Label(text = 'Rock-Paper-Scissors', font = font.Font(size = 24), fg = 'purple')
game_title.pack()

#Label to dispay, who wins each time
winner_label = Label(text = "Let's start the game", fg = 'green', font = font.Font(size = 15), pady = 8)
winner_label.pack()

input_frame = Frame(game_window)
input_frame.pack()

#Displaying player options
player_options = Label(input_frame, text = "Choose: ", font = font.Font(size = 13), fg = 'blue')
player_options.grid(row = 0, column = 0, pady = 8)

rock_btn = Button(input_frame, text = 'Rock', width = 15, bd = 0, bg = 'pink', pady = 5, command = lambda: player_choice(options[0]))
rock_btn.grid(row = 1, column = 1, padx = 8, pady = 5)

paper_btn = Button(input_frame, text = 'Paper', width = 15, bd = 0, bg = 'yellow', pady = 5, command = lambda: player_choice(options[1]))
paper_btn.grid(row = 1, column = 2, padx = 8, pady = 5)

scissors_btn = Button(input_frame, text = 'Scissors', width = 15, bd = 0, bg = 'light blue', pady = 5, command = lambda: player_choice(options[2]))
scissors_btn.grid(row = 1, column = 3, padx = 8, pady = 5)

#Displaying Score and players choise
score_label = Label(input_frame, text = 'Score: ', font = font.Font(size = 13), fg = 'blue')
score_label.grid(row = 2, column = 0)

player_choice_label = Label(input_frame, text = 'Your Selected : ---', font = app_font)
player_choice_label.grid(row = 3, column = 1, pady = 5)

player_score_label = Label(input_frame, text = 'Your Score : -', font = app_font)
player_score_label.grid(row = 3, column = 2, pady = 5)

computer_choice_label = Label(input_frame, text = 'Computer Selected : ---', font = app_font, fg = 'black')
computer_choice_label.grid(row = 4, column = 1, pady = 5)

computer_score_label = Label(input_frame, text = 'Computer Score : -', font = app_font, fg = 'black')
computer_score_label.grid(row = 4, column = 2, padx = (10,0), pady = 5)

game_window.geometry('800x350')
game_window.mainloop()