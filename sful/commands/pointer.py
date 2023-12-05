class PointerCommands:
    def Down(interpreter, env):
        env.mem.row += interpreter.param

    def Up(interpreter, env):
        env.mem.row -= interpreter.param

    def Right(interpreter, env):
        env.mem.col += interpreter.param

    def Left(interpreter, env):
        env.mem.col -= interpreter.param

    def Row(interpreter, env):
        env.mem.row = interpreter.param

    def Col(interpreter, env):
        env.mem.col = interpreter.param


pointer_commands = {
    "v": PointerCommands.Down,
    "^": PointerCommands.Up,
    ">": PointerCommands.Right,
    "<": PointerCommands.Left,
    "c": PointerCommands.Row,
    "r": PointerCommands.Col,
}
