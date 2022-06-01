def merge_sort(arr):
    if len(arr) > 1:
        mid_p = len(arr)//2
        l_arry = arr[:mid_p]
        r_arry = arr[mid_p:]
        merge_sort(l_arry)
        merge_sort(r_arry)
        merge(arr, l_arry, r_arry)
        

def merge(arr, l_arry, r_arry):
    i,j,k =0,0,0
    while i < len(l_arry) and j < len(r_arry) :
        if l_arry[i] > r_arry[j]:
            arr[k] = r_arry[j]
            j += 1
        elif l_arry[i] < r_arry[j]:
            arr[k] = l_arry[i]
            i += 1
        k += 1
    while i < len(l_arry):
        arr[k] = l_arry[i]
        i += 1
        k += 1    
    while j < len(r_arry):
        arr[k] = r_arry[j]
        j += 1
        k += 1
    
    return arr


data_arry = [8, 7, 2, 1, 0, 9, 6]
merge_sort(data_arry)
print(data_arry)