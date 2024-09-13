# Question: Define a class with a generator which can iterate the numbers, which are divisible by 7, between a given range 0 and n.

# Hints: Consider use yield

def getNum(max):
    i = 1
    while i < max:
        if i%7 == 0:
            yield i
        i += 1

for i in getNum(100):
    print(i)