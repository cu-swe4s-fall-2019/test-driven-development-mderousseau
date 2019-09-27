""" script that allows the user to select plot type
and an output file name for plotting the distribution
of values from a column of stdin. """
import get_data
import math_lib
import data_viz
import argparse
import sys


def main():
    # L coming from stdin from get_data method
    L = get_data.read_stdin_col(0)

    parser = argparse.ArgumentParser(description='inputs\
                                     for file name and \
                                     type of plot',
                                     prog='viz.py')

    parser.add_argument('--plot_type',
                        type=str,
                        help='Choice of plot: Boxplot, Histogram, or Combo',
                        required=True)

    parser.add_argument('--out_file_name',
                        type=str,
                        help='Name of output file',
                        required=True)

    args = parser.parse_args()

    try:
        if args.plot_type == 'Boxplot':
            data_viz.boxplot(L, args.out_file_name)
        elif args.plot_type == 'Histogram':
            data_viz.histogram(L, args.out_file_name)
        elif args.plot_type == 'Combo':
            data_viz.combo(L, args.out_file_name)
        else:
            print("Must choose from: 'Histogram', 'Boxplot', or 'Combo'")
    except ValueError:
        print('Must have correct file extension. Try .png?')


if __name__ == '__main__':
    main()
