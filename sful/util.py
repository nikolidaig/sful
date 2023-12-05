def parse_param(code: list[str], line: int, index: int):
    """
    Parses a parameter from the given code.

    Parameters:
        code (list[str]): The code to parse from.
        line (int): The line in the file in which the parameter is defined.
        index (int): The index in the line in which the parameter is defined.

    Returns:
        The parsed parameter.
    """
    param = code[line][index]

    while index + 1 < len(code[line]) and code[line][index + 1] in "0123456789":
        index += 1
        param += code[line][index]

    return int(param)


def match_delim(
    code: list[str], line: int, index: int, match: str, forward=True, nestable=True
):
    """
    Matches a delimiter in the given code.

    Parameters:
        line (iunt): The line in which the delimiter is defined.
        index (int): The index in the line in which the delimiter is defined.
        code (list[str]): The code to match from.
        match (str): The delimiter to match.
        forward (bool): Whether to match forward or backward.
        nestable (bool): Whether the delimiter is nestable.
    """

    ignore = code[line][index]
    depth = 1

    while depth > 0:
        if forward:
            index += 1
            if index >= len(code[line]):
                line += 1
                index = 0
        else:
            index -= 1
            if index < 0:
                line -= 1
                index = len(code[line]) - 1

        char = code[line][index]

        if char == ignore and nestable:
            depth += 1
        elif char == match:
            depth -= 1

    return (line, index)
