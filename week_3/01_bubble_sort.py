input = [4, 6, 2, 9, 1]

def bubble_sort(array):
    n = len(array)
    for i in range(n - 1): #n의 길이만큼 반복
        for j in range(n - i - 1): #n의 길이만큽 반복
            if array[j] > array [j+1]:
                array[j], array[j+1] = array[j+1], array[j]
            print(j)
    return

bubble_sort(input)
print(input)