def spiralmatrix(arr, m, n):
    left = top  = 0
    right = n
    bottom = m
    # for i in range(0, m):
    #     for j in range(0, n):
    #         if j < m:
    #             print(arr[i][j], end=" ")
    while left < right and top < right:
        for i in range(left, right):
            print(arr[top][i], end=" ")
        top += 1
        
        if top == bottom:
            break
        
        for i in range(top, bottom):
            print(arr[i][right-1], end=" ")
        right -= 1
        
        if left == right:
            break
    
        for i in range(right-1, left-1, -1):
            print(arr[bottom-1][i], end=" ")
        bottom -= 1
        
        for i in range(bottom - 1, top-1, -1):
            print(arr[i][left], end=" ")
        left += 1


# mtrx = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
# mtrx = [[1,2,3,4]]
mtrx = [[1],[5],[9],[13]]
m = len(mtrx)
n = len(mtrx[0])
spiralmatrix(mtrx, m, n)