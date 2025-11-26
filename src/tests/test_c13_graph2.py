import pytest
from algo_project.c13_graph2 import shortest_transformation_sequence, MergingCommunities

def test_shortest_transformation_sequence_exists():
    start = "hit"
    end = "cog"
    dictionary = ["hit", "hot", "dot", "dog", "lot", "log", "cog"]
    res = shortest_transformation_sequence(start, end, dictionary)
    # hit → hot → dot → dog → cog = 5 steps
    assert res == 5


def test_shortest_transformation_sequence_no_path():
    start = "hit"
    end = "cog"
    dictionary = ["hot", "dot", "dog", "lot", "log"]  # No "cog"
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

