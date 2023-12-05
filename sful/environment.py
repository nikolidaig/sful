class Environment:
    """
    Represents the environment in which procedures are executed.

    Attributes:
        memory (dict[str, int]): A dictionary that stores the values at different pointers.
        row (int): The current row position in the memory.
        col (int): The current column position in the memory.
        procedures (dict): A dictionary of procedures available in the environment.

    Procedure Attributes:
        name (str): The name of the procedure.
        code (list[str]): The lines of code of the procedure.
        file (str): The file in which the procedure is defined.
        line (int): The line in the file in which the procedure is defined.
    """

    def __init__(
        self, memory: dict[str, int] = dict(), row=0, col=0, procedures=dict()
    ):
        self.memory = memory
        self.row = row
        self.col = col
        self.procedures = procedures

    def get(self):
        """Returns the value at the current pointer, or 0 if it doesn't exist."""
        pointer = f"{self.row},{self.col}"

        if pointer not in self.memory:
            return 0

        return self.memory[pointer]

    def set(self, value: int):
        """Sets the value at the current pointer, or deletes it if the desired value is 0"""
        if value == 0:
            return self.delete()

        if value < 0:
            raise ValueError("Cannot set cell to a negative value")

        pointer = f"{self.row},{self.col}"

        self.memory[pointer] = value

    def inc(self, value: int):
        """Increments the value at the current pointer"""
        value += self.get()
        self.set(value)

    def delete(self):
        """Deletes the value at the current pointer"""
        pointer = f"{self.row},{self.col}"

        if pointer in self.memory:
            del self.memory[pointer]
