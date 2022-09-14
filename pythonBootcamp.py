words= ["tester","word"]
import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']



selected_word = random.choice(words)
print(f'secilen kelime = {selected_word}')
display = []
for _ in selected_word:
    display += "_"

lives = 6
print(display)
end_of_game = False
word_lenght = len(selected_word)

while not end_of_game:
    guess = input("bir kelime giriniz: ")
    
    
    for pozition in range(word_lenght):
        letter = selected_word[pozition]
        if letter == guess:
            display[pozition] = letter
        
    print(display)

    if guess not in selected_word:
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("u lose.")

            
    else:
        print(f'kalan hakkiniz {lives}')

    if "_" not in display:
        end_of_game = True
        print("end of game kongracıleşıns")
    
    print(stages[lives])

