from sful.memory import Memory


class Environment:
    """
    Represents the environment in which procedures are executed.
    
    Attributes:
        mem (Memory): The memory object associated with the environment.
        procedures (dict): A dictionary of procedures available in the environment.

    Procedure Attributes:
        name (str): The name of the procedure.
        code (list[str]): The lines of code of the procedure.
        file (str): The file in which the procedure is defined.
        line (int): The line in the file in which the procedure is defined.
    """

    def __init__(self, memory: Memory = Memory(), procedures = dict()):
        self.mem = memory
        self.procedures = procedures