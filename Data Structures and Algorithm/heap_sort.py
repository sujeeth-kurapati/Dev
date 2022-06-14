def heap_sort(arry, p):
    if 2*p+1 <= len(arry) - 1:
        l_c = 2*p+1 
        r_c = 2*p+2 if 2*p+2 <= len(arry) - 1 else None

        if r_c is not None and l_c is  not None:
            if arry[l_c] > arry[r_c]:
                largest = l_c
            else:
                largest = r_c
        elif l_c:
            largest = l_c
        elif r_c:
            largest = r_c

        if arry[p] < arry[largest]:
            arry[p], arry[largest] = arry[largest], arry[p]
            heap_sort(arry, largest)

def heapify(arr):
    n = (len(arr)-2)//2
    for prnt_index in range(n, -1, -1):
        print(prnt_index)
        heap_sort(arr, prnt_index)
    return arr

arr = heapify([5,16,8,14,20,1,26])
print(arr)