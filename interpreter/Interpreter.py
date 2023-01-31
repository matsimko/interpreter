import shlex
from Instructions import INSTRUCTION_MAP

class Interpreter():

    def __init__(self, filename) -> None:
        self.filename = filename
        self.stack = None
        self.instructions = []
        self.instruction_pointer = 0
        self.labels = {}
        self.variables = {}
        self.load_instructions()

    def load_instructions(self):
        with open(self.filename, 'r') as f:
            for idx, line in enumerate(f):
                parts = shlex.split(line.strip()) # split by whitespace, ignoring whitespace in quotes, and remove quotes
                instruction_class = INSTRUCTION_MAP[parts[0]]
                args = parts[1:]
                instruction = instruction_class(self, idx, args)
                self.instructions.append(instruction)

    def run(self):
        self.stack = []
        self.instruction_pointer = 0
        total_instructions = len(self.instructions)
        while self.instruction_pointer < total_instructions:
            try:
                self.instructions[self.instruction_pointer].exec()
                self.instruction_pointer += 1
            except Exception as e:
                print(e)
                return

    def add_label(self, label, instruction_id):
        self.labels[label] = instruction_id

    def go_to_label(self, label):
        self.instruction_pointer = self.labels[label]

    def get_var_value(self, id):
        return self.variables[id]

    def set_var_value(self, id, value):
        self.variables[id] = value

    def pop(self):
        return self.stack.pop()

    def push(self, value):
        self.stack.append(value)
