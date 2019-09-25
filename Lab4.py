""" Guessing Game """
import random


def guessing_game():
    # generate a random integer from 1 to 1000
    answer = random.randint(1, 1000)
    # your code goes here.
    guessing = int(input('Enter your guess from 1 to 1000: '))
    print(answer)
    min = 0
    max = 1000
    count = 0
    while guessing != answer:
        print(answer, guessing)
        count += 1
        print("Wrong! Guess count: " + str(count))
        if guessing > answer:
            max = guessing - 1
        else:
            min = guessing + 1
        guessing = int(input('Again Enter your guess from ' +
                             str(min) + ' to ' + str(max) + ': '))
    else:
        print("You got it! The hidden number is " + str(answer))


# https://stackoverflow.com/questions/419163/what-does-if-name-main-do
if __name__ == '__main__':
    guessing_game()
