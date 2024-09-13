sum = 0
while True:
    s = input()
    if not s:
        break
    log = s.split(' ')
    if log[0] == 'D':
        sum += int(log[1])
    elif log[0] == 'W':
        sum -= int(log[1])
    else:
        print("Wrong log!")

print(sum)