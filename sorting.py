from random import randint

#Using pythod sort method
rand_list_nums = []
for x in range(10):
    rand_list_nums.append(randint(1,10))
def sort_list(list_of_nums):
    list_of_nums.sort()
print("___PYTHON SORT___")
print(f"The unsorted list: {rand_list_nums}")
sort_list(rand_list_nums)
print(f"The sorted list: {rand_list_nums}")



#Bubble sort in python
def bubble_sort(list):
    n = len(list)

    for i in range(n):
        # Create a flag that will allow the function to
        # terminate early if there's nothing left to sort
        already_sorted = True

        # Start looking at each item of the list one by one,
        # comparing it with its adjacent value. With each
        # iteration, the portion of the array that you look at
        # shrinks because the remaining items have already been
        # sorted.
        for j in range(n - i - 1):
            if list[j] > list[j + 1]:
                # If the item you're looking at is greater than its
                # adjacent value, then swap them
                list[j], list[j + 1] = list[j + 1], list[j]

                # Since you had to swap two elements,
                # set the `already_sorted` flag to `False` so the
                # algorithm doesn't finish prematurely
                already_sorted = False

        # If there were no swaps during the last iteration,
        # the array is already sorted, and you can terminate
        if already_sorted:
            break

    return list

rand_list_nums.clear()
for x in range(10):
    rand_list_nums.append(randint(1,10))
print("\n___BUBBLE SORT___")
print(f"The unsorted list: {rand_list_nums}")
bubble_sort(rand_list_nums)
print(f"The sorted list: {rand_list_nums}")



#Merge sort in python
def merge(left, right):
    # If the first array is empty, then nothing needs
    # to be merged, and you can return the second array as the result
    if len(left) == 0:
        return right

    # If the second array is empty, then nothing needs
    # to be merged, and you can return the first array as the result
    if len(right) == 0:
        return left

    result = []
    index_left = index_right = 0

    # Now go through both arrays until all the elements
    # make it into the resultant array
    while len(result) < len(left) + len(right):
        # The elements need to be sorted to add them to the
        # resultant array, so you need to decide whether to get
        # the next element from the first or the second array
        if left[index_left] <= right[index_right]:
            result.append(left[index_left])
            index_left += 1
        else:
            result.append(right[index_right])
            index_right += 1

        # If you reach the end of either array, then you can
        # add the remaining elements from the other array to
        # the result and break the loop
        if index_right == len(right):
            result += left[index_left:]
            break

        if index_left == len(left):
            result += right[index_right:]
            break

    return result
def merge_sort(list):
    # If the input array contains fewer than two elements,
    # then return it as the result of the function
    if len(list) < 2:
        return list

    midpoint = len(list) // 2

    # Sort the array by recursively splitting the input
    # into two equal halves, sorting each half and merging them
    # together into the final result
    return merge(
        left=merge_sort(list[:midpoint]),
        right=merge_sort(list[midpoint:]))

rand_list_nums.clear()
for x in range(10):
    rand_list_nums.append(randint(1,10))
print("\n____MERGE SORT____")
print(f"The unsorted list: {rand_list_nums}")
r = merge_sort(rand_list_nums)
print(f"The sorted list: {r}")