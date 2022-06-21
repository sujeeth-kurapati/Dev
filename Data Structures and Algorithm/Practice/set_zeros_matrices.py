def set_zeros(arr, m ,n):
    firstrow = False
    # Looping through matrix to find the zeros and updating respective rows and clolumns
    for i in range(0,m):
        for j in range(0,n):
            if arr[i][j] == 0:
                if i == 0 and arr[0][0] == 0:
                    firstrow = True
                arr[i][0] = 0
                arr[0][j] = 0
                
    # column updater
    # for j in range(0, m):
    #     if arr[0][j] == 0:
    #         for i in range(0,n):
    #             arr[i][j] = 0
    
    # row updater
    # for i in range(0, n):
    #     if arr[i][0] == 0:
    #         for j in range(0, n):
    #             arr[i][j] = 0
    return arr
                

matrix = [[1,0,1],[1,1,1],[1,1,1]]
m = len(matrix)
n = len(matrix[0])
print(set_zeros(matrix, m, n))