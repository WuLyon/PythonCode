import re

user_email = 'wuliyanglyon@gmail.com'
format = r'(\w+)@\w+.com'
print(re.match(format, user_email).group(1))
