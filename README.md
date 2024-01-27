# So-Far Unnamed Language

A somewhat backwards-compatible extension of Brainfuck, written in python. Here's example that multiplies 123 by 456 by repeated addition and prints the result:

    @×{
        &{                  * Store original cell column
            2C              * Claim 2 columns of memory
            $c              * Move to original cell
            !{ 2m $= }      * Copy value to memory col 1 (iterations left)
            [ - > 2$+ < ]   * Repeat addition in col 2 (running total)
            > !{ 2$c $= }   * Replace original cell with result
            2R              * Release memory
        }
    }
    
    123s 456× #n

## Memory

Memory is stored on an infinite 2-dimensional matrix of unsigned integers. Each cell's value is zero until it is set to a nonzero value. At runtime, a row and column pointer stores the selected cell's position. Setting a cell or pointer to a non-uint value raises an error

## Commands

Commands are run on the data in the selected cell, the pointers, and a parameter. The parameter is equal to 1 by default, but any number can be given before the command: `+++` is therefore equal to `3+`.

### Pointer Commands

    >   Increment column pointer by parameter 
    <   Decrement column pointer 
    v   Increment row pointer 
    ^   Decrement row pointer 
    c   Set column pointer to parameter 
    r   Set row pointer to parameter 

\*Note that the down arrow _increments_ the row pointer.

### Cell Commands

    +   Increment cell by parameter 
    -   Decrement cell by parameter 
    =   Set cell to parameter 

### Printing Commands

    _   Print spaces parameter times 
    n   Print newlines parameter times 
    ~   Print debug information 
    .   Print cell value as a character 
    #   Print cell value as an integer 

### Parameter Commands

The parameter commands set the parameter for the following command.

    &   Set parameter to selected column
    %   Set parameter to selected row
    !   Set parameter to cell value

### Other Commands

    *       Starts a comment, which ends at the next line break
    'file   Runs an external file

## Control Flow and Procedures

    [       Continue if cell value is greater than zero, jump forward to ] if zero
    ]       Jump back to [ if cell value greater than zero, continue if zero
    (       Continue if cell value is zero, jump forward to ) if greater

Procedures are strings of code that can be run at a later time. For example, if a procedure `@a{+}` is defined, then each time `a` is called thereafter, the then selected cell will be incremented. A procedure can take a parameter and use it within the code using the `$` parameter command. For example, the procedure `@a{$+}` can be used with a parameter to increment a cell by a value: `6a` will then be equivalent to `6+`. The default parameter for all defined procedures is 1. Defining a procedure whose symbol is a built-in command already will not change the function of the command, doing nothing.

    @a{...} Defines new procedure named a
    $       Sets parameter to procedure parameter
    a       Runs procedure named a
    q       Quits running procedure

Using the `{}` brackets without `@` starts an anonymous procedure, which is run immediately. Using `$` inside an anonymous procedure and a parameter before the `{` lets you "cast" a parameter accross later commands. For example, to copy a cell's value to the next column over, use `!{>$=}`. Nested anonymous procedures are allowed, and to use the parameter of a parent procedure, use `2$`, or `3$` for the grandparent, etc.