class ProcCommands:
    def Proc(interpreter, env):
        interpreter.advance(1)
        proc_name = interpreter.code[interpreter.line][interpreter.index]
        interpreter.advance(1)
        code, line, index = interpreter.delim_code('}')
        code = code[1:-1]

        env.procedures[proc_name] = {
            "code": code,
            "file": interpreter.file,
            "line": interpreter.line + 1,
        }

        interpreter.line = line
        interpreter.index = index

    def OpenCurlyBracket(interpreter, _):
        code, line, index = interpreter.delim_code('}')
        code = code[1:-1]

        interpreter.subrun(code, interpreter.file, interpreter.start_line + interpreter.line + 1)

        interpreter.line = line
        interpreter.index = index

    def ProcParam(interpreter, _):
        param_index = len(interpreter.proc_params) - interpreter.param

        if param_index < 0:
            raise ValueError("Invalid parameter index.")
        
        interpreter.param = interpreter.proc_params[param_index]

    def Quit(interpreter, _):
        interpreter.line = len(interpreter.code)
        interpreter.index = 0

proc_commands = {
    "@": ProcCommands.Proc,
    "{": ProcCommands.OpenCurlyBracket,
    "$": ProcCommands.ProcParam,
    "q": ProcCommands.Quit,
}
