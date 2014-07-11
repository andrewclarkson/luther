#Luther - The lexer

A pythonic lexical analyzer (tokenizer) written for research purposes

##Todo
-[ ] Regular expression to NFA
    -[x] Convert to postfix form
    -[x] One Character machines
    -[x] Concatenation ('.')
    -[x] Kleene Start ('*')
    -[x] Repetition ('+')
    -[] Optional ('?')
    -[x] Union ('|')
-[ ] DFA from NFA
    -[ ]
-[ ] Optimization
    -[ ] Prune Unreachable
    -[ ] Hopcroft Minimization
-[ ] Validation
-[ ] Extend Syntax
    -[ ] Advanced Repetition "{0,4}"
    -[ ] Sets "[abcd]"
    -[ ] Ranges "[a-z]"
    -[ ] Intersection "&"
    -[ ] Difference "-"
    -[ ] Negation "!"
-[ ] Graphviz Support
