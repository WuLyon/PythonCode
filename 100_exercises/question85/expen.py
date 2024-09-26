'''
Please write a program to generate all sentences where subject is in ["I", "You"] and verb is in ["Play", "Love"] and the object is in ["Hockey","Football"].

Hints: Use list[index] notation to get a element from a list.
'''


from random import choice
list1 = ['I', 'You']
list2 = ['Play', 'Love']
list3 = ['Hockey', 'Football']
lists = [list1, list2, list3]
sentence = []
for aList in lists:
    sentence.append(choice(aList))

print(' '.join(sentence))
