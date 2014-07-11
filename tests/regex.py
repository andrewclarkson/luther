from unittest import TestCase

from luther.regex import RegularExpression
from luther.collections import State
from luther.exceptions import InvalidTransition

class TestRegularExpression(TestCase):

    def test_postfix(self):
        """
        Tests the functionality of translating infix
        regular expressions to postfix ones
        """

        regex = RegularExpression("ab")
        self.assertEqual(regex.to_postfix(), "ab.")
        
        regex = RegularExpression("abc")
        self.assertEqual(regex.to_postfix(), "ab.c.")
        
        regex = RegularExpression("abcd")
        self.assertEqual(regex.to_postfix(), "ab.c.d.")
        
        regex = RegularExpression("ab+")
        self.assertEqual(regex.to_postfix(), "ab+.")

        regex = RegularExpression("ab*(cd|fg)")
        self.assertEqual(regex.to_postfix(), "ab*.cd.fg.|.")
        
        regex = RegularExpression("a|b|c|d")
        self.assertEqual(regex.to_postfix(), "abcd|||")
        
        regex = RegularExpression("(ab|c)*|d")
        self.assertEqual(regex.to_postfix(), "ab.c|*d|")


    def test_atom(self):
        """
        Tests a simple one character expression
        """
        nfa = RegularExpression("a").to_nfa()
        nfa.transition("a")

        expected = set([nfa.end])
        self.assertEqual(nfa.states, expected)

        with self.assertRaises(InvalidTransition):
            nfa.transition("a")

    def test_concatenation(self):
        """
        Tests the concatenation of two atomic expressions
        """

        nfa = RegularExpression("ab").to_nfa()
        
        nfa.transition("a")
        nfa.transition("b")
        
        expected = set([nfa.end])
        self.assertEqual(nfa.states, expected)
        
        with self.assertRaises(InvalidTransition):
            nfa.transition("a")
        
        nfa = RegularExpression("aaaaa").to_nfa()
        
        for character in "aaaaa":
            nfa.transition("a")

        expected = set([nfa.end])
        self.assertEqual(nfa.states, expected)
        
        with self.assertRaises(InvalidTransition):
            nfa.transition("a")
    
    def test_kleene_star(self):
        """
        Test kleene star (zero or more)
        """
        nfa = RegularExpression("a*").to_nfa()

        self.assertTrue(nfa.accepting)

        for character in "aaaa":
            nfa.transition(character)

        self.assertTrue(nfa.accepting)
        

    def test_repetition(self):
        """
        Test repetition (one or more)
        """
        nfa = RegularExpression("a+").to_nfa()

        self.assertFalse(nfa.accepting)

        for character in "aaaa":
            nfa.transition(character)

        self.assertTrue(nfa.accepting)
    
    
    def test_alternation(self):
        """
        Test alternation "|"
        """
        nfa = RegularExpression("a|b").to_nfa()
        self.assertFalse(nfa.accepting)

        nfa.transition("a")
        self.assertTrue(nfa.accepting)

        nfa.reset()

        nfa.transition("b")
        self.assertTrue(nfa.accepting)

    def test_complex(self):
        """
        Tests more complex regular expressions
        """
        nfa = RegularExpression("a*(a|b)+").to_nfa()
        self.assertFalse(nfa.accepting)

        for character in "aaaabababaab":
            nfa.transition(character)

        self.assertTrue(nfa.accepting)
        

    def test_optional(self):
        """
        Tests the optional operator "?"
        """
        
        nfa = RegularExpression("a?a?a?aaa").to_nfa()
        self.assertFalse(nfa.accepting)

        for character in "aaa":
            nfa.transition(character)

        self.assertTrue(nfa.accepting)
