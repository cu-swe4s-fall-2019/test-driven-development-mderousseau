import sys

def read_stdin_col(col_number):
    file_name = sys.stdin
    try:
        file = open(file_name)
    except FileNotFoundError:
        raise FileNotFoundError(file_name + ' not found.')

