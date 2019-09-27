""" Function that will take a column number and
    select that column from stdin."""
import sys


def read_stdin_col(col_num):
    L = []
    for l in sys.stdin:
        A = [int(x) for x in l.split()]
        L.append(int(A[col_num]))
    return(L)
# no tests due for stdin method at this point
