def selection_sort(array):
    n = len(array)  # get the length of the array

    for i in range(n-1):  # loop through all elements except the last one
        min_index = i  # assume the current element is the smallest

        # find the smallest element in the remaining unsorted part
        for j in range(i, n):
            if array[j] < array[min_index]:  # if a smaller element is found
                min_index = j  # update the index of the smallest element

        # swap the found smallest element with the first unsorted element
        array[i], array[min_index] = array[min_index], array[i]



# example list
numbers = [12, 4, 54, 3, 1, 6]

print("Before sorting:", numbers)
selection_sort(numbers)
print("After sorting:", numbers)


