class Memory:
    """
    A class representing a memory matrix

    Attributes:
    - memory (dict[str, int]): A dictionary that stores the values at different pointers.
    - row (int): The current row position in the memory.
    - col (int): The current column position in the memory.
    """

    def __init__(self):
        self.memory: dict[str, int] = {}
        self.row = 0
        self.col = 0

    def get(self):
        """Returns the value at the current pointer, or 0 if it doesn't exist."""
        pointer = f"{self.row},{self.col}"

        if pointer not in self.memory:
            return 0

        return self.memory[pointer]

    def set(self, value: int):
        """Sets the value at the current pointer, or deletes it if the desired value is 0"""
        if value == 0:
            self.delete()

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
