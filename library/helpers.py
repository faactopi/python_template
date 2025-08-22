import sys
def one_more_time():
 pass
# Add 4 spaces (an extra level of indentation) to distinguish arguments from the rest.
def long_function_name(
        var_one:int, var_two, var_three,
        var_four):
    print(var_one)
    return var_one

class MyClass:
    """This is the documentation for MyClass."""

    def __init__(self):
        """This is the documentation for the __init__ method."""
        pass
    
def trim(docstring: str)-> str:
    """
    Trim indentation from docstrings.
    This is similar to Python's own trim function, which is
    not exposed through the API.
    The code is taken from PEP documentation : https://peps.python.org/pep-0257/
    
    Keyword arguments:
    Parameters:
    docstring (str): Input string to trim

    Returns:
    str: trimmed string 
    """
    if not docstring:
        return ''
    # Convert tabs to spaces (following the normal Python rules)
    # and split into a list of lines:
    lines = docstring.expandtabs().splitlines()
    # Determine minimum indentation (first line doesn't count):
    indent = sys.maxsize
    for line in lines[1:]:
        stripped = line.lstrip()
        if stripped:
            indent = min(indent, len(line) - len(stripped))
    # Remove indentation (first line is special):
    trimmed = [lines[0].strip()]
    if indent < sys.maxsize:
        for line in lines[1:]:
            trimmed.append(line[indent:].rstrip())
    # Strip off trailing and leading blank lines:
    while trimmed and not trimmed[-1]:
        trimmed.pop()
    while trimmed and not trimmed[0]:
        trimmed.pop(0)
    # Return a single string:
    return '\n'.join(trimmed)

