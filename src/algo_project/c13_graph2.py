from collections import deque

class GraphNode:
    def __init__(self, val):
        self.val = val
        self.neighbors = []

def shortest_transformation_sequence(start, end, dictionary):
    # 0. 检查start和end在不在 dictionary
    # 1. 转换成set
    # 2. 找到start
    # 3. 用在word L各个位置遍历替换26个字母的办法找到潜在的下家，并记录在queue里，该下家必须未出现在visited中过
    # 4. 把word加入 visited
    # 5. dist++, 如果找到了终点，则返回dist
    words = set(dictionary)
    abc = "abcdefghijklmnopqrstuvwxyz"
    if start not in dictionary or end not in dictionary:
        return 0
    if start == end:
        return 1
    queue = deque([start])
    visited = set()
    dist = 0
    while queue:
        level_size = len(queue)
        for l in range(level_size):
            if l == 0:
                dist += 1
            node = queue.popleft()
            visited.add(node)
            if node == end:
                return dist
            for i in range(len(node)):
                for c in abc:
                    next_word = node[0:i] + c + node[i+1:]
                    if next_word in words and next_word not in visited:
                        queue.append(next_word) 
            
    return 0