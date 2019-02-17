import pytest

from data_structures import linked_list as ll

@pytest.fixture
def new_linked_list():
        list = ll.LinkedList()
        list.append(1)
        list.append(2)
        list.append(3)
        list.append(4)
        list.append(5)
        return list

class TestLinkedList:
    def test_init(self):
        assert ll.LinkedList().head is None

    def test_append(self):
        list = ll.LinkedList()
        list.append("a node")

        first = list.head
        assert list.count() == 1
        assert first.data == "a node"
        assert first.next == None
        assert first.past == None

        list.append("another node")
        second = first.next
        assert list.count() == 2
        assert second.data == "another node"
        assert second.next == None
        assert second.past == first
        assert first.next == second

        list.append("yet another node")
        third = second.next
        assert list.count() == 3
        assert third.data == "yet another node"
        assert third.next == None
        assert third.past == second
        assert second.next == third

    def test_count(self):
        list = ll.LinkedList()
        assert list.count() == 0

        list.insert("a node")
        assert list.count() == 1

        list.insert("another node")
        assert list.count() == 2

    def test_delete(self, new_linked_list):
        list = ll.LinkedList()
        list.append(1)
        list.append(2)
        list.append(3)
        assert list.count() == 3
        assert list.to_array() == [1, 2, 3]

        list.delete(2)
        assert list.count() == 2

        first = list.head
        last = first.next

        assert first.data == 1
        assert first.next == last
        assert first.past == None

        assert last.data == 3
        assert last.next == None
        assert last.past == first

        list = new_linked_list
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
        list = ll.LinkedList()
        list.insert("a node")

        first = list.head
        assert list.count() == 1
        assert first.data == "a node"
        assert first.next == None
        assert first.past == None

        list.insert("another node")
        new_first = list.head
        assert list.count() == 2
        assert new_first.data == "another node"
        assert new_first.next == first
        assert new_first.past == None
        assert first.past == new_first

    def test_reverse(self):
        list = ll.LinkedList()
        list.insert(3)
        list.insert(2)
        list.insert(1)

        assert list.to_array() == [1, 2, 3]
        list.reverse()
        assert list.to_array() == [3, 2, 1]


class TestNode:
    def test_init(self):
        node = ll.Node("data")
        assert node.data == "data"
        assert node.next is None
        assert node.past is None
