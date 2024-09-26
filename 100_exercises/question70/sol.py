# The useage of assert

numbers = [0, 2, 4, 6, 8, 9]


def is_even(nums):
    for num in nums:
        assert num % 2 == 0, f'{num} is not an even number.'
        print(f'{num} is an even number.')


is_even(numbers)
