#!/usr/bin/python3
def fizzbuzz():
    for item in range(1, 101):
        if item % 3 == 0 and item % 5 == 0:
            print('FizzBuzz ', end="")
        elif item % 5 == 0 and 3 != 0:
            if item != 100:
                print('Buzz ', end="")
            else:
                print('Buzz', end="")
        elif item % 3 == 0 and 5 != 0:
            print('Fizz ', end="")
        else:
            print(item, end=" ")
