import getch


class InputCommands:
    def CellInput(interpreter, env):
        key = getch.getch()
        env.set(ord(key))

    def ParamInput(interpreter, env):
        key = getch.getch()
        interpreter.param = ord(key)


input_commands = {
    ",": InputCommands.CellInput,
    ";": InputCommands.ParamInput,
}
