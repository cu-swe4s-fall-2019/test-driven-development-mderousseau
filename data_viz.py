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
    return None

def combo(L, out_file_name):
    return None
