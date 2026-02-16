#!/usr/bin/env python

# ----------------------------------------------------------------------------------------
# Visutils_soh.py - ASTR 302 Winter 2026 Homework 2
# Programmed by Aria Soh @ University of Washington 2/11/2026

# Task - Read a csv file for g and g-r and plot them using an interactive Hess diagram 
# with interactive gridsize
# ----------------------------------------------------------------------------------------

# Command to load a specific csv file into a Pandas dataframe provdided it has the proper format
def load_and_prepare_cmd(filename):

    # Importing the packages inside the function so they can be called in any notebook even if that notebook doesn't already have the packages
    import pandas as pd
    import numpy as np

    # Csv_whole is generated the Pandas dataframe, containing all the columns of the data
    csv_whole = pd.read_csv(filename, 
            sep=",", header=None, skiprows=1, 
            names=['l', 'b', 'g', 'r', 'err_g', 'err_r', 'flags'])

    # Adding a column g-r, which takes g - r for every row in the dataframe 
    csv_whole['g-r'] = (csv_whole['g'] - csv_whole['r'])

    # Paring the csv so that it only includes rows who have g and g-r values that satisfy both these contidions
    csv_pared = csv_whole[
        (csv_whole['g'].between(14, 24, inclusive="neither")) 
        & (csv_whole['g-r'].between(-0.5, 2.5, inclusive="neither"))]

    # Setting the data in each of the pared columns to numpy arrays
    g = csv_pared['g'].to_numpy()
    gr = csv_pared['g-r'].to_numpy()

    # Returns two numpy arrays, g and gr
    return (g, gr)

# ----------------------------------------------------------------------------------------

# Command to display an interactive Hess diagram from two numpy arrays of g-band magnitude (g) and g-band mag - r-band mag (gr)
def interactive_hess(g, gr):

    # Importing the packages inside function so it can be called in any notebook even if that notebook doesn't already have the packages
    from ipywidgets import interact, fixed
    import matplotlib.mlab as mlab
    import matplotlib.pyplot as plt

    # Defining a nested function to plot the Hess diagram (necessary to create a slider)
    def plot_hess(g, gr, gridsize_val=100):

        # Defining the plot type and size
        fig, ax = plt.subplots(figsize=(9, 4))

        # Setting limits of the axes to the limitations put on the data from load_and_prepare_cmd()
        ax.set_xlim(xmin=14, xmax = 24)
        ax.set_ylim(ymin=-0.5, ymax=2.5)

        # Since this is graphing magnitudes on both axes, both axes have to be inverted because higher magnitude means dimmer object
        ax.invert_xaxis()
        ax.invert_yaxis()
        
        # Plotting the hexbin with x=g, y=gr, gridsize is an input var with init val 100, the bins are log (color log scale) and I think inferno just looks nice
        init_hxb = ax.hexbin(g, gr, gridsize=gridsize_val, bins='log', cmap='inferno')

        # Creating a color bar to understand what colors correspond to what values
        cb = fig.colorbar(init_hxb, ax=ax)

        # Labelling the plot
        ax.set_xlabel('g', 
                     fontfamily = 'serif',
                     fontsize = 15)
        ax.set_ylabel('g-r', 
                     fontfamily = 'serif',
                     fontsize = 15)
        ax.set_title('Interactive Hess With a Log Color Scale', 
                     fontfamily = 'serif',
                     fontsize = 15)
        
        # Hashmarks on axes for clarity
        ax.tick_params(axis='both', which='major', labelsize = 12)
        
        # Returns the plot generated with these parameters
        return plt.show()

    # Interactive widget that runs the function plot_hess (replots it) keeping g and gr fixed but changing the gridsize in steps of 1 from 50-300
    interact(plot_hess, g=fixed(g), gr=fixed(gr), gridsize_val=(50, 300, 1), continuous_update=False)

# ----------------------------------------------------------------------------------------