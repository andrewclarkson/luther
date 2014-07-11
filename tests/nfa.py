from unittest import TestCase

from luther.nfa import NFA
from luther.exceptions import InvalidTransition
from luther.collections import State, Transition

class TestNFA(TestCase):

    
    def test_concatenation(self):
        """
        Tests the concatenation of two NFAs
        """
        a = NFA()
        a.end = State()
        a.start = State()
        a.start.left = Transition("a", a.end)

        b = NFA()
        b.end = State()
        b.start = State()
        b.start.left = Transition("b", b.end)

        a += b

        self.assertEqual(a.end, b.end)

        

