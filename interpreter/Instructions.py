def bool_convertor(x):
    if x == 'true':
        return True
    elif x == 'false':
        return False
    raise Exception(f"Cannot convert '{x}' to bool")

TYPE_FUNC_MAP = {
    'F': float,
    'I': int,
    'B': bool_convertor,
    'S': str
}


class Instruction:
    def __init__(self, interpreter, id, args) -> None:
        self.interpreter = interpreter
        self.id = id
        self.args = args

    def exec(self):
        pass


class BinaryOperation(Instruction):
    def exec(self):
        right = self.interpreter.pop()
        left = self.interpreter.pop()
        result = self.do_operation(left, right)
        self.interpreter.push(result)

    def do_operation(self, a, b):
        pass


class UnaryOperation(Instruction):
    def exec(self):
        value = self.interpreter.pop()
        result = self.do_operation(value)
        self.interpreter.push(result)

    def do_operation(self, value):
        pass


class Add(BinaryOperation):
    def do_operation(self, a, b):
        return a + b


class Substract(BinaryOperation):
    def do_operation(self, a, b):
        return a - b


class Multiply(BinaryOperation):
    def do_operation(self, a, b):
        return a * b


class Divide(BinaryOperation):
    def do_operation(self, a, b):
        # I don't have to check type(b), because if one was int and one float, there had to be IntToFloat instruction before
        # Therefore, if I check for type(b) here, the IntToFloat instruction is completely redundant
        if (type(a) == int):
            return a // b
        else:
            return a / b


class Modulo(BinaryOperation):
    def do_operation(self, a, b):
        return a % b


class LogicalAnd(BinaryOperation):
    def do_operation(self, a, b):
        return a and b


class LogicalOr(BinaryOperation):
    def do_operation(self, a, b):
        return a or b


class GreaterThan(BinaryOperation):
    def do_operation(self, a, b):
        return a > b


class LessThan(BinaryOperation):
    def do_operation(self, a, b):
        return a < b


class Concat(BinaryOperation):
    def do_operation(self, a, b):
        return a + b


class Equal(BinaryOperation):
    def do_operation(self, a, b):
        return a == b


class UnaryMinus(UnaryOperation):
    def do_operation(self, value):
        return -value


class LogicalNot(UnaryOperation):
    def do_operation(self, value):
        return not value


class IntToFloat(UnaryOperation):
    def do_operation(self, value):
        return float(value)


class Push(Instruction):
    def __init__(self, interpreter, id, args) -> None:
        super().__init__(interpreter, id, args)
        self.convertor = TYPE_FUNC_MAP[self.args[0]]
        self.value = self.convertor(self.args[1])

    def exec(self):
        self.interpreter.push(self.value)


class Pop(Instruction):
    def exec(self):
        self.interpreter.pop()


class Load(Instruction):
    def exec(self):
        value = self.interpreter.get_var_value(self.args[0])
        self.interpreter.push(value)


class Save(Instruction):
    def exec(self):
        value = self.interpreter.pop()
        self.interpreter.set_var_value(self.args[0], value)


class Label(Instruction):
    def __init__(self, interpreter, id, args) -> None:
        super().__init__(interpreter, id, args)
        # I can keep the labels as strings
        self.interpreter.add_label(self.args[0], id)


class Jump(Instruction):
    def exec(self):
        self.interpreter.go_to_label(self.args[0])


class FalseJump(Jump):
    def exec(self):
        value = self.interpreter.pop()
        if not value:
            super().exec()


class Print(Instruction):
    def get_display_value(self, value):
        if type(value) == bool:
            return 'true' if value else 'false'
        return value

    def exec(self):
        n = int(self.args[0])
        values = []
        for i in range(n):
            value = self.interpreter.pop()
            values.append(self.get_display_value(value))
        for value in reversed(values):
            print(value, end='')
        print()


class Read(Instruction):
    def __init__(self, interpreter, id, args) -> None:
        super().__init__(interpreter, id, args)
        self.convertor = TYPE_FUNC_MAP[self.args[0]]

    def exec(self):
        try:
            value = self.convertor(input())
            self.interpreter.push(value)
        except Exception as e:
            raise e


INSTRUCTION_MAP = {
    'add': Add,
    'sub': Substract,
    'mul': Multiply,
    'div': Divide,
    'mod': Modulo,
    'uminus': UnaryMinus,
    'concat': Concat,
    'and': LogicalAnd,
    'or': LogicalOr,
    'gt': GreaterThan,
    'lt': LessThan,
    'eq': Equal,
    'not': LogicalNot,
    'itof': IntToFloat,
    'push': Push,
    'pop': Pop,
    'load': Load,
    'save': Save,
    'label': Label,
    'jmp': Jump,
    'fjmp': FalseJump,
    'print': Print,
    'read': Read,
}
