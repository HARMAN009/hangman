import random

with open('newfolder.txt', 'r')as f:
    words = f.readlines()

word = random.choice(words)[:-1]

total_errors = 7
guesses = []
done = False

while not done:
    for letter in word:
        if letter.lower() in guesses:
            print(letter, end="")
        else:
            print("_", end="")
    print("")

    guess = input(f"errors remaining {total_errors}, next guess: ")
    guesses.append(guess.lower())
    if guess.lower() not in word.lower():
        total_errors -= 1
        if total_errors == 0:
            break

    done = True
    for letter in word:
        if letter not in guesses:
            done = False

if done:
    print(f"Yayy you found the word!!")
else:
    print(f"game over!! the word was {word}.")
