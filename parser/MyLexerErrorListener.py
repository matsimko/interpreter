from antlr4.error.ErrorListener import ErrorListener


class MyLexerErrorListener(ErrorListener):
    def __init__(self) -> None:
        super().__init__()
        self.had_errors = False

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        self.had_errors = True
        print(f"[Line {line}, column {column}] at {offendingSymbol}: {msg}")
    pass
