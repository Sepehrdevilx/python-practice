
matrix = [1,2,3],[4,5,6],[7,8,9]

l, r = 0, len(matrix) -1

while l < r :
    for i in range(r -1):
        top, bottom = l, r

        topLeft = matrix[top][l + i]
        matrix[top][l+i] = matrix[bottom - i][l]
        matrix[bottom-i][l] = matrix[bottom][r-i]
        matrix[bottom][r-i] = matrix[top+i][r]
        matrix[top+i][r]=topLeft
        for x in matrix:
            print(x)
    r -= 1
    l+=1