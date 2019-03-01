# Import turtle, a simple drawing library
import turtle
import random


# List of english words and number of hangman pieces left variable
english_words = ['back', 'cheeks', 'chest', 'chin', 'ears', 'eyebrows', 'eyes', 'feet', 'fingers', 'foot', 'forehead',
                 'hair', 'hands', 'head', 'hips', 'knees', 'legs', 'lips', 'mouth', 'neck', 'nose', 'shoulders',
                 'teeth', 'stomach', 'teeth', 'throat', 'toes', 'tongue', 'tooth', 'waist'
                 'alligator', 'ant', 'bear', 'bee', 'bird', 'camel', 'cat', 'cheetah', 'chicken',
                 'chimpanzee', 'cow', 'crocodile', 'deer', 'dog', 'dolphin', 'duck', 'eagle', 'elephant', 'fish',
                 'fly', 'fox', 'frog', 'giraffe', 'goat', 'goldfish', 'hamster', 'hippopotamus', 'horse', 'kangaroo',
                 'kitten', 'lion', 'lobster', 'monkey', 'octopus', 'owl', 'panda', 'pig', 'puppy', 'rabbit', 'rat',
                 'scorpion', 'seal', 'shark', 'sheep', 'snail', 'snake', 'spider', 'squirrel',
                 'tiger', 'turtle', 'wolf', 'zebra']
n_pieces_left = 7

# Choose if the host is the machine or a human
machine_host_option = input('Choose who you want the \"Host\" to be. '
                            'If you want the word to be chosen by the machine type something and then press enter. '
                            'If you want a a human to chose the word, just press enter.')

if not machine_host_option:
    # Input host word variable
    host_word = input('Roses are red, Violets are blue... What are you!? Where are you!?\n'
                      'As the master player \"Host\" you will have the important task '
                      'of choosing the word that the players will have to guess! Now choose a word: ')

# Checks if input is in alphabet and at least 1 letter for 100 times, if problem persists exit
    for i in range(100):
        if not host_word.isalpha() or len(host_word) == 0:
            host_word = input('Please remember to only one word. Not a number, not a phrase, just a word. Try again! ')
    if not host_word.isalpha() or len(host_word) == 0:
        exit()

# Make input lower case
    host_word.lower()

else:
    host_word = random.choice(english_words)

# Correct guesses variable
correct_guesses = ['-'] * len(host_word)

# Easter eggs
if host_word in ['penguin', 'a human', 'a penguin', 'person', 'a person', 'human', 'barcelona',
                 'ironhack', 'ironhack campus', 'catalonia', 'spain', 'marina', 'earth', 'planet earth', 'the galaxy']:
    print('Congrats! You have found the hidden easter egg! You are awesome!')
    exit()

# Dictionary for pieces of hangman
hangman_parts = {7: 'upside down L', 6: 'head', 5: 'body', 4: 'arm', 3: 'arm', 2: 'leg', 1: 'leg'}


# Define Hangman drawings for turtle library
def draw_hangman_piece(piece, pen):
    if piece == 7:
        for it in range(2):
            pen.left(90)
            pen.forward(250)
    elif piece == 6:
        pen.left(90)
        pen.forward(25)
        pen.right(90)
        pen.circle(25)
    elif piece == 5:
        pen.penup()
        pen.left(90)
        pen.forward(50)
        pen.pendown()
        pen.forward(105)
    elif piece == 4:
        pen.penup()
        pen.right(180)
        pen.forward(70)
        pen.pendown()
        pen.left(135)
        pen.forward(60)
    elif piece == 3:
        pen.right(180)
        pen.penup()
        pen.forward(60)
        pen.right(90)
        pen.pendown()
        pen.forward(60)
    elif piece == 2:
        pen.penup()
        pen.right(180)
        pen.forward(60)
        pen.left(135)
        pen.forward(70)
        pen.right(45)
        pen.pendown()
        pen.forward(60)
    elif piece == 1:
        pen.right(180)
        pen.penup()
        pen.forward(60)
        pen.right(90)
        pen.pendown()
        pen.forward(60)


# Function that outputs True if the player has lost
def player_lost():
    if n_pieces_left > 0:
        return False
    else:
        return True


# Function that outputs True if the player has won
def player_won():
    return '-' not in correct_guesses


# Function that processes a turn
# and returns a different number of hangman parts and correct_guesses changes
# if one of them has to be changed
def turn(guess_, correct_guesses_, n_pieces_left_):
    # Copy of correct_guesses_list to do updates
    correct_guesses_out = correct_guesses_

    if guess_ in correct_guesses_:
        # If letter has already been guessed
        # ask for a new letter 100 times. If problem persists exit
        for it in range(100):
            guess_ = input('This letter has already been guessed! Please type a new one :) ')
            if guess_ not in correct_guesses_:
                break
        if guess_ in correct_guesses_:
            print('Maximum times of tries reached. Exiting now.')
            exit()

    if guess_ in host_word:
        # If letter hasn't been guessed and is correct
        # save it in the correct index of correct_guesses
        print('Correct! ' + guess_ + ' has been found')
        for index, char in enumerate(host_word):
            if char == guess_:
                correct_guesses_out[index] = guess_  # Update correct_guesses_out
        # Print correct guesses list for player context
        print(correct_guesses_out)

        return correct_guesses_out, n_pieces_left_
    else:
        # If letter hasn't been guessed and is incorrect
        # draw the corresponding hangman piece and subtract one to n_pieces_left
        print('Wrong letter... The host draw a: ' + hangman_parts[n_pieces_left_])
        draw_hangman_piece(n_pieces_left_, drawing_pen)

        return correct_guesses_, n_pieces_left_ - 1  # Update correct n_pieces_left


# Tell players how many letters the host_word has and new blank lines so the other players can't see the answer
for i in range(20):
    print('\n')
print('The host has chosen a word with ' + str(len(host_word)) + ' letters in it')

# Show screen and define "pen"
screen = turtle.Screen()
drawing_pen = turtle.RawPen(screen)
drawing_pen.hideturtle()

# For 100 times, if there isn't a clear winner or loser continue asking for letters and running turns
for i in range(100):
    if not player_won() and not player_lost():
        guess = input('Please type the letter you think is in the hosts word: ')

        # Checks if input is in alphabet and only one character (one letter) for 100 times,
        # then exits program if user persists
        for ii in range(100):
            if not guess.isalpha() or len(guess) > 1 or len(guess) == 0:
                guess = input('Please remember to only type 1 letter. '
                              'Not a number, not a phrase, just a letter. Try again! ')
        if not guess.isalpha() or len(guess) > 1 or len(guess) == 0:
            print('Maximum times of tries reached. Exiting now.')
            exit()

        guess_l = guess.lower()

        # Run a turn with the guess and update correct_guesses and n_pieces_left
        correct_guesses, n_pieces_left = turn(guess_l, correct_guesses, n_pieces_left)
    else:
        break

# Print message depending if the player won or host won
if player_lost():
    a = input('Congrats you have lost! Losing is a part of learning so, don\'t worry, in a way you haven\'t lost. '
              'But not here, lol. Here you actually lost.')
else:
    print('Incredible! Amazing! Wonderful! Congrats, you actually won! Who would have said it...')
