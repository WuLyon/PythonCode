# Question: Write a program which can compute the factorial of a given numbers. The results should be printed in a comma-separated sequence on a single line. Suppose the following input is supplied to the program: 8 Then, the output should be: 40320

# Hints: In case of input data being supplied to the question, it should be assumed to be a console input.
import time

def get_factorial(num):
    if num == 0:
        return 1
    else:
        return num * get_factorial(num - 1)

num = input("Please input a number to compute the factorial:")
start_time = time.time()
print(get_factorial(int(num)))
print(f"during: {time.time()-start_time}")
