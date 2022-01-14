import random
import string
from words import food_list
from stages import display_hangman

def word_random():
    word=random.choice(food_list)
    return word.upper()

def hangman():
    word=word_random()
    word_letters=set(word)
    alphabets=set(string.ascii_uppercase)
    used_letters=set()
    lives = 6
    

    print("Welcome to Hangman!!")
    print("You get to have 6 lives. Good luck!")
    
    
    while(len(word_letters) > 0 and lives > 0):
        print(display_hangman(lives))
        word_list= [letter if letter in used_letters else '_' for letter in word]
        print(' '.join(word_list))
        user_letters=input("Please give a valid input:").upper()
        
        
        if user_letters in alphabets - used_letters:
            used_letters.add(user_letters)
            print('Letters already guessed:',used_letters)
            if user_letters in word_letters:
                word_letters.remove(user_letters)

            else:
                lives-=1
                print(f'Oops! The letter is not in the word. You have {lives} lives left.')
        elif user_letters in used_letters:
            print("Alphabet already entered. Please try again!")

        else:
            print("Invalid input. Please try again!")
    
    
    
    if lives == 0:
        print("Sorry you died! The word was:",word)
    else:
        print("Congo! You have guessed the word. It was:",word)

hangman()
