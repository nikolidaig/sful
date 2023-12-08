from sful.commands.cell import cell_commands
from sful.commands.flow import flow_commands
from sful.commands.input import input_commands
from sful.commands.other import other_commands
from sful.commands.param import param_commands
from sful.commands.pointer import pointer_commands
from sful.commands.printing import printing_commands
from sful.commands.proc import proc_commands

commands = {}
command_sets = [
    cell_commands,
    flow_commands,
    input_commands,
    other_commands,
    param_commands,
    pointer_commands,
    printing_commands,
    proc_commands,
]

for command_set in command_sets:
    for command in command_set:
        commands[command] = command_set[command]
