# Question: Write a program, which will find all such numbers between 1000 and 3000 (both included) such that each digit of the number is an even number. 
# The numbers obtained should be printed in a comma-separated sequence on a single line.

# Hints: In case of input data being supplied to the question, it should be assumed to be a console input.

res = []
for num in range(1000, 3001):
    s = str(num)
    if int(s[0])%2 == 0 and int(s[1])%2 == 0 and int(s[2])%2 == 0 and int(s[3])%2 == 0:
        res.append(s)
    
print(','.join(res))