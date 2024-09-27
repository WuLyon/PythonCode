heads = int(input('heads: '))
feet = int(input('feet: '))

chiken = 2 * heads - feet / 2
rabbit = feet / 2 - heads

if chiken.is_integer() and chiken >= 0 and rabbit.is_integer() and rabbit >= 0:
    print(f'chiken: {int(chiken)}')
    print(f'rabbit: {int(rabbit)}')
else:
    print('No solution! ')
