#!/usr/bin/python3
def fizzbuzz():
    for m in range(1, 101):
        number = ""
        if m % 15 == 0:
            number = "FizzBuzz"
        elif m % 5 == 0:
            number = "Buzz"
        elif m % 3 == 0:
            number = "Fizz"
        print(number, end=" ") if number else print(m, end=" ")
