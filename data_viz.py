""" Several functions for plotting including
    histogram, boxplot, and a combo plot."""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import sys
import os.path
from os import path
import math_lib


def boxplot(L, out_file_name):
    # check to see if the path already exists
    if path.exists(out_file_name) is True:
        return None
    width = 3
    height = 3
    fig = plt.figure(figsize=(width, height), dpi=300)

    # calc mean and stdev for titling the plot
    mean = round(math_lib.list_mean(L), 4)
    stdev = round(math_lib.list_stdev(L), 4)

    ax = fig.add_subplot(1, 1, 1)
    ax.set_ylabel('Value')
    ax.set_title('Mean: ' + str(mean) + ' Stdev: ' + str(stdev))
    ax.boxplot(L)
    plt.savefig(out_file_name, bbox_inches="tight")


def histogram(L, out_file_name):
    if path.exists(out_file_name) is True:
        return None
    width = 3
    height = 3
    mean = round(math_lib.list_mean(L), 4)
    stdev = round(math_lib.list_stdev(L), 4)
    fig = plt.figure(figsize=(width, height), dpi=300)
    ax = fig.add_subplot(1, 1, 1)
    ax.hist(L)
    ax.set_ylabel('Frequency')
    ax.set_xlabel('Value')
    ax.set_title('Mean: ' + str(mean) + ' Stdev: ' + str(stdev))
    plt.savefig(out_file_name, bbox_inches="tight")


def combo(L, out_file_name):
    if path.exists(out_file_name) is True:
        return None
    mean = round(math_lib.list_mean(L), 4)
    stdev = round(math_lib.list_stdev(L), 4)
    fig, (ax1, ax2) = plt.subplots(1, 2)
    fig.suptitle('Mean: ' + str(mean) + ' Stdev: ' + str(stdev))
    ax1.hist(L)
    ax1.set_ylabel('Frequency')
    ax1.set_xlabel('Value')
    ax2.boxplot(L)
    ax2.set_ylabel('Value')
    plt.savefig(out_file_name, bbox_inches="tight")
