# Question: A website requires the users to input username and password to register. Write a program to check the validity of password input by users. Following are the criteria for checking the password:

#     At least 1 letter between [a-z]
#     At least 1 number between [0-9]
#     At least 1 letter between [A-Z]
#     At least 1 character from [$#@]
#     Minimum length of transaction password: 6
#     Maximum length of transaction password: 12 
#     Your program should accept a sequence of comma separated passwords and will check them according to the above criteria. 
#     Passwords that match the criteria are to be printed, each separated by a comma. 
#     Example If the following passwords are given as input to the program: ABd1234@1,a F1#,2w3E*,2We3345 Then, the output of the program should be: ABd1234@1

# Hints: In case of input data being supplied to the question, it should be assumed to be a console input.
import re

def isPassword(s):
    if len(s) <= 6 or len(s) >= 12:
        return False
    if not re.search('[a-z]', s):
        return False
    if not re.search('[A-Z]', s):
        return False
    if not re.search('[0-9]', s):
        return False
    if not re.search('[$#@]', s):
        return False

    return True

s_list = input().split(',')
password = []
for s in s_list:
    if isPassword(s):
        password.append(s)
print(','.join(password))