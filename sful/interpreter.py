from sful.environment import Environment
from sful.commands import commands
import sful.util as util


class Interpreter:
    def __init__(
        self,
        code,
        file,
        line=0,
        index=0,
        env: Environment = None,
        proc_params=[],
    ):
        self.code = code.split("\n")
        self.file = file

        self.env = env or Environment()

        self.line = line
        self.index = index
        self.param = 1
        self.proc_params = proc_params

        self.delim_cache = dict()

    def run(self):
        while self.line < len(self.code):
            self.run_char()

    def run_char(self):
        if len(self.code[self.line]) == 0:
            self.advance()
            return
        
        command = self.code[self.line][self.index]

        if command in "0123456789":
            self.param = util.parse_param(self.code, self.line, self.index)
            self.advance(len(str(self.param)))

        command = self.code[self.line][self.index]

        if command in commands:
            commands[command](self, self.env)

        elif command in self.env.procedures:
            sub_int = Interpreter(
                self.env.procedures[command]["code"],
                self.env.procedures[command]["file"],
                proc_params=[*self.proc_params, self.param],
            )

            sub_int.run()

        if command not in "&%!$@":
            self.param = 1

        self.advance()

    def subrun(self, code, file):
        sub_int = Interpreter(
            code,
            file,
            env=self.env,
            proc_params=[*self.proc_params, self.param],
        )

        sub_int.run()

    def advance(self, steps=1):
        """
        Advances the pointer in the interpreter.
        """

        for _ in range(steps):
            self.index += 1

            if self.line >= len(self.code):
                return

            if self.index >= len(self.code[self.line]):
                self.line += 1
                self.index = 0


    def retreat(self, steps=1):
        """
        Advances the pointer in the interpreter.
        """

        for _ in range(steps):
            self.index -= 1

            if self.index < 0:
                self.line -= 1
                self.index = len(self.code[self.line]) - 1

    def match_delim(self, match: str, forward=True, nestable=True):
        """
        Matches a delimiter in the given code, but cached

        params:
            match (str): The delimiter to match.
            forward (bool): Whether to match forward or backward.
            nestable (bool): Whether the delimiter is nestable.
        """

        cache_key = f"{self.line}:{self.index}"

        if cache_key in self.delim_cache:
            return self.delim_cache[cache_key]

        delim = util.match_delim(
            self.code, self.line, self.index, match, forward, nestable
        )

        self.delim_cache[cache_key] = delim
        return delim

    def delim_code(self, match: str):
        """
        Gets the code between the current position and the matching delimiter.
        """

        line, index = self.match_delim(match)
        code = ""

        for i in range(self.line, line + 1):
            if i == line + 1:
                code += self.code[i][:index]
            else:
                code += self.code[i] + "\n"

        return (code, line, index)
