def bubble_sort(arr):
    n = len(arr)

    permutation = True
    while permutation:
        permutation = False
        for i in range(n - 1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                permutation = True


array = [
    2,
    3,
    5,
    7,
    62,
    21,
    3,
]
bubble_sort(array)
print(array)
