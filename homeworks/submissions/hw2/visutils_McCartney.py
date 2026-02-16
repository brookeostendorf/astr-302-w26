#!/usr/bin/env python

import pandas as pd
import numpy as np
from ipywidgets import interact, fixed
import matplotlib.pyplot as plt

## Importing my stuff to have the useful modules

def load_and_prepare_cmd(filename):
    data_frame = pd.read_csv(filename)
    ## Read the file
    df_mask = (
        (data_frame['g'] > 14.0) & (data_frame['g'] < 24.0) &
        ((data_frame['g'] - data_frame['r']) > -0.5) & ((data_frame['g'] - data_frame['r']) < 2.5)
    )
    ## Mask the data frame to get the correct bands of data
    data_frame = data_frame[df_mask]
    ## New data frame witht he mask and return the values
    g = data_frame['g'].values
    gr = (data_frame['g'] - data_frame['r']).values
    return g, gr

def plot_hess(g, gr, gridsize = 100):
    ## THe plotting function for the hess diagram with the grid size and titles
    g = np.asarray(g)
    gr = np.asarray(gr)
    
    fig, ax = plt.subplots(figsize=(7, 6))

    inital_hb = ax.hexbin(
        g,
        gr,
        gridsize = gridsize,
        bins = "log"
    )

    cb = fig.colorbar(inital_hb, ax=ax)

    ax.set_xlabel("g")
    ax.set_ylabel("g-r")
    ax.set_title("Interactive Hess")

    return plt.show()

def interactive_hess(g, gr):
    interact(
        plot_hess, 
        g = fixed(g), 
        gr = fixed(gr), 
        gridsize = (50, 300, 1),
        continuous_update = False
    )

## The interactive function that with the slider will update the graph based on what value for gridsize