## functional.py

The module includes the following functions:

**sequential_map**\
The function takes any number of functions as positional arguments (NOT a list) and a container with values, returns a list of the results of applying the passed functions sequentially to the values in the container.

**consensus_filter**\
The function takes any number of functions as positional arguments (NOT a list) that return True or False and a container with values.
The function returns a list of values that, when passed to all functions, got all True.

**conditional_reduce**\
The function takes 2 functions and a container with values as input.
The first function must take 1 argument and return True or False, the second takes 2 arguments
and returns a value (as in a regular reduce function). The conditional_reduce should returns one value that is the result of reduce, skipping the values with which the first function returned False.

**func_chain**\
func_chain takes any number of functions as positional arguments (NOT a list)and returns a function that combines all
passed ones by sequential execution.

**multiple_partial**\
multiple_partial is similar to partial function, however it takes an unlimited
number of functions as input and returns a list of the same number of "partial functions".

### Requirements
python>=3.6
