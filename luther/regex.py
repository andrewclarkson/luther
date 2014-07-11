from io import StringIO

from luther.collections import Stack, State
from luther.nfa import NFA


class RegularExpression():
    """
    TODO:
        - refactor
        - properties? (self.nfa, self.postfix)
    """


    def __init__(self, expression):
        self.expression = expression

    def to_nfa(self):
        #TODO: refactor... too long
        stack = Stack()

        for character in self.to_postfix():

            if character == "*":
                try:
                    previous = stack.pop()
                except IndexError:
                    raise SyntaxError
                
                previous.end.add("epsilon", previous.start)

                start = State()
                end = State()

                start.add("epsilon", previous.start)
                start.add("epsilon", end)
                previous.end.add("epsilon", end)

                previous.start = start
                previous.end = end

                stack.push(previous)
            
            elif character == ".":
                # TODO: refactor to Stack class
                try:
                    second = stack.pop()
                    first = stack.pop()
                except IndexError:
                    raise SyntaxError

                first += second
                stack.push(first)

            elif character == "|":
                try:
                    second = stack.pop()
                    first = stack.pop()
                except IndexError:
                    raise SyntaxError

                first |= second
                stack.push(first)
                
            elif character == "+":
                try:
                    previous = stack.pop()
                except IndexError:
                    raise SyntaxError
                
                previous.end.add("epsilon", previous.start)
                stack.push(previous)
            
            elif character == "?":
                try:
                    previous = stack.pop()
                except IndexError:
                    raise SyntaxError
                
                start = State()
                start.add("epsilon", previous.start)
                start.add("epsilon", previous.end)
                previous.start = start
                stack.push(previous)

            else:
                # TODO: refactor to NFA class
                symbol = NFA()
                symbol.end = State()
                symbol.start = State()
                symbol.start.add(character, symbol.end)
                stack.push(symbol)

        return stack.pop()



    def to_postfix(self):
        """
        Parses the regular expression into postfix form
        """
        #TODO: refactor... too long
        buffer = StringIO()

        unary = [
            "*",
            "+",
            "?"
        ]

        stack = Stack()
        literals = 0
        alternates = 0
        escaped = False

        for character in self.expression:

            # Escape the next character and continue
            if escaped:
                escaped = False
                buffer.write(character + "\\")
                continue

            # Escape character
            if character == "\\":
                escaped = True
            
            #
            elif character == "(":
                
                if literals > 1:
                    literals -= 1
                    buffer.write(".")
                else:
                    literals = 0

                stack.push((literals, alternates))

                literals = 0
                alternates = 0

            elif character == "|":
                if literals == 0:
                    raise SyntaxError
                
                if literals > 1:
                    literals = 0
                    buffer.write(".")
                else:
                    literals = 0
                
                alternates += 1

            elif character == ")":
                if literals == 0:
                    SyntaxError
               
                if literals > 1:
                    literals = 1
                    buffer.write(".")
                else:
                    literals = 0

                while alternates:
                    buffer.write("|")
                    alternates -= 1
                
                try:
                    literals, alternates = stack.pop()
                except IndexError:
                    raise SyntaxError
                
                literals += 1


            # The unary operators are already postfix
            elif character in unary:
                if literals == 0:
                    raise SyntaxError

                buffer.write(character)

            # A literal character
            else:
                # concatenate more than two literal characters
                if literals > 1:
                    literals -= 1
                    buffer.write(".")
                
                literals += 1
                buffer.write(character)
       
        if len(stack) > 0:
            raise SyntaxError

        while literals > 1:
            buffer.write(".")
            literals -= 1
        
        while alternates:
            buffer.write("|")
            alternates -= 1

        return buffer.getvalue()
