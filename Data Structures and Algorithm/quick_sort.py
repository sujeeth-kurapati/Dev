def quickSort(arr, start,end):
    if start < end:
        pi = partition(arr, start, end)
        quickSort(arr, start, pi-1)
        quickSort(arr, pi+1, end)

def partition(arr, start, end):
    pivt = arr[end]
    pp = start
    for loop_item in range(start,end):
        if arr[loop_item] <= pivt:
            arr[loop_item], arr[pp] = arr[pp], arr[loop_item]
            pp += 1
    arr[end], arr[pp] = arr[pp], arr[end]
    
    return pp
            
data = [1,2,2,3,3,3,4]
print("Unsorted Array")
print(data)

size = len(data)

quickSort(data, 0, size - 1)

print('Sorted Array in Ascending Order:')
print(data) 