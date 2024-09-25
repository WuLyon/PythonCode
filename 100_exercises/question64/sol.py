def get_result(n):
    sum = 0
    expentation_list = []
    for i in range(1, n+1):
        expentation_list.append(f'{str(i)}/{str(i+1)}')
        i = float(i)
        sum += i / (i+1)
    expentation = ' + '.join(expentation_list)
    print(f'{expentation} = {sum}')


get_result(3)
