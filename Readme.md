#Luther - The lexer

A pythonic lexical analyzer (tokenizer) written for research purposes

##Todo
- Regular expression to NFA
    - X Convert to postfix form
    - X One Character machines
    - X Concatenation ('.')
    - X Kleene Start ('*')
    - X Repetition ('+')
    - X Optional ('?')
    - X Union ('|')
- DFA from NFA
- Optimization
    - X Prune Unreachable
    - X Hopcroft Minimization
- Validation
- Extend Syntax
    - Advanced Repetition "{0,4}"
    - Sets "[abcd]"
    - Ranges "[a-z]"
    - Intersection "&"
    - Difference "-"
    - Negation "!"
- Graphviz Support
