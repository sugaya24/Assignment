""" Guessing Game """
import random


def guessing_game():
    # generate a random integer from 1 to 1000
    answer = random.randint(1, 1000)
    # your code goes here.
    min = 0
    max = 1000
    count = 0
    while True:
        # print(answer)
        while True:
            try:
                guessing = int(input('Enter your guess from ' +
                                     str(min) + ' to ' + str(max) + ': '))
                break
            except ValueError as e:
                print(f"Invalid input: {e}")
                print("Invalid input. Please enter a number!")
            except KeyboardInterrupt:
                print("\nNo input taken.\n")
                break
            except ZeroDivisionError as e:
                print(f"Invalid input: {e}")
            except EOFError as e:
                print(f"Invalid input: {e}")

        count += 1
        if guessing == answer:
            print("You got it! The hidden number is " + str(answer))
            print("It took you " + str(count) + " guess(es)!")
            break
        else:
            print('Wrong! Guess count: ' + str(count))

        if guessing < answer and guessing >= min:
            min = guessing + 1
        elif guessing > answer and guessing <= max:
            max = guessing - 1


# https://stackoverflow.com/questions/419163/what-does-if-name-main-do
if __name__ == '__main__':
    guessing_game()
