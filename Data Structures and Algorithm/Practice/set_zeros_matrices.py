def set_zeros(arr, m ,n):
    firstrow = False
    firstcol = False
    # Looping through matrix to find the zeros and updating respective rows and clolumns
    for i in range(0,m):
        for j in range(0,n):
            if arr[i][j] == 0:
                if i == 0 and arr[0][j] == 0:
                    firstrow = True
                if j == 0 and arr[i][0] == 0:
                    firstcol = True
                if j != 0 and i != 0:
                    arr[i][0] = 0
                    arr[0][j] = 0 
    print(arr) 
    print(firstrow)           
    # column updater
    for j in range(0, n):
        if arr[0][j] == 0 and j !=0 :
            for i in range(0,m):
                arr[i][j] = 0
    
    # row updater
    for i in range(0, m):
        if arr[i][0] == 0 and i != 0:
            for j in range(0, n):
                arr[i][j] = 0
    if firstrow:
        for j in range(0,n):
            arr[0][j] = 0
    
    if firstcol:
        for i in range(0,m):
            arr[i][0] = 0
    return arr
                

matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
m = len(matrix)
n = len(matrix[0])
print(set_zeros(matrix, m, n))