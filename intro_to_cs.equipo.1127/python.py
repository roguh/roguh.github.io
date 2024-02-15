"""python.py - A small Python interpreter.

ROGUH 2019
"""

import ast


def print_error(message, expression, source):
    print(f"ERROR: {message}")
    print("at node", ast.dump(expression))

    if hasattr(ast, 'get_source_segment'):
        print(f"at code '{ast.get_source_segment(source, expression)}'")


def parse_string(source):
    abstract_syntax_tree = ast.parse(source)
    instructions = []

    def err(*args):
        print_error(*args, source=source)

        return []

    def instruct(instruction, associated_data=[]):
        instructions.append([instruction, associated_data])

    def expr(subexpression):
        """Emits LOAD_LITERAL, LOAD_VAR, and ADD_LAST_TWO instructions."""
        type_ = type(subexpression)

        # ADD_LAST_TWO

        if type_ is ast.BinOp:
            if type(subexpression.op) is ast.Add:
                expr(subexpression.right)
                expr(subexpression.left)
                instruct("ADD_LAST_TWO")
            else:
                err("unknown binary op", subexpression)

        # LOAD_LITERAL
        elif type_ is ast.Constant:
            literal_value = subexpression.value
            instruct("LOAD_LITERAL", literal_value)

        # LOAD_VAR
        elif type_ is ast.Name:
            var_name = subexpression.id
            instruct("LOAD_VAR", var_name)
        else:
            err("unknown expression", subexpression)

    for expression in abstract_syntax_tree.body:
        type_ = type(expression)


        # STORE_TO_VAR
        if type_ is ast.Assign:
            if len(expression.targets) != 1:
                err("too many variable assignment targets", expression)

            expr(expression.value)

            var_name = expression.targets[0].id
            instruct("STORE_TO_VAR", var_name)
        # PRINT
        elif type_ is ast.Expr:
            value = expression.value

            if type(value) is ast.Call:
                if type(value.func) is not ast.Name or value.func.id != "print":
                    err("unknown function", expression)

                for arg in value.args:
                    expr(arg)
                    instruct("PRINT")
            else:
                err("unknown expression", expression)
        else:
            err("unknown expression", expression)

    return instructions

def run_code(instructions):
    names = dict()
    stack = list()

    for each_step in instructions:
        instruction, associated_data = each_step

        if instruction == "ADD_LAST_TWO":
            result = stack.pop() + stack.pop()
            stack.append(result)
        elif instruction == "PRINT":
            value = stack.pop()
            print(value, end='')
        elif instruction == "STORE_TO_VAR":
            value = stack.pop()
            name = associated_data
            names[name] = value
        elif instruction == "LOAD_VAR":
            name = associated_data
            stack.append(names[name])
        elif instruction == "LOAD_LITERAL":
            stack.append(associated_data)
        else:
            print("ERROR: unknown instruction", instruction)

            break

run_code([
    ["LOAD_LITERAL", "Alice"],
    ["STORE_TO_VAR", "name"],
    ["LOAD_VAR", "name"],
    ["LOAD_LITERAL", "Hello "],
    ["ADD_LAST_TWO", []],
    ["PRINT", []]
])

# CHALLENGE: MAKE THIS INTERPRETER INTERPRET ITSELF!!!!
