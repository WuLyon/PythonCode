from math import floor

def bin_search(numbers, element):
    top = len(numbers) - 1
    bottom = 0
    index = -1

    while top >= bottom:
        mid = int(floor((top + bottom) / 2))
        if numbers[mid] == element:
            index = mid
            print(index)
            return index
        elif numbers[mid] > element:
            top = mid - 1
        else:
            bottom = mid + 1

    print('There is no this element in the list!')


numbers = [1, 3, 5, 6, 8, 10, 14, 18, 21, 24, 26, 30]
print(numbers)
element = int(input('Please input the number which you want to search: '))
bin_search(numbers, element)
