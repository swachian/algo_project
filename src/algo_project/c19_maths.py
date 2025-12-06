def spiral_matrix(matrix):
    #  设置top, bottom， left, right 4个边界，只要top和left没有越过bottom和right,就持续遍历
    # 中间第三和第四步时，因为top和right已经做过修正，所以要再次判断top或right是否已经越过bottom和left
    if not matrix:
        return []
    
    top, bottom = 0, len(matrix) - 1
    left, right = 0, len(matrix[0]) - 1
    res = []
    
    while top <= bottom and left <= right:
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
        