import sys

# no tests due for stdin method at this point
def read_stdin_col(col_num):
    L = []
    for l in sys.stdin:
        A = [int(x) for x in l.split()]
        L.append(int(A[col_num]))
    return(L)
    
