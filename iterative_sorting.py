# import sys

# sys.setrecursionlimit(10**4)

arr = [x for x in range(20000)]
# print(arr)


def binary_search(arr, target):
    # middle = (len(arr)-1)//2
    min = 0
    max = len(arr)-1
    # *  Edge case in which arr is empty
    if len(arr) == 0:
        return None
    while min <= max:
        mid = (min+max) // 2
        guess = arr[mid]
        # print(f'starting middle, {middle}')
        if guess == target:
            return guess
        if guess > target:
            max = mid - 1
            print(f'mid > target {mid}')
        if guess < target:
            min = mid + 1
            print(f'mid < target {mid}')


# print(binary_search(arr, 1234))


# Recursive approach

def recursive_bin_search(arr, target, min=0, max=len(arr)-1):
    mid = (min+max) // 2
    guess = arr[mid]
    if guess > target:
        max = mid - 1
    if guess < target:
        min = mid + 1
    if guess == target:
        return mid
    return recursive_bin_search(arr, target, min, max)


print(recursive_bin_search(arr, 15))
