def find_smallest(arr, start_index):
    if start_index >= len(arr):
        return None, None
    
    #Stores the smallest value
    smallest = arr [start_index]
    #stores the index of the smallest value
    index = start_index

    for i in range (start_index, len(arr)):
        if arr[i] < smallest:
            index = i
            smallest = arr [i]
    return smallest, index

def selection_sort(arr):
    for i in range(len(arr)):
        #finds the smallest element and its index in the array from inndex i
        smallest, smallest_index = find_smallest(arr, i)
        if smallest and smallest_index:
            #swap the smallest element and the first element of the unsorted part
            arr[i], arr[smallest_index] = arr[smallest_index], arr[i]
        return arr

print (selection_sort([5,3,6,2,10]))
print (selection_sort(["banana", "orange", "apple"]))