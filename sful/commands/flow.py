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

flow_commands = {
    "[": FlowCommands.OpenSquareBracket,
    "]": FlowCommands.CloseSquareBracket,
    "(": FlowCommands.OpenParen,
}
