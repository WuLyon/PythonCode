# Question: Write a program that accepts a sentence and calculate the number of letters and digits. 
# Suppose the following input is supplied to the program: hello world! 123 Then, the output should be: LETTERS 10 DIGITS 3

# Hints: In case of input data being supplied to the question, it should be assumed to be a console input.
s = input()
d = {"digit": 0, "alpha": 0}
for c in s:
    if c.isdigit():
        d["digit"] += 1
    elif c.isalpha():
        d["alpha"] += 1
    else:
        pass

print(f"LETTERS {d['alpha']} DIGITS {d['digit']}")