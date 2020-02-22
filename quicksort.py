
list_1 = [5, 9, 7, 2, 8, 1, 6]

[][5][][][][][][][][]
[3][2][1] | | [5][9][7][8][6]

[3] | | [2][1][5][9][7][8][6]
[1][2][3] | |[5][9][7][8][6]
[1][2][3][5][9] | | [7][8][6]
[1][2][3][5][9] | | [7][8][6]


# * Decide on Base Case
# *       Base Case is an empty array
# * Find Pivot Point
# * Partition data to the left and right of the Pivot Point

def partition(data):
    left = []
    right = []
    pivot = data[0]

    for entry in data[1:]:
        if entry < pivot:
            left.append(entry)
        else:  # equals itself
            right.append(entry)

    return left, pivot, right


def quicksort(data):
    if data == []:
        return data
    left, pivot, right = partition(data)

    return quicksort(left) + [pivot] + quicksort(right)
