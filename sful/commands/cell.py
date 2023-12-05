class CellCommands:
    def Inc(interpreter, env):
        env.inc(interpreter.param)

    def Dec(interpreter, env):
        env.inc(-interpreter.param)

    def Set(interpreter, env):
        env.set(interpreter.param)


cell_commands = {
    "+": CellCommands.Inc,
    "-": CellCommands.Dec,
    "=": CellCommands.Set,
}
