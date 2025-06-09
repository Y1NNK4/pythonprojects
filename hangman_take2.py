import random
from hangmanwordbank import *
from hangman import logo

player_guess = []
lives = 6 

def chosen_word():
    return random.choice(words) 

def mystery_word(word):
    return " ".join(["_" if letter not in player_guess else letter for letter in word])

def word_check(guess,chosen_word):
        global lives
        if guess in player_guess:
            print("Letter already in guessed, try again!")
        elif guess in chosen_word:
            player_guess.append(guess)
            print("Nice, Input your next letter.")
        
        else:
            lives -= 1
            print("Word guess! Lives remaining:", lives)

def art():
    print(HANGMANPICS[6 - lives])

                
def Hangman():
    print("Welcome to Hangman")
    print(logo)

word_to_guess = chosen_word()
while lives > 0 and "_" in mystery_word(word_to_guess):
    Hangman()
    print("Current Word:", mystery_word(word_to_guess))
    guess = input("Enter your letter --->").lower()
    word_check(guess,word_to_guess)
    art()
if set(player_guess) == set(chosen_word()):
        print("Congratulations! You guessed the word:", word_to_guess)
else:
        print("Game over. The word was:", word_to_guess)






        
            

