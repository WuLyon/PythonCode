string = 'asldfjnvaskdjfalsdjfnasdkjf'
dic = {}
for char in string:
    dic[char] = dic.get(char, 0) + 1

print('\t'.join([f'{key}, {value}' for key, value in dic.items()]))
