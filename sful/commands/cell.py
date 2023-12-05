class CellCommands:
    def Inc(interpreter, env):
        env.mem.inc(interpreter.param)

    def Dec(interpreter, env):
        env.mem.inc(-interpreter.param)

    def Set(interpreter, env):
        env.mem.set(interpreter.param)


cell_commands = {
    "+": CellCommands.Inc,
    "-": CellCommands.Dec,
    "=": CellCommands.Set,
}
