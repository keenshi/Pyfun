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
    

    print("Aagaye re tumla Hangman ku!")
    print("Che(6) dillan hain. Zyada guess kare to mauti aati!")
    print("Ab khali AANDOO!!")
    
    while(len(word_letters) > 0 and lives > 0):
        print(display_hangman(lives))
        word_list= [letter if letter in used_letters else '_' for letter in word]
        print(' '.join(word_list))
        user_letters=input("Tukka mar ek:").upper()
        
        
        if user_letters in alphabets - used_letters:
            used_letters.add(user_letters)
            print('Guessan mara so:',used_letters)
            if user_letters in word_letters:
                word_letters.remove(user_letters)
                print("Offoo!!")

            else:
                lives-=1
                print(f'Thad teri.. Kya tukke marra re! {lives} dillan bache hain ab khali mak**')
        elif user_letters in used_letters:
            print("Maro so alphabet kitti baar matare re, phir accha maar:")

        else:
            print("Alphabet maro bole re tereku bgn ke. Alphabet maar:")
    
    
    
    if lives == 0:
        print("Are bgn latkadiye na potte ku haram ke. Jahannam me jalte re tumla! Word:",word)
    else:
        print("Abababa!! Sahi tukke mare re tumla. Word:",word)

hangman()
