def is_even(n):
    for i in range(0, n+1):
        if i % 2 == 0:
            yield str(i)
        i += 1


num_list = []
for i in is_even(10):
    num_list.append(i)
print(','.join(num_list))
