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
            print(value)
        elif instruction == "STORE_NAME":
            name, value = associated_data
            names[name] = value
        elif instruction == "LOAD_NAME":
            stack.append(names[name])
        elif instruction == "LOAD_LITERAL":
            stack.append(associated_data)
        else:
            print("WARNING: unknown instruction", instruction)

run_code([
    ("STORE_NAME", ("name", "Alice")),
    ("LOAD_NAME", "name"),
    ("LOAD_LITERAL", "Hello "),
    ("ADD_LAST_TWO", ()),
    ("PRINT", ())
])
