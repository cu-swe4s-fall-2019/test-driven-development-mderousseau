import sys
import math

def list_mean(L):
    if L is None:
        return None
    if len(L) == 0:
        return None
    
    s = 0
    
    for l in L:
        try:
            s += l
        except TypeError:
            return None
    return s/len(L)

def list_stdev(L):
    if L is None:
        return None
    if len(L) == 0:
        return None
    
    std = math.sqrt(sum([(list_mean(L)-x)**2 for x in L]) / len(L))
    return std
