class FlowCommands:
    def OpenSquareBracket(interpreter, env):
        if env.get() == 0:
            interpreter.line, interpreter.index = interpreter.match_delim("]")

    def CloseSquareBracket(interpreter, env):
        if env.get() > 0:
            interpreter.line, interpreter.index = interpreter.match_delim(
                "[", forward=False
            )

    def OpenParen(interpreter, env):
        if env.get() > 0:
            interpreter.line, interpreter.index = interpreter.match_delim(")")

    def CloseParen(interpreter, env):
        if env.get() == 0:
            interpreter.line, interpreter.index = interpreter.match_delim(
                "(", forward=False
            )

    def SetCommand(interpreter, env):
        env.set(interpreter.param)


flow_commands = {
    "[": FlowCommands.OpenSquareBracket,
    "]": FlowCommands.CloseSquareBracket,
    "(": FlowCommands.OpenParen,
    ")": FlowCommands.CloseParen,
    "=": FlowCommands.SetCommand,
}
