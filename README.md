![Ironhack logo](https://i.imgur.com/1QgrNNw.png)

# Weekly Project 1 - Code a game!

## Rules of Hangman

The rules of Hangman are very simple. The "host player chooses a word and the other players have to guess letters until they know what word it is. For each wrong guess one mark has to be drawn. If all the marks of the Hangman have been drawn before the word has been guessed, the host wins. If the word is guessed before this happens, the player that guessed the word wins.

To make this program simpler version 1.0 will work only with one letter instead of one word.

## Features
- The "Host" player will be able to introduce a letter of his/her choice.
- The program will be able to ask players for letters until either a player has figured out what word it was or they have lost the game because all the marks have been "drawn".
- The program has to be able to inform the player how the game is going until it finishes.

## Ideas for future versions
- The host can input words. (Done)
- The host can input phrases.
- The host can be the machine. (Done)
- The players can input number of players and names, and this info is used to give context.
- There is a version for kids.
- The machine draws the hangman instead of giving the info written. (Done)
- The players can use speech recognition as an input.
- Check for existence of word in the dictionary.


## Variables
- host_word: Stores a string with the word/letter/phrase choseen by the host

- n_pieces_left: Stores the number of tries left before the players loose and the host wins. It will always starts at 7.

- correct_guesses: Stores a list that contains all the letters that have been already succsesfully guessed. It's length is the same is host_word.

- english_words: Stores a list of easy english words for the computer to chose from.

- hangman_parts: Stores a dictionary that as keys has numbers from 7 to 1 and as values the part the hangman loses for each stage of the game.

- screen: The turtle library screen.

- pen: The turtle library pen.

## Functions
- turn(guess, correct_guess, n_pieces_left): It inputs a letter choosen by a player. If the letter has already been discovered it asks again for a letter. If it hasn't been discovered yet and it is a correct guess, it saves the letter in it's corresponding index in correct_guesses (if no letters to dicover the player has won). If the letter is a wrong guess, it draws the corresponding hangman part (if no parts left the player has lost). It returns an updated correct_guess list and and updated n_pieces_left.

- player_lost(): If there aren't more hangman parts to draw return True. Else return False.

- player_won(): If there aren't more letters to discover return True. Else return False.

- draw_hangman_pieces(piece, pen): It draws a the corresponding hangman part.
