import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import sys
import os.path
from os import path

def boxplot(L, out_file_name):
    if path.exists(out_file_name) == True:
        return None
    width = 3
    height = 3
    fig = plt.figure(figsize=(width, height), dpi=300)
    ax = fig.add_subplot(1, 1, 1)
    ax.boxplot(L)
    plt.savefig(out_file_name, bbox_inches="tight")


def histogram(L, out_file_name):
    if path.exists(out_file_name) == True:
        return None
    width = 3
    height = 3
    fig = plt.figure(figsize=(width, height), dpi=300)
    ax = fig.add_subplot(1, 1, 1)
    ax.hist(L)
    plt.savefig(out_file_name, bbox_inches="tight")

def combo(L, out_file_name):
    if path.exists(out_file_name) == True:
        return None
    fig, (ax1, ax2) = plt.subplots(1, 2)
    fig.suptitle("Mean, Std")
    ax1.hist(L)
    ax2.boxplot(L)
    plt.savefig(out_file_name, bbox_inches="tight")

combo([1,2,3,4], 'out_file.png')
