import random
import numpy as np
arr_1 = [random.randint(0, 430000000) for i in range(50000)]
# print(arr_1)
# evaluation_arr = arr_1.sort()


def bubble_sort(arr):
    arr_end = len(arr)-1
    # * Each iteration moves the largest accessible value to the end, so i=2 will move the second largest number to the second-to-last index. That means the end of the loop can decrement after each iteration.
    for i in range(0, arr_end):
        j = 0
        # * The inner loop, in turn, only needs to run while j is less than the latest 'ending' index. This keeps the loop from needing to check the entire array
        while j < arr_end:
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
            j += 1
        arr_end -= 1
        i += 1
    return arr


bubble_sorted_arr = bubble_sort(arr_1)
python_sorted_arr = sorted(arr_1)

print(bubble_sorted_arr)
print(python_sorted_arr)


def compare_arrays(arr1, arr2):
    if len(arr1) != len(arr2):
        print('Arrays must have same lengh.')
    mismatches = 0
    for i in range(0, len(arr1)-1):
        if arr1[i] != arr2[i]:
            mismatches += 1
    if mismatches != 0:
        return False
    else:
        return True


print(compare_arrays(bubble_sorted_arr, python_sorted_arr))

# while sorted_arr is None:
#     pass
# print(sorted_arr)


# print(compare_arrays(sorted_arr, evaluation_arr))
