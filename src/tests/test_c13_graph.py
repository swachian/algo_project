import pytest
from algo_project.c13_graph import graph_deep_copy, GraphNode #, count_islands, matrix_infection
# from algo_project.c13_graph import bipartite_graph_validation, longest_increasing_path

def test_graph_deep_copy_triangle():
    # Original graph:
    # 1 -- 2
    #  \   /
    #    3
    n1 = GraphNode(1)
    n2 = GraphNode(2)
    n3 = GraphNode(3)

    n1.neighbors = [n2, n3]
    n2.neighbors = [n1, n3]
    n3.neighbors = [n1, n2]

    clone = graph_deep_copy(n1)

    # Values must match (order not guaranteed)
    def collect(node):
        from collections import deque
        visited = set()
        q = deque([node])
        vals = []
        while q:
            cur = q.popleft()
            if cur in visited:
                continue
            visited.add(cur)
            vals.append(cur.val)
            for nei in cur.neighbors:
                q.append(nei)
        return sorted(vals)

    assert collect(clone) == [1, 2, 3]

    # Must be deep copy — different objects
    assert clone is not n1
    for orig, cp in zip([n1] + n1.neighbors, [clone] + clone.neighbors):
        assert orig is not cp
        
# def test_count_islands_multiple():
#     matrix = [
#         [1, 1, 0, 0],
#         [1, 0, 0, 1],
#         [0, 0, 1, 1],
#         [0, 0, 0, 0],
#     ]
#     # Islands:
#     # - (0,0),(0,1),(1,0)
#     # - (1,3),(2,3),(2,2)
#     assert count_islands(matrix) == 2
    
# def test_count_islands_single():
#     matrix = [
#         [1, 1],
#         [1, 1]
#     ]
#     assert count_islands(matrix) == 1


# def test_matrix_infection_all_infectable():
#     matrix = [
#         [2, 1, 1],
#         [1, 1, 0],
#         [0, 1, 1]
#     ]
#     # Infection spreads like:
#     # t=0: initial infected
#     # t=1,2,3,4: final total time = 4
#     assert matrix_infection(matrix) == 4
    
# def test_matrix_infection_impossible():
#     matrix = [
#         [2, 1, 1],
#         [0, 0, 1],
#         [1, 0, 1]
#     ]
#     # Bottom-left '1' is isolated → impossible
#     assert matrix_infection(matrix) == -1

# def test_bipartite_graph_validation():
#     # Test case 1: Simple bipartite graph
#     graph1 = [
#         [1, 3],
#         [0, 2],
#         [1, 3],
#         [0, 2]
#     ]
#     assert bipartite_graph_validation(graph1) == True

#     # Test case 2: Non-bipartite graph (odd cycle)
#     graph2 = [
#         [1, 2],
#         [0, 2],
#         [0, 1]
#     ]
#     assert bipartite_graph_validation(graph2) == False

# def test_longest_increasing_path_basic():
#     matrix = [
#         [9, 9, 4],
#         [6, 6, 8],
#         [2, 1, 1]
#     ]
#     # Longest increasing path: 1 → 2 → 6 → 9 (length = 4)
#     assert longest_increasing_path(matrix) == 4

# def test_longest_increasing_path_full_increasing():
#     matrix = [
#         [1, 2, 3],
#         [6, 5, 4],
#         [7, 8, 9]
#     ]
#     # One possible path: 1→2→3→4→5→6→7→8→9  (length = 9)
#     assert longest_increasing_path(matrix) == 9
