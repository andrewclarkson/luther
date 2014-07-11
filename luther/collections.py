"""
Common Data Structures
"""


class StateOverload(BaseException):
    pass

class State():
    """
    Implements a state with left and right transitions
    """
    def __init__(self):
        self.left = None
        self.right = None

    def __iter__(self):
        return iter((self.left, self.right))

    def __repr__(self):
        return "({}, {})".format(self.left, self.right)

    def add(self, event, node):
        """
        """
        if self.left and self.right:
            raise StateOverload

        if self.left:
            self.right = Transition(event, node)
        elif self.right:
            self.left = Transition(event, node)
        else:
            self.left = Transition(event, node)


class Transition():
    """
    Implements a transition
    """
    def __init__(self, event, next):
        self.event = event
        self.next = next

    def __eq__(self, event):
        return self.event == event

    def __repr__(self):
        return self.event

class Stack(list):
    def push(self, item):
        self.append(item)

