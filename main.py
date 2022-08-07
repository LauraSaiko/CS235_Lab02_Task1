"""
The code is written for COMPSCI235 Lab 2 Git.

- You should work as a pair for this activity.
- Let the student who creates the repo be A, another student be B.

Tasks 1 -- Branching and merging
- Student A creates an empty public repo on GitHub (Do not include README nor
copy right file).
- Student A commits this project to the repo.
- Student A creates a `requirement.txt` file and commit it.
- Student A adds Student B as a collaborator.
- Student B clones the repo to B's local machine.
- Student B finds a correct `.gitignore` file, and commit it.
- Both students create and checkout a new branch, A's branch is called "rand",
and B's branch is called "coin".
- Student A implements the `get_rand()` function.
- Student B implements the `toss_coin()` function.
- For both students, commit your code, and then merge to main.
- Resolve the conflict.
- Remove your temporary branch.



Author: Luke Change (xcha011@aucklanduni.ac.nz)
Date: 23/07/2022
"""

import random

import numpy as np


MESSAGE = """Press "A" to get a random integer.
Press "B" to toss a coin.
Or enter an integer. It will return its factorial (n!).
Press "E" to exit.
"""


def get_factorial(value: int):
    '''Returns the factorial of the input value.'''
    list_values = np.arange(1, value + 1)
    factorial = list_values.prod()
    return factorial


def get_rand():
    '''Returns a random integer.'''
    """TODO: Add your code here 
        Hint: Using random.randint() function.
    """
    my_randint = 0
    return my_randint


def toss_coin():
    '''Return either Head or Tail'''
    """TODO: Add your code here
        Hint: Using random.randint() function.
    """
    number = random.randint(0, 2)
    if number == 0:
        coin = 'Head'
    else:
        coin = 'Tail'
    return coin


def read_input():
    my_input = input(MESSAGE)
    if my_input.lower() == 'e':
        exit()
    elif my_input.lower() == 'a':
        res = get_rand()
        print(res)
    elif my_input.lower() == 'b':
        res = toss_coin()
        print(res)
    elif my_input.isnumeric():
        res = get_factorial(int(my_input))
        print(f'{my_input}! = {res}')
    else:
        print(f'{my_input} is not a valid integer!')
    read_input()


if __name__ == '__main__':
    print('This is a toy toolbox.\nIt can do the following:')
    read_input()
