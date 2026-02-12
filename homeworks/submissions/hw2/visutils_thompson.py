#!/usr/bin/env python

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from ipywidgets import interact, fixed

def load_and_prepare_cmd(filename):
    table = pd.read_csv(filename)
    table['gr'] = table['g'] - table['r']
    filtered_table = table.query("-0.5 < gr < 2.5 and 14 <g < 24")
    return filtered_table['g'].values, filtered_table['gr'].values
    
def interactive_hess(g, gr):
    def make_plot(size=100):
        fig, ax = plt.figure(figsize=(8, 5))
        
        hb = ax.hexbin(gr, g, gridsize=size, bins='log', cmap='inferno')
    
        fig.colorbar(label='log10(N)')
        ax.invert_yaxis()  
        ax.xlabel('g - r')
        ax.ylabel('g')
        
        plt.show()
    
    interact(make_plot, size=(50, 300, 1))
    