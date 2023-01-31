class Type():
    BOOL = 'bool'
    INT = 'int'
    FLOAT = 'float'
    STRING = 'string'
    ERROR = 'error'

# I could have made the class type have name, stack_symbol and default value
# instead of these maps, but w/e


StackTypeMap = {
    Type.BOOL: 'B',
    Type.INT: 'I',
    Type.STRING: 'S',
    Type.FLOAT: 'F'
}

TypeDefaultValueMap = {
    Type.BOOL: 'false',
    Type.INT: '0',
    Type.STRING: '""',
    Type.FLOAT: '0.0'
}
