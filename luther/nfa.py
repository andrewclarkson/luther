from luther.collections import State, Stack, Transition
from luther.exceptions import InvalidTransition
from luther.dfa import DFA

class NFA():
    """
    Creates a Non-deterministic Finite Automata based on a regular 
    expression.
    """

    def __init__(self):
        self.start = None
        self.end = None
        self._states = set()

    @property
    def accepting(self):

        epsilons = set()

        for state in self.states:
            for transition in state:
                if transition == "epsilon":
                    epsilons.add(transition.next)

        return self.end in epsilons | self.states
                

    @property
    def states(self):
        """
        Gets the current state of the machine
        """

        if not self._states:
            self._states = set([self.start])
        
        return self._states

    @states.setter
    def states(self, value):
        """
        Replaces the states set
        """
        self._states = value
    
    def epsilons(self, states=None):
        """
        Collect all epsilon* transitions (zero or more)
        """
        if not states:
            states = self.states

        literals = set()
        
        #TODO: any possible way to make this 
        # not so infinite loop prone... 
        while True:
            next = set()
            for state in states:
                for transition in state:
                    if transition == "epsilon":
                        next.add(transition.next)
                    else:
                        literals.add(state)

            if not next:
                break

            states = next

        return literals

    def __iadd__(self, other):
        """
        Concatenates two NFA's destructively (faster)
        """
        self.end.left = other.start.left
        self.end.right = other.start.right
        self.end = other.end
        return self


    def __add__(self, other):
        """
        TODO:
        Concatenates two NFA's via copying (slower)
        """
        pass

    def __ior__(self, other):
        """
        Alternates two NFA's destructively (faster)
        """

        start = State()
        start.left = Transition("epsilon", self.start)
        start.right = Transition("epsilon", other.start)
        self.start = start

        end = State()
        self.end.add("epsilon", end)
        other.end.add("epsilon", end)
        self.end = end

        return self


    def reset(self):
        """
        Resets the state to the start state
        """
        self.states = set([self.start])


    def transition(self, character):
        """
        Transition the automaton forward by one state
        """
       
        self.states = self.epsilons()

        next = set()
        for state in self.states:
            for transition in state:
                if transition == character:
                    next.add(transition.next)  

        if not next:
            raise InvalidTransition

        self.states = next

    def to_dfa(self):
        """
        Creates a dfa from a nfa
        """
        dfa = DFA()
