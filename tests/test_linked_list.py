from python_scratch import linked_list as ll

class TestLinkedList:
    def test_init(self):
        assert ll.LinkedList().nodes == []
