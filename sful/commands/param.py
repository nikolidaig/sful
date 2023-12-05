class ParamCommands:
    def Column(interpreter, env):
        interpreter.param = env.col

    def Row(interpreter, env):
        interpreter.param = env.row

    def Cell(interpreter, env):
        interpreter.param = env.get()


param_commands = {
    "&": ParamCommands.Column,
    "%": ParamCommands.Row,
    "!": ParamCommands.Cell,
}
