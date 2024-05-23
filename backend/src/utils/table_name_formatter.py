def camel_case_to_snake_case(input: str) -> str:
    output = []
    first_char = True
    for char in input:
        if not first_char and char.isupper():
            output.append("_")
        output.append(char.lower())
        first_char = False
    return "".join(output)
