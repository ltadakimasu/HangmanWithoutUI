import random
from hangman_art import logo,stages
from hangman_words import word_list

print(logo)

selected_word = random.choice(word_list)
print(f'Psssh selected word is {selected_word}')

display = []
for _ in selected_word:
    display += "_"
print(display)

word_lengt = len(selected_word)
lives = 6
end_of_game = False
while not end_of_game:
    guess = input("Enter a letter: ")


    for pozition in range(word_lengt):
        letter = selected_word[pozition]
        if letter == guess:
            display[pozition] = letter
            
    print(display)
    if "_" not in display:
        print("tebrikler kanka")

    if guess not in selected_word:
        lives -= 1
        print(f'u have only {lives} lives. More carefully.')
        if lives == 0:
            print("u lose, die")
            end_of_game = True
    print(stages[lives])