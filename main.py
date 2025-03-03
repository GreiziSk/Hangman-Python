import random
from word_list import list_of_words

chosen_word = random.choice(list_of_words)
word_length = len(chosen_word)
placeholder = ""
lives = 6

for blank in range(0,word_length):
    placeholder += "_"
print(placeholder)


correct_letter = []
game_over = False
while game_over == False:
    guess = input("which letter will you use :").lower()

    display = ""

    if guess in correct_letter:
        print(f"you have already chosen,{guess}")



    for char in chosen_word:
        if char == guess:
            display += char
            correct_letter.append(char)
        elif char in correct_letter:
            display += char

        else:
            display += "_"

    print(display)

    if guess not in chosen_word:
        lives -= 1
        print(f"{guess} is not in the word,you lost a life remaining:{lives}")
        if lives == 0:
            game_over = True
            print(f"game over the correct word was {chosen_word}")

    if "_" not in display :
        game_over = True
        print("You win")

