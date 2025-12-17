import pytest
from algo_project.c13_graph2 import shortest_transformation_sequence, MergingCommunities, prerequisites, shortest_path, connect_the_dots

def test_shortest_transformation_sequence_exists():
    start = "hit"
    end = "cog"
    dictionary = ["hit", "hot", "dot", "dog", "lot", "log", "cog"]
    res = shortest_transformation_sequence(start, end, dictionary)
    # hit → hot → dot → dog → cog = 5 steps
    assert res == 5

def test_shortest_transformation_sequence_exists2():
    start = 'red'
    end = 'hit'
    dictionary = [
            'red', 'bed', 'hat', 'rod', 'rad', 'rat', 'hit', 'bad', 'bat'
       ]
    res = shortest_transformation_sequence(start, end, dictionary)
    # hit → hot → dot → dog → cog = 5 steps
    assert res == 5
    
def test_shortest_transformation_sequence_no_path():
    start = "loop"
    end = "pool"
    dictionary =["loop","pool","pole","poll","loom","doom","doop"]  # No "cog"
    res = shortest_transformation_sequence(start, end, dictionary)
    assert res == 0


def test_merging_communities_basic():
    mc = MergingCommunities(5)

    mc.connect(0, 1)
    mc.connect(1, 2)

    assert mc.get_community_size(0) == 3
    assert mc.get_community_size(2) == 3
    assert mc.get_community_size(3) == 1  # untouched

def test_merging_communities_multiple_groups():
    mc = MergingCommunities(6)

    mc.connect(0, 1)
    mc.connect(2, 3)
    mc.connect(1, 2)   # merges {0,1} and {2,3}

    assert mc.get_community_size(0) == 4
    assert mc.get_community_size(3) == 4

    mc.connect(4, 5)
    assert mc.get_community_size(4) == 2

    # Repeated connect should not change anything
    mc.connect(0, 3)
    assert mc.get_community_size(1) == 4


def test_prerequisites_no_cycle():
    """Test case where it's possible to finish all courses (no cycle)"""
    n = 4
    prerequisites_list = [[1, 0], [2, 1], [3, 2]]
    # Valid order: 0 -> 1 -> 2 -> 3
    assert prerequisites(n, prerequisites_list) == True

def test_prerequisites_with_cycle():
    """Test case where it's impossible to finish due to cycle"""
    n = 3
    prerequisites_list = [[1, 0], [2, 1], [0, 2]]
    # Cycle: 0 -> 1 -> 2 -> 0
    assert prerequisites(n, prerequisites_list) == False
    

def test_shortest_path_basic():
    """Test basic shortest path functionality"""
    n = 5
    edges = [
        [0, 1, 2],
        [0, 2, 4],
        [1, 2, 1],
        [1, 3, 7],
        [2, 4, 3],
        [3, 4, 1]
    ]
    start = 0
    
    result = shortest_path(n, edges, start)
    expected = [0, 2, 3, 9, 6]  # Shortest paths from node 0
    
    assert result == expected

def test_shortest_path_unreachable():
    """Test case with unreachable nodes"""
    n = 4
    edges = [
        [0, 1, 3],
        [1, 2, 2]
        # Node 3 is disconnected
    ]
    start = 0
    
    result = shortest_path(n, edges, start)
    expected = [0, 3, 5, -1]  # Node 3 is unreachable
    
    assert result == expected
    
def test_connect_the_dots_single_point():
    """Test case with single point"""
    points = [[0, 0]]
    result = connect_the_dots(points)
    expected = 0
    assert result == expected

def test_connect_the_dots_two_points():
    """Test case with two points"""
    points = [[0, 0], [1, 1]]
    result = connect_the_dots(points)
    expected = 2  # |0-1| + |0-1| = 1 + 1 = 2
    assert result == expected