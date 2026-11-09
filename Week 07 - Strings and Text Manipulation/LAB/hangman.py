import random

word_list = ["peach", "table", "house", "car", "dog"]

chosen_word = random.choice(word_list)

display = []

for letter in chosen_word:
    display.append("_")

print(" ".join(display))

while "_" in display:
    guess = input("Guess a letter: ").lower()

    for position in range(len(chosen_word)):
        if chosen_word[position] == guess:
            display[position] = guess
    
        print(" ".join(display))

print("You win!")