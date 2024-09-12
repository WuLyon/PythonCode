# Question: Write a program that computes the value of a+aa+aaa+aaaa with a given digit as the value of a. 
# Suppose the following input is supplied to the program: 9 Then, the output should be: 11106

# Hints: In case of input data being supplied to the question, it should be assumed to be a console input.
a = int(input("input the a: "))

sum = 0
temp = 0

for _ in range(4):
    temp = temp * 10 + a
    sum += temp

print(sum)