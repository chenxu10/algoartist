import re

def lexing(s):
    parsed_lists = re.split(r'Given|return|such that', s)
    return parsed_lists

def parsing():
    pass

def parse_into_trees(problem_statements):
    """
    Understand the problem, what's know, unknown,
    what's condition and what's relationships
    between them?
    """
    return lexing(problem_statements)
    