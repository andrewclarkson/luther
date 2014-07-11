from unittest import TestCase

from luther.collections import State, TransitionTable

class TestTransitionTable(TestCase):

    def test_init(self):
        table = TransitionTable()
        self.assertEqual(table, [State()])

    def test_update(self):
        table = TransitionTable()
        table.update(0, {"a": 1})
        self.assertEqual(table, [{"a": 1}])


    def test_append(self):
        table = TransitionTable()
        table.append(State())
        self.assertEqual(table, [{}, {}])

