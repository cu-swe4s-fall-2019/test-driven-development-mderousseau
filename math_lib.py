""" Several math functions: mean and stdev"""
import sys
import math


def list_mean(L):
    """Compute the mean of an array. Expects nonempty array

    Parameters
    ----------
    L: list of numbers

    Returns
    -------
    m: mean of list of values

    """
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
    m = s/len(L)
    return(m)


def list_stdev(L):
    """Compute the stdev of an array. Expects nonempty array.

    Parameters
    ----------
    L: list of numbers

    Returns
    -------
    stdev: stdev of list of values

    """
    if L is None:
        return None
    if len(L) == 0:
        return None

    v = 0

    for l in L:
        try:
            v += (list_mean(L) - l)**2
        except TypeError:
            return None
    var = v/len(L)
    stdev = math.sqrt(var)
    return stdev
