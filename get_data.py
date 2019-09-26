import sys

# no tests due for stdin method at this point
def read_stdin_col():
    col_num = 0
    data_str = (sys.stdin.read().splitlines())
    # convert string of numbers to floats or integers
    data = [float(i) if '.' in i else int(i) for i in data_str]
    