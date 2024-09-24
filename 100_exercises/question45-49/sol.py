'''
Write a program which can filter even numbers in a list by using filter function. The list is: [1,2,3,4,5,6,7,8,9,10].

Hints:

Use filter() to filter some elements in a list. Use lambda to define anonymous functions.
'''


ori_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
filter_list = list(filter(lambda x: x % 2 == 0, ori_list))
map_list = list(map(lambda x: x ** 2, ori_list))
even_list = [x for x in ori_list if x % 2 == 0]
square_list = [x ** 2 for x in ori_list]

print(f"ori_list = {ori_list}")
print(f"filter_list = {filter_list}")
print(f"map_list = {map_list}")
print(f"even_list = {even_list}")
print(f"square_list = {square_list}")
