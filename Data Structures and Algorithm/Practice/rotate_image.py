def rotate_matrix(arr, n):

    # traonspose matrix
    for i in range(0, n):
        for j in range(0,n):
            if j<=i:
                arr[i][j], arr[j][i] = arr[j][i], arr[i][j]
            
    for i in range(0,n):
        for j in range(0,n//2):
            arr[i][j],arr[i][n-1-j] = arr[i][n-j-1],arr[i][j] 
    print(arr)

arr = [[1,2,3],[4,5,6],[7,8,9]]
arr_len = len(arr)
rotate_matrix(arr, arr_len)
