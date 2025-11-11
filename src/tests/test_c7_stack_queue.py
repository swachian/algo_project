import pytest
from algo_project.c7_stack_queue import Queue as MyQueue

def test_enqueue_and_peek():
    q = MyQueue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    assert q.peek() == 1  # first element remains in front

def test_dequeue_order():
    q = MyQueue()
    q.enqueue(10)
    q.enqueue(20)
    q.enqueue(30)
    assert q.dequeue() == 10
    assert q.dequeue() == 20
    assert q.dequeue() == 30

def test_mixed_operations():
    q = MyQueue()
    q.enqueue(5)
    q.enqueue(6)
    assert q.dequeue() == 5
    q.enqueue(7)
    assert q.peek() == 6
    assert q.dequeue() == 6
    assert q.dequeue() == 7

# def test_empty_exceptions():
#     q = MyQueue()
#     with pytest.raises(IndexError):
#         q.dequeue()
#     with pytest.raises(IndexError):
#         q.peek()