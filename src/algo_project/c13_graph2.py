from collections import deque

def shortest_transformation_sequence(start, end, words):
    words_set = set(words)
    visited = set()
    if start not in words_set or end not in words_set:
        return 0
    
    abc = "abcdefghijklmnopqrstuvwxyz"
    queue = deque()
    queue.append(start)
    visited.add(start)
    
    count = 0
    while queue:
        count += 1
        level_size = len(queue)
        for _ in range(level_size):
            word = queue.popleft()
            if word == end:
                return count
            for i in range(len(word)): 
                for c in abc:
                    new_word = word[0:i] + c + word[i + 1:]
                    if new_word in words_set and new_word not in visited:
                        queue.append(new_word)
                        visited.add(new_word)

                    
    return 0
    