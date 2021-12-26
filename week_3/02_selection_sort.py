input = [4, 6, 2, 9 ,1]

def selection_sort(array):
    n = len(array)

    for i in range(n - 1):  # i=0, #O(N^2)
        min_index = i
        for j in range(n - i):  # j=0 #O(N^2)
            if array[i+j] < array[min_index]:
                min_index = i+j
        array[i], array[min_index] = array[min_index], array[i]
    return

selection_sort(input)
print(input)
