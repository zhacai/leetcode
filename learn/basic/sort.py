arr = [1,3,4,5,2,3,2,67,75,7,2,4,3,67,58,18,38,68,66,88]

# bubble sort
def bubble_sort(arr):
    n = len(arr) 
    for i in range(n):
        for j in range(1,n-i):
            if  arr[j-1] > arr[j] : 
                arr[j-1],arr[j] = arr[j],arr[j-1] 
    return arr

# print bubble_sort(arr)

# selection sort 
def selection_sort(arr):
    n = len(arr)

    for i in range(n):
        min_index = i

        for j in range(i, n):
            if arr[j] < arr[min_index]:
                min_index = j

        arr[min_index],arr[i] = arr[i],arr[min_index]
        
    return arr

#print selection_sort(arr)
