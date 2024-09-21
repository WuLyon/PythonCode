'''
Define a function that can accept an integer number as input and print the "It is an even number" if the number is even, otherwise print "It is an odd number".

Hints:

Use % operator to check if a number is even or odd.
'''


def isEvenOrOdd(num):
    if num % 2 == 0:
        print(f'{num} is even.')
    else:
        print(f'{num} is odd.')


num = input('Please input a num: ')
isEvenOrOdd(int(num))
