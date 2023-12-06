class OtherCommands:
    def Comment(interpreter, _):
        interpreter.line += 1
        interpreter.index = -1
        
    def ImportFile(interpreter, _):
        filename = interpreter.code[interpreter.line][interpreter.index + 1 :]
        interpreter.line += 1
        interpreter.index = -1
        
        with open(filename, "r") as f:
            code = f.read()
            interpreter.subrun(code, filename, 1)


other_commands = {
    "*": OtherCommands.Comment,
    "'": OtherCommands.ImportFile,
}
