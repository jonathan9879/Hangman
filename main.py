while True:
    # Host word variable and number of hangman pieces left variable
    host_word = input('Roses are red, Violets are blue... What are you!? Where are you!?\nAs the master player \"Host\" you will have the important task of choosing the letter that the players will have to guess! Now choose a letter: ')
    n_pieces_left = 7

    #Easter eggs
    if host_word in ['penguin', 'Penguin', 'human', 'Human', 'ironhack', 'Ironhack']:
        print('Congrats! You have found the hidden easter egg! You are awesome!')
        #  Choose to exit or restart the program
        exit_option = input('What would you like to do next? To try again, type AGAIN. To exit, type EXIT. ')
        while exit_option not in ['AGAIN', 'EXIT']:
            exit_option = input('Please only type the word AGAIN or the word EXIT all in capital letters: ')
        if exit_option == 'AGAIN':
            continue
        else:
            break

    # Checks if input is in alphabet and only one character (one letter)
    while (not host_word.isalpha()) or len(host_word) > 1 or len(host_word) == 0:
        host_word = input('Please rember to only type 1 letter. Not a number, not a phrase, just a letter. Try again! ')

    # Correct guesses variable
    correct_guesses = [None] * len(host_word)

    # Dictionary for pieces of hangman
    hangman_parts = {7: 'upside down L', 6: 'head', 5: 'body', 4: 'arm', 3: 'arm', 2: 'leg', 1: 'leg', 0: 'death'}

    # Function that outputs True if the player has lost
    def player_lost():
        if n_pieces_left > 0:
            return False
        else:
            return True

    # Function that outputs True if the player has won
    def player_won():
        if None in correct_guesses:
            return False
        else:
            return True

    # Function that processes a turn and return a different number of hangman parts if it has to be changed and correct_guesses changes
    def turn(guess, correct_guesses, n_pieces_left):
        # Variables to do updates
        correct_guesses_out = correct_guesses

        if guess in correct_guesses: # If letter has already been guessed ask for a new letter
            while guess in correct_guesses:
                guess = print('This letter has already been guessed! Please type a new one :) ')
        if guess in host_word: # If letter hasn't been guessed and is correct save it in the correct index in correct_guesses
            for index, char in enumerate(host_word):
                if char == guess:
                    correct_guesses_out[index] = guess # Update correct_guesses_out
            return correct_guesses_out, n_pieces_left
        else: # If letter hasn't been guessed and is incorrect draw the corresponding hangman piece and substract one to n_pieces_left
            print('The host draws a: ' + hangman_parts[n_pieces_left])
            return correct_guesses, n_pieces_left - 1 # Update correct n_pieces_left

    # Tell players how many letters the host_word has
    print('The host has chosen a word with ' + str(len(host_word)) + ' letters in it')

    # While there isn't a clear winner or losser continue asking for letters and runnning turns
    while(not player_won() and not player_lost()):
        guess = input('Please type the letter you think is in the hosts word: ')

        # Checks if input is in alphabet and only one character (one letter)
        while (not guess.isalpha()) or len(guess) > 1 or len(guess) == 0:
            host_word = input('Please rember to only type 1 letter. Not a number, not a phrase, just a letter. Try again! ')

        # Run a turn with the guess and update correct_guesses and n_pieces_left
        correct_guesses, n_pieces_left = turn(guess, correct_guesses, n_pieces_left)

    # Print message depending if the player won or host won
    if player_lost():
        print('Congrats you have lost! Lossing is a part of learning so, don\'t worry, in a way you haven\'t won. But not here lol. You actually lost. lol lol lol')
    else:
        print('Incredible! Amazing! Wonderful! Congrats, you actually won! Who would have said it...')

    # Choose to exit or restart the program
    exit_option = input('What would you like to do next? To try again, type AGAIN. To exit, type EXIT')
    while exit_option not in ['AGAIN', 'EXIT']:
        exit_option = input('Please only type the word AGAIN or the word EXIT all in capital letters: ')
    if exit_option == 'AGAIN':
        continue
    else:
        break