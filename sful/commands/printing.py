from pprint import pprint


class PrintingCommands:
    def Space(interpreter, _):
        print(" " * interpreter.param, end="")

    def Line(interpreter, _):
        print("\n" * interpreter.param, end="")

    def Debug(interpreter, env):
        pprint(vars(interpreter))
        pprint(vars(env))

    def Char(interpreter, env):
        print(chr(env.get()), end="")

    def Number(interpreter, env):
        print(env.get(), end="")


printing_commands = {
    "_": PrintingCommands.Space,
    "n": PrintingCommands.Line,
    "~": PrintingCommands.Debug,
    ".": PrintingCommands.Char,
    "#": PrintingCommands.Number,
}
