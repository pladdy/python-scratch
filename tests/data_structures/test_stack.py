from python_scratch.data_structures.stack import Stack


def test_stack():
    s = Stack()
    assert s.isEmpty() is True
    assert s.peek() is None
    assert s.size() == 0

    s.push("some data")
    assert s.isEmpty() is False
    assert s.peek() == "some data"
    assert s.size() == 1

    assert s.pop() == "some data"
    assert s.isEmpty() is True
    assert s.size() == 0

    assert s.pop() is None

    s.push("1")
    s.push("2")
    assert s.isEmpty() is False
    assert s.peek() == "2"
    assert s.size() == 2
