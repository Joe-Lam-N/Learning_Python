# Author Block: 
#     " I am writing this after I finished it. I tried to make everything i needed to repeat into a function. There was one thing that was repeated that I couldn't make into a function because 
#       I needed to change some variable inside main. Thinking back if I made a class of gameinfo, I could have done it and made the code a little bit easier to read and disect"


import os
import random


def pick_word():
    word_list = open("HangMan5LettersWords.txt","r")
    if not word_list.readable():
        print("Unable to open word file")
        exit()
    list_size = len(word_list.readlines())
    random_number = random.randrange(list_size)
    word_list.close()
    word_list = open("HangMan5LettersWords.txt","r")
    word = word_list.readlines()[random_number]
    word_list.close()
    return(word)
def drawhangman(stage):
    if stage == 1:
        print("-----------")
        print("|")
        print("|")
        print("|")
        print("|")
        print("------------")
    if stage == 2:
        print("-----------")
        print("|         O")
        print("|")
        print("|")
        print("|")
        print("------------")
    if stage == 3:
        print("-----------")
        print("|         O")
        print("|         |")
        print("|")
        print("|")
        print("------------")
    if stage == 4:
        print("-----------")
        print("|         O")
        print("|         |")
        print("|        /")
        print("|")
        print("------------")
    if stage == 5:
        print("-----------")
        print("|         O")
        print("|         |")
        print("|        / \\")
        print("|")
        print("------------")
    if stage == 6:
        print("-----------")
        print("|         O")
        print("|        /|")
        print("|        / \\")
        print("|")
        print("------------")
    if stage == 7:
        print("-----------")
        print("|         O")
        print("|        /|\\")
        print("|        / \\")
        print("|")
        print("------------")
def startmenu():
    start_game = " "
    while not (start_game in "yn"):
        start_game=input("Would you like to play? Y/N: ")
        start_game.lower()
        if start_game == "":
            start_game= "l"
        os.system('cls||clear')
    if(start_game == "n"):
        print("Good Bye")
        exit()
def startagain():
    start_game = " "
    while not (start_game in "yn"):
        start_game=input("Would you like to play again? Y/N: ")
        start_game.lower()
        if start_game == "":
            start_game= "l"
    os.system('cls||clear')
    if(start_game == "n"):
        print("Good Bye")
        exit()


alpha = ["q","w","e","r","t","y","u","i","o","p","a","s","d","f","g","h","j","k","l","z","x","c","v","b","n","m",]
guess_words = ["_","_","_","_","_"]
guess_letters = []
game_active = True
sercet_word = pick_word()
stage = 1


startmenu()
while True:
    drawhangman(stage)
    current_guess= input("Guess the word or letter: ")
    current_guess.lower()
    os.system('cls||clear')
    #checking for letter match
    if current_guess in alpha:
        if current_guess in guess_letters:
            print("You already guessed this letter, try again")
        elif current_guess in sercet_word:
            index = sercet_word.index(current_guess)
            guess_words[index] = current_guess
            guess_letters.append(current_guess)
            repeated = sercet_word.count(current_guess)
            while repeated != 1:
                index = sercet_word.index(current_guess,index+1)
                guess_words[index] = current_guess
                repeated -= 1         
        else:
            # you guess incorrectly
            guess_letters.append(current_guess)
            stage +=1
    # For when you guess the whole word
    elif (len(current_guess)==5):
        if current_guess in sercet_word:
            print("You guessed it")
            print("The word was: " + sercet_word)
            startagain()
            sercet_word = pick_word()
            stage = 1
            guess_words = ["_","_","_","_","_"]
            guess_letters = [""]
        else:
            print("Your Guess was wrong")
            stage += 1
    # If max guess is reached
    if (stage == 8):
        print("You Lost")
        print("The word was: "+sercet_word)
        startagain()
        sercet_word = pick_word()
        stage = 1
        guess_words = ["_","_","_","_","_"]
        guess_letters = [""]
    # If all letters are guess right
    if "".join(guess_words) in sercet_word:
        print("You did it, the word was: " + sercet_word)
        startagain()
        sercet_word = pick_word()
        stage = 1
        guess_words = ["_","_","_","_","_"]
        guess_letters = [""]
    print("The word is: "+"".join(guess_words))
    print("Guess Letters: "+ str(guess_letters))


