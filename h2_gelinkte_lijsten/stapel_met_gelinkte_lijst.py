class StackList:

    """
    >>> s = StackList()
    >>> s.is_empty()
    True
    >>> s.push("This")
    >>> s.is_empty()
    False
    >>> s.peek()
    'This'
    >>> s.push("Is")
    >>> s.push("A Test")
    >>> s.peek()
    'A Test'
    >>> s.pop()
    'A Test'
    >>> s.pop()
    'Is'
    >>> s.is_empty()
    False
    >>> s.pop()
    'This'
    >>> s.is_empty()
    True
    """

    class Knoop:
        def __init__(self, data=None, volgende=None):
            self.data = data
            self.volgende = volgende

    def __init__(self):
        self.top = None

    def is_empty(self):
        return self.top is None

    def push(self, data):
        nieuw = StackList.Knoop(data, self.top)
        self.top = nieuw

    def peek(self):
        return self.top.data

    def pop(self):
        x = self.top.data
        self.top = self.top.volgende
        return x
    