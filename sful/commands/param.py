class ParamCommands:
    def Column(interpreter, env):
        interpreter.param = env.mem.col

    def Row(interpreter, env):
        interpreter.param = env.mem.row

    def Cell(interpreter, env):
        interpreter.param = env.mem.get()


param_commands = {
    "&": ParamCommands.Column,
    "%": ParamCommands.Row,
    "!": ParamCommands.Cell,
}
