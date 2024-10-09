# import re
from random import sample
from random import choice
import time

OPERATORS = ['+', '-', '*', '/']
NUMBERS = range(100)


def gen_divisor(num):
    """
    Generate a divisor.
    """
    divisors = []
    for i in range(2, 100):
        if num % i == 0 and i != num:
            divisors.append(i)
    if not divisors:
        return 1
    return choice(divisors)


def gen_expression():
    """
    Generate a mathematical expression and ensure division by zero is avoided.
    """
    operator = choice(OPERATORS)
    if operator != '/':
        num1, num2 = sample(NUMBERS, 2)
    else:
        num1 = choice(NUMBERS)
        num2 = gen_divisor(num1)

    return f'{num1} {operator} {num2}'


def run(duration=60):
    """
    Evaluate the number of expressions completed by user
    and accuracy whitin specified time.
    """
    start_time = time.time()
    count = right = wrong = 0
    while time.time() - start_time <= duration:
        expression = gen_expression()
        result = eval(expression)
        print(expression + ' =')
        try:
            user_input = float(input())
            # pattern = r'(\d+)\s*[\+\-\*\/]\s*\d+'
            # user_input = int(re.match(pattern, expression).group(1))
        except ValueError:
            print('Need to input as numbers')
        count += 1
        if user_input == result:
            right += 1
            print('Right!')
        else:
            wrong += 1
            print(f'Wrong! The correct result is {result}')
        print(f'Remain {int(duration - (time.time() - start_time))}s')

    print(f'You have finished {count} expression!')
    print(
        f'{right} are right, and {wrong} are wrong!\
 The accuracy is {(right / count) * 100: .2f}%'
    )


if __name__ == '__main__':
    run()
