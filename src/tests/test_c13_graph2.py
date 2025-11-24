import pytest
from algo_project.c13_graph2 import shortest_transformation_sequence

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
