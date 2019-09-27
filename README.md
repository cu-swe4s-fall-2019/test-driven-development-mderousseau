# test-driven-dev

## Project description
From a high level stand-point, this project allows the user to select a type of plot (from Histogram, Boxplot, or Combo), graph the plot, and save it to a file name of the user's choice. The input data can come from standard in, and the user has the ability to select a column if the standard in has several columns. Mean and standard deviations for the list of values are also calculated and plotted on the graph.

## How to use project
The user may run this project by running the following command in the terminal.

```
bash gen_data.sh | python viz.py --out_file_name out_file.png --plot_type 'Histogram'
```

Note that the '--out_file_name' can be a filename of the user's choice and the '--plot_type' can be 'Histogram', 'Boxplot', or 'Combo'

## How to install software
To use this project, you will need to create a conda environment with python 3 installed as well as the following libraries: pycodestyle, numpy, matplotlib, unittest, and statistics. However, a travis.yml file is included which will install dependencies and set up the required environment

