import string
import random

word = []
word.append(random.choices(string.ascii_letters + string.digits, k=4))
print(''.join(word))
