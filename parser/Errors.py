from antlr4.tree.Tree import TerminalNode

class Errors():
    def __init__(self) -> None:
        self.errors = []

    def add(self, symbol, error):
        if isinstance(symbol, TerminalNode):
            symbol = symbol.getSymbol()
        self.errors.append(f'[Line {symbol.line}, column {symbol.column}]: {error}')

    def has_errors(self):
        return len(self.errors) > 0

    def __str__(self):
        return "\n".join(self.errors)

errors = Errors()