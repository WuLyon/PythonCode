def get_expen(n):
    if n == 1:
        return '1'
    else:
        expen = f'{str(n)} + {get_expen(n-1)}'
        return expen


def get_sum(n):
    if n == 1:
        return 1
    else:
        sum = n + get_sum(n-1)
        return sum


def display(n):
    print(f'{get_expen(n)} = {get_sum(n)}')


display(5)
