def rotate_matrix(arr, n):
    l,t = 0,0
    r = b = n
    # while l < r and t < b:
    for i in range(l, r-1):
        for j in range(t,b-1):
            print(i,j)
            first = arr[i][j]
            tmp = arr[i][r-1-j]
            arr[i][r-1-j] = first
            scnd_tmp = arr[b-1-i][r-1-j]
            arr[b-1-i][r-1-j] = tmp
            third_tmp = arr[b-1-i][j]
            arr[b-1-i][j] = scnd_tmp
            arr[i][j] = third_tmp

    return arr


arr = [[1,2,3],[4,5,6],[7,8,9]]
arr_len = len(arr)
print(rotate_matrix(arr, arr_len))
