def spiral_matrix(matrix):
    if not matrix or not matrix[0]:
        return matrix
    
    top, bottom = 0, len(matrix) - 1
    left, right = 0, len(matrix[0]) - 1
    res = []
    
    while top <= bottom or left <= right:
        i = top
        j = left
        for j in range(left, right + 1):
            res.append(matrix[i][j])
        top += 1
        
        for i in range(top, bottom + 1):
            res.append(matrix[i][j])
        right -= 1
        
        if top <= bottom: 
            for j in range(right, left - 1, -1):
                res.append(matrix[i][j])
            bottom -= 1
        
        if left <= right:    
            for i in range(bottom, top - 1, -1):
                res.append(matrix[i][j])
            left += 1
    return res