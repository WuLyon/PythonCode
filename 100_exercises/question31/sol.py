'''
Define a function that can accept two strings as input and print the string with maximum length in console. If two strings have the same length, then the function should print al l strings line by line.

Hints:

Use len() function to get the length of a string
'''
s = input().split(' ')
if len(s[0]) > len(s[1]):
    print(s[0])
elif len(s[0]) < len(s[1]):
    print(s[1])
else:
    for item in s:
        print(item)

