class PointerCommands:
    def Down(interpreter, env):
        env.row += interpreter.param

    def Up(interpreter, env):
        env.row -= interpreter.param

    def Right(interpreter, env):
        env.col += interpreter.param

    def Left(interpreter, env):
        env.col -= interpreter.param

    def Row(interpreter, env):
        env.row = interpreter.param

    def Col(interpreter, env):
        env.col = interpreter.param


pointer_commands = {
    "v": PointerCommands.Down,
    "^": PointerCommands.Up,
    ">": PointerCommands.Right,
    "<": PointerCommands.Left,
    "r": PointerCommands.Row,
    "c": PointerCommands.Col,
}
