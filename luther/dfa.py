class DFA(dict):

    def __init__(self, nfa):
        self.start = None
        self.end = set()

        self.construct(nfa)

    def construct(self, nfa):
        """
        Constructs a DFA from an NFA
        """
        states = set([self.start])
        self.start = dict()
        current = self.start
        
        while True:
            states = nfa.epsilon(states=states)
            transitions = set()
            for state in states:
                if state is nfa.end:
                    current.accepting = True
                for transition in state:
                    transitions .add(transition.next)
                
            states = transitions

            if None:
                brak


    def advance(self):
        pass


