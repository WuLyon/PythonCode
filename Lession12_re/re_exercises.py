import re
emails = ['test.email@example.com', 'invalid-email', 'user@domain.org', 'user@domain']

format = r'^[\w\._-]+@\w+\.\w{2,}$'
result = []
for email in emails:
    if re.match(format, email):
        result.append(email)
    
print('\n'.join(result))
