# arr = [x for x in range(20000)]
arr = [1, 4, 3, 5, 6, 7, 2, 40]


# def insertion_sort(arr):
#     for entry in arr:
#         current_idx = 0
#         sorted = arr[:current_idx]
#         eval_idx = current_idx+1
#         eval_value = arr[eval_idx]


#         # loop through sorted values -- backwards
#         for sorted_entry in sorted:
#             if arr[current_idx] < arr[eval_idx]:
#                 del arr[eval_idx]
#                 sorted.append(eval_value)
#             if arr[current_idx] > arr[eval_idx]:

#         current_idx = current_idx+1


def insertion_sort(arr):
    #  * loop through array in increments of one, starting at index 1 since index 0 is considered sorted
    # max = len(arr)-1
    for current_idx in range(1, len(arr)):
        current_value = arr[current_idx]
        print(f'first, current_value : {current_value}')
        print(f'and current_idx : {current_idx}')
        #  * loop backwards over sorted segment of arr
        eval_idx = current_idx - 1
        # print(
        #     f'checking value {current_value} at index {current_idx} against value {arr[eval_idx]} at index {eval_idx}')
        while eval_idx > 0:
            print(f'eval_idx is {eval_idx}')
            # print(
            #     f'left {arr[eval_idx]} > {current_value}   --- exchanging values')
            print(
                f'arr[e_i] : {arr[eval_idx]} | | | |  arr[c_i] : {arr[current_idx]}')
            if arr[eval_idx] > current_value:
                arr[current_idx] = arr[eval_idx]
                arr[eval_idx] = current_value
                print(f'modified arr is {arr}')
            # arr[eval_idx] = current_value
            eval_idx -= 1
            print('while loop end')
        print('for loop end')
        # for current_sorted_idx in range(current_idx, 0, -1):
        #     # * starting at arr[current_sorted_index] and when arr[current_sorted_index] is less than current_value, insert current_value then delete original current value
        #     if arr[current_sorted_idx] > current_value:

        # i represents the current index *and* describes the sorted index + 1. So, the index of the sorted numbers is [0 : i-1]
        # check if the value of arr[i] is greater than each descending sorted entry


print(insertion_sort(arr))
