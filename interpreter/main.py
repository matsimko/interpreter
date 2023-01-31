import sys
from Interpreter import Interpreter


def main(argv):
    if len(argv) != 2:
        return
    filename = argv[1]
    interpreter = Interpreter(filename)
    print(f'---{filename}---')
    interpreter.run()
    print()


if __name__ == '__main__':
    main(sys.argv)
