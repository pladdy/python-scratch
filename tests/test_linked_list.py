from python_scratch import linked_list as ll


class TestLinkedList:
    def test_init(self):
        assert ll.LinkedList().head is None

    def test_append(self):
        list = ll.LinkedList()
        list.append("a node")
        assert list.head.data == "a node"

        list.append("another node")
        assert list.head.next.data == "another node"

        list.append("yet another node")
        assert list.head.next.next.data == "yet another node"

    def test_count(self):
        list = ll.LinkedList()
        assert list.count() == 0

        list.insert("a node")
        assert list.count() == 1

        list.insert("another node")
        assert list.count() == 2

    def test_insert(self):
        list = ll.LinkedList()
        list.insert("a node")

        # the first node is the newly inserted node
        assert list.head.data == "a node"

        # since this is an insert, this new node should now tbe first node
        list.insert("another node")
        assert list.head.data == "another node"

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
