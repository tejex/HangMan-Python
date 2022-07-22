import random
from logo import logo
from stages import stages
from words import word_list
print(f"Welcome to {logo}")
chosen_word = random.choice(word_list)
display = []
for char in range(len(chosen_word)):
  display += "_"
print(display)
end_of_game = False 
lives = 6 
while not end_of_game:
  guess = input("Guess a letter bro: ").lower()
  for position in range(len(chosen_word)):
    if chosen_word[position] == guess:
      display[position] = guess
    if guess in display:
      print("you already guessed that word")
  if guess not in chosen_word:
    lives -= 1
    print(f"The letter {guess} is not in this word, you lose a life")
  print(stages[lives])
  print(display)
  if "_" not in display:
    end_of_game = True
    print("you win")
  if lives == 0:
    end_of_game = True
    print(stages[0])
    print("you lose")
  
