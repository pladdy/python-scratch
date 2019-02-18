import pytest

from data_structures.linked_list import LinkedList
from data_structures.linked_list import Node


def list_from_array(array):
    list = LinkedList()
    for node in array:
        list.append(node)
    return list

def list_from_integer(int):
    list = LinkedList()
    for i in range(int):
        list.append(i + 1)
    return list

class TestLinkedList:
    def test_init(self):
        assert LinkedList().head is None

    def test_append(self):
        list = LinkedList()
        list.append("a node")

        first = list.head
        assert list.count() == 1
        assert first.data == "a node"
        assert first.next is None
        assert first.past is None

        list.append("another node")
        second = first.next
        assert list.count() == 2
        assert second.data == "another node"
        assert second.next is None
        assert second.past == first
        assert first.next == second

        list.append("yet another node")
        third = second.next
        assert list.count() == 3
        assert third.data == "yet another node"
        assert third.next is None
        assert third.past == second
        assert second.next == third

    def test_count(self):
        list = LinkedList()
        assert list.count() == 0

        list.insert("a node")
        assert list.count() == 1

        list.insert("another node")
        assert list.count() == 2

    def test_delete(self):
        list = list_from_integer(3)
        assert list.count() == 3
        assert list.to_array() == [1, 2, 3]

        list.delete(2)
        assert list.count() == 2

        first = list.head
        last = first.next

        assert first.data == 1
        assert first.next == last
        assert first.past is None

        assert last.data == 3
        assert last.next is None
        assert last.past == first

        list = list_from_integer(5)
        list.delete(3)
        assert list.to_array() == [1, 2, 4, 5]

        list.append(5)
        assert list.to_array() == [1, 2, 4, 5, 5]

        list.delete(5)
        assert list.to_array() == [1, 2, 4]

        list.delete(1)
        assert list.to_array() == [2, 4]

        list.delete(3)
        assert list.to_array() == [2, 4]

        list.delete(2)
        assert list.to_array() == [4]

        list.delete(4)
        assert list.to_array() == []

    def test_insert(self):
        list = LinkedList()
        list.insert("a node")

        first = list.head
        assert list.count() == 1
        assert first.data == "a node"
        assert first.next is None
        assert first.past is None

        list.insert("another node")
        new_first = list.head
        assert list.count() == 2
        assert new_first.data == "another node"
        assert new_first.next == first
        assert new_first.past is None
        assert first.past == new_first

        list.insert("yet another node")
        new_first = list.head
        second = new_first.next
        assert list.count() == 3
        assert new_first.data == "yet another node"
        assert new_first.next == second
        assert new_first.past is None
        assert first.past == second

    def test_reverse(self):
        tests = [
            {'list': list_from_integer(3),
             'before': [1, 2, 3],
             'after': [3, 2, 1]
             },
            {'list': list_from_integer(1),
             'before': [1],
             'after': [1]
             },
            {'list': list_from_array([]),
             'before': [],
             'after': []
             },
            {'list': list_from_array(["first", "second", "third"]),
             'before': ["first", "second", "third"],
             'after': ["third", "second", "first"]
             }
        ]

        for test in tests:
            list = test['list']
            assert list.to_array() == test['before']
            list.reverse()
            assert list.to_array() == test['after']


class TestNode:
    def test_init(self):
        node = Node("data")
        assert node.data == "data"
        assert node.next is None
        assert node.past is None

    def test_to_string(self):
        node = Node("data")
        str = node.to_string()
        assert len(str) > 0
