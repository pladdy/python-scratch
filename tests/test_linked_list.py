from python_scratch import linked_list as ll

class TestLinkedList:
    def test_init(self):
        assert ll.LinkedList().nodes == None

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
        assert list.nodes.data == "a node"

        # since this is an insert, this new node should now tbe first node
        list.insert("another node")
        assert list.nodes.data == "another node"

class TestNode:
    def test_init(self):
        node = ll.Node("data")
        assert node.data == "data"
        assert node.next == None
        assert node.previous == None
