import random
arr = [4, 3, 1, 2, 6, 5]
# TO-DO: Complete the selection_sort() function below


# def selection_sort(arr):
#     # loop through n-1 elements
#     for i in range(0, len(arr) - 1):
#         cur_index = i
#         smallest_index = cur_index

#         # TO-DO: find next smallest element
#         # (hint, can do in 3 loc)
#         # j = cur_index + 1

#         # while j < len(arr)-1:
#         #     print(f'j = {j} value = {arr[j]}')
#         #     if arr[cur_index] > arr[j]:
#         #         smallest_index = j
#         #         print(
#         #             f'arr[c_i] > arr[j] -- new smallest_index = {smallest_index}')
#         #     if arr[j] < arr[smallest_index]:
#         #         smallest_index = j
#         #         print(
#         #             f'arr[cur_index] > arr[j] and arr[j] < arr[smallest_index] -- new smallest_index={smallest_index}')
#         #     j += 1

#         # TO-DO: swap
#         # current_value = arr[cur_index]
#         # smallest_value = arr[smallest_index]
#         # arr[cur_index] = smallest_index
#         # arr[smallest_index] = current_value
#         i += 1
#     return arr

# TO-DO: Complete the selection_sort() function below
# def selection_sort(arr):
#     # loop through n-1 elements
#     for i in range(0, len(arr) - 1):
#         cur_index = i
#         smallest_index = cur_index
#         print(f'outer loop -- smallest_index = {smallest_index}')
#         # TO-DO: find next smallest element
#         # (hint, can do in 3 loc)
#         for j in range(i+1, len(arr)-1):
#             print(f'inner loop | j = {j} || arr[j] = {arr[j]}')
#             if arr[j] < arr[i] and arr[j] < arr[smallest_index]:
#                 print(
#                     f'{arr[j]} is less than {arr[i]} and is also less than {arr[smallest_index]}')
#                 smallest_index = j
#                 smallest_val = arr[smallest_index]
#                 swap_val = arr[cur_index]
#                 arr[cur_index] = smallest_val
#                 arr[smallest_index] = swap_val
#             j += 1

#         # TO-DO: swap

#     return arr


# print(selection_sort(arr))

arr_2 = [17, 14, 7, 11, 3, 9, 8, 4, 6]

random_arr = [random.randint(1, 25000) for _ in range(25000)]


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


# print(bubble_sort(arr))
# print(bubble_sort(arr_2))
print(bubble_sort(random_arr))
