from luther import Tokenizer, Token

class Word(Token):
    """
    A word token
    """
    pattern = r"[a-zA-Z]+"

class Whitespace(Token):
    """
    A whitespace token
    """
    pattern = r"[\t\n ]+"

class Punctuation(Token):
    """
    A punctuation token
    """
    pattern = r"[!-/:-@[-`{-~]"


if __name__ == "__main__":

    source = """
    hello world!
    """

    tokenizer = Tokenizer(source)

    tokenizer.tokens = [
        Word,
        Whitespace,
        Punctuation
    ]

    for token in Tokenizer(source=source, tokens=tokens):
