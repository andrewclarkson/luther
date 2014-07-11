from luther.dfa import DFA

class Lexer():

    def __init__(self, **options):

        #TODO try except
        self.source = options.pop("source")
        self.machine = DFA()
        


    def next(self):


        for character in source:
            token = self.machine.advance(character)
            if token:
                yield token


    def __setitem__(self, token, regex):

        for character in regex:
            
