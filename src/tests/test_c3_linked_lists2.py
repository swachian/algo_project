import pytest
from algo_project.c3_linked_lists2 import LRUCache



def test_basic_put_and_get():
    """Basic test: put and get single item."""
    cache = LRUCache(2)
    cache.put(1, 10)
    assert cache.get(1) == 10
    assert cache.get(2) == -1  # non-existing key


def test_update_existing_key():
    """If key already exists, update its value and mark as recently used."""
    cache = LRUCache(2)
    cache.put(1, 10)
    cache.put(1, 20)
    assert cache.get(1) == 20


def test_eviction_order():
    """Least recently used item should be evicted when capacity exceeded."""
    cache = LRUCache(2)
    cache.put(1, 10)
    cache.put(2, 20)
    cache.put(3, 30)  # should evict key=1
    assert cache.get(1) == -1
    assert cache.get(2) == 20
    assert cache.get(3) == 30


def test_recently_used_promoted():
    """Accessing an item makes it most recently used, so it should not be evicted."""
    cache = LRUCache(2)
    cache.put(1, 10)
    cache.put(2, 20)
    cache.get(1)        # 1 becomes most recently used
    cache.put(3, 30)    # evict 2
    assert cache.get(2) == -1
    assert cache.get(1) == 10
    assert cache.get(3) == 30


def test_capacity_one():
    """When capacity = 1, every new put evicts previous entry."""
    cache = LRUCache(1)
    cache.put(1, 10)
    assert cache.get(1) == 10
    cache.put(2, 20)
    assert cache.get(1) == -1
    assert cache.get(2) == 20


def test_multiple_updates_and_evictions():
    """Complex sequence of puts and gets to test internal consistency."""
    cache = LRUCache(3)
    cache.put(1, 1)
    cache.put(2, 2)
    cache.put(3, 3)
    cache.get(1)        # access 1, now most recent
    cache.put(4, 4)     # evict key=2
    assert cache.get(2) == -1
    assert cache.get(3) == 3
    assert cache.get(1) == 1
    assert cache.get(4) == 4
