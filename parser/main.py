import sys
import os
from antlr4 import *
from Errors import errors
from MyErrorListener import MyErrorListener
from MyLexerErrorListener import MyLexerErrorListener
from StackInstructionGenVisitor import StackInstructionGenVisitor
from PrintCallOrderListener import PrintCallOrderListener
from TypeCheckingListener import TypeCheckingListener

from ProjectLexer import ProjectLexer
from ProjectParser import ProjectParser


def compile_file(input_file, output_file):
    input_stream = FileStream(input_file)
    lexer = ProjectLexer(input_stream)
    lexer_error_listener = MyLexerErrorListener()
    lexer.removeErrorListeners()
    lexer.addErrorListener(lexer_error_listener)

    stream = CommonTokenStream(lexer)
    parser = ProjectParser(stream)
    parser.removeErrorListeners()
    parser.addErrorListener(MyErrorListener())

    tree = parser.program()

    if parser.getNumberOfSyntaxErrors() > 0 or lexer_error_listener.had_errors:
        return

    walker = ParseTreeWalker()
    listener = TypeCheckingListener()
    walker.walk(listener, tree)
    if errors.has_errors():
        print(errors)
        return

    visitor = StackInstructionGenVisitor()
    visitor.visit(tree)
    with open(output_file, 'w') as f:
        for instruction in visitor.instructions:
            f.write(instruction)
            f.write('\n')


def main(argv):
    if len(argv) != 2:
        return
    input_file = argv[1]
    output_file = f'{os.path.splitext(input_file)[0]}.out'
    compile_file(input_file, output_file)


if __name__ == '__main__':
    main(sys.argv)
