import math
import random


ATK = 100
t = 1
rio = 1.1

def count(hp, atk):
    if hp % atk == 0:
        return int(hp // atk)
    else:
        return int(hp // atk + 1)

def compare(t1, t2):
    if t1 < t2:
        return 1
    elif t1 > t2:
        return 2
    else:
        return 0


def calculate():
    HP = random.uniform(0, 880)
    # HP = 30.02 * ATK


    print(f'hp: {HP}')

    atk1 = rio * ATK
    atk2 = ATK
    n1 = count(HP, atk1)
    n2 = count(HP, atk2)

    T1 = n1 * t
    T2 = n2 * t / rio

    # print(f'n1: {n1}')
    # print(f'n2: {n2}')
    # print(f'T1: {T1}')
    # print(f'T2: {T2}')

    if compare(T1, T2) == 1:
        print(f'1 win')
        return 1
    elif compare(T1, T2) == 2:
        print(f'2 win')
        return 2
    else:
        print(f'draw')
        return 0


def sum():
    win_1 = 0
    win_2 = 0
    for i in range(1100):
        calculate()
        if calculate() == 1:
            win_1 += 1
        elif calculate() == 2:
            win_2 += 1
    print(f'win_1: {win_1}')
    print(f'win_2: {win_2}')

    if win_1 > win_2:
        print("win_1")
    elif win_1 < win_2:
        print("win_2")
    else:
        print("draw")
def main():
    sum()
    # print(calculate())

if __name__ == '__main__':
    main()