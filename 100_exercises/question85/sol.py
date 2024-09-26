'''
Please write a program to generate all sentences where subject is in ["I", "You"] and verb is in ["Play", "Love"] and the object is in ["Hockey","Football"].

Hints: Use list[index] notation to get a element from a list.
'''


list1 = ['I', 'You']
list2 = ['Play', 'Love']
list3 = ['Hockey', 'Football']
lists = [list1, list2, list3]
sentence = []
for subject in list1:
    sentence.append(subject)
    for verb in list2:
        sentence.append(verb)
        for ob in list3:
            sentence.append(ob)
            print(' '.join(sentence))
            sentence.pop()
        sentence.pop()
    sentence.pop()
