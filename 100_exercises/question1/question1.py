def is_theNum(num):
    if num%7 == 0 and num%5 != 0:
        return True
    else:
        return False

for i in range(2000, 3201):
    if is_theNum(i):
        print(i, end=',')
