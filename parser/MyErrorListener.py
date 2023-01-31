from antlr4.error.ErrorListener import ErrorListener

class MyErrorListener(ErrorListener):
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        stack = recognizer.getRuleInvocationStack()
        stack.reverse()
          
        print("rule stack: " + ", ".join(stack))
        print(f"[Line {line}, column {column}] at {offendingSymbol}: {msg}")
    pass

