# Import turtle, a simple drawing library
import turtle

# List of english words
english_words = ['back', 'cheeks', 'chest', 'chin', 'ears', 'eyebrows', 'eyes', 'feet', 'fingers', 'foot', 'forehead', 'hair', 'hands', 'head', 'hips', 'knees', 'legs', 'lips', 'mouth', 'neck' , 'nose<', 'shoulders', 'teeth', 'stomach', 'teeth', 'throat', 'toes', 'tongue', 'tooth', 'waist'
                 'alligator', 'ant', 'bear', 'bee', 'bird', 'camel', 'cat', 'cheetah', 'chicken', 'chimpanzee', 'cow', 'crocodile', 'deer', 'dog', 'dolphin', 'duck', 'eagle', 'elephant', 'fish', 'fly', 'fox', 'frog', 'giraffe', 'goat', 'goldfish', 'hamster', 'hippopotamus', 'horse', 'kangaroo', 'kitten', 'lion', 'lobster', 'monkey', 'octopus', 'owl', 'panda', 'pig', 'puppy', 'rabbit', 'rat', 'scorpion', 'seal', 'shark', 'sheep', 'snail', 'snake', 'spider', 'squirrel', 'tiger', 'turtle', 'wolf', 'zebra',
                 ]

# Host word variable and number of hangman pieces left variable
host_word = input('Roses are red, Violets are blue... What are you!? Where are you!?\nAs the master player \"Host\" you will have the important task of choosing the word that the players will have to guess! Now choose a word: ')
n_pieces_left = 7

# Easter eggs
if host_word in ['penguin', 'Penguin', 'human', 'Human', 'ironhack', 'Ironhack']:
    print('Congrats! You have found the hidden easter egg! You are awesome!')
    exit()

# Checks if input is in alphabet and at least 1 letter for 100 times, if problem persists exit
for i in range(100):
    if not host_word.isalpha() or len(host_word) == 0:
        host_word = input('Please remember to only one word. Not a number, not a phrase, just a word. Try again! ')
if not host_word.isalpha() or len(host_word) == 0:
    exit()

# Make input lower case
host_word.lower()

# Correct guesses variable
correct_guesses = [None] * len(host_word)

# Dictionary for pieces of hangman
hangman_parts = {7: 'upside down L', 6: 'head', 5: 'body', 4: 'arm', 3: 'arm', 2: 'leg', 1: 'leg'}

# Define Hangman drawings for turtle library
def draw_hangman_piece(piece, pen):
    if piece == 7:
        for i in range(2):
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
    return None not in correct_guesses

# Function that processes a turn and return a different number of hangman parts if it has to be changed and correct_guesses changes
def turn(guess, correct_guesses, n_pieces_left):
    # Copy of correct_guesses_list to do updates
    correct_guesses_out = correct_guesses

    if guess in correct_guesses: # If letter has already been guessed ask for a new letter 100 times, if problem persists exit
        for i in range(100):
            guess = input('This letter has already been guessed! Please type a new one :) ')
            if guess not in correct_guesses:
                break
        if guess in correct_guesses:
            print('Maximum times of tries reached. Exiting now.')
            exit()

    if guess in host_word:  # If letter hasn't been guessed and is correct save it in the correct index in correct_guesses
        print('Correct! ' + guess + ' has been found')
        print('Here are the positions were it has been found')
        for index, char in enumerate(host_word):
            if char == guess:
                correct_guesses_out[index] = guess  # Update correct_guesses_out
                print(index + 1)
        return correct_guesses_out, n_pieces_left
    else: # If letter hasn't been guessed and is incorrect draw the corresponding hangman piece and substract one to n_pieces_left
        print('Wrong letter... The host draw a: ' + hangman_parts[n_pieces_left])
        draw_hangman_piece(n_pieces_left, pen)

        return correct_guesses, n_pieces_left - 1 # Update correct n_pieces_left

# Tell players how many letters the host_word has and new blank lines so the other players can't see the answer
for i in range(20):
    print('\n')
print('The host has chosen a word with ' + str(len(host_word)) + ' letters in it')

# Show screen and define "pen"
screen = turtle.Screen()
pen = turtle.RawPen(screen)
pen.hideturtle()

# For 100 times, if there isn't a clear winner or losser continue asking for letters and runnning turns
for i in range(100):
    if not player_won() and not player_lost():
        guess = input('Please type the letter you think is in the hosts word: ')

        # Checks if input is in alphabet and only one character (one letter) for 100 times, the exits if persists
        for ii in range(100):
            if not guess.isalpha() or len(guess) > 1 or len(guess) == 0:
                guess = input('Please remember to only type 1 letter. Not a number, not a phrase, just a letter. Try again! ')
        if not guess.isalpha() or len(guess) > 1 or len(guess) == 0:
            print('Maximum times of tries reached. Exiting now.')
            exit()

        guess_l = guess.lower()
        print(guess_l)

        # Run a turn with the guess and update correct_guesses and n_pieces_left
        correct_guesses, n_pieces_left = turn(guess_l, correct_guesses, n_pieces_left)
    else:
        break

# Print message depending if the player won or host won
if player_lost():
    a = input('Congrats you have lost! Lossing is a part of learning so, don\'t worry, in a way you haven\'t won. But not here lol. You actually lost. lol lol lol')
else:
    print('Incredible! Amazing! Wonderful! Congrats, you actually won! Who would have said it...')