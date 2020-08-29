

def selection_sort(arr):
    for i in range(len(arr)-1, 0, -1):
        minElement = 0
        for k in range(1, i+1):
            if arr[k] > arr[minElement]:
                minElement = k

        temp = arr[i]
        arr[i] = arr[minElement]
        arr[minElement] = temp


arr = [5,3,2,7,1]
selection_sort(arr)
print(arr)