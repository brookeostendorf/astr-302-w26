import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from ipywidgets import interact, IntSlider

def load_and_prepare_cmd(filename):
    #Read csv file using pandas
    df = pd.read_csv(filename)
    #Convert the g and r columns of df into numpy arrays
    g = df['g'].to_numpy()
    r = df['r'].to_numpy()
    #Define conditions for the g band and apply them
    g_cut = (g > 14) & (g < 24)
    g = g[g_cut]
    #Computing cut on r to correct dimensionality for next step
    r = r[g_cut]
    #Compute g-r and then use conditions to cut the final arrays
    gr = g - r
    gr_cut = (gr > -0.5) & (gr < 2.5)
    #Cutting for both g and gr to satisfy both conditions
    gr = gr[gr_cut] 
    g = g[gr_cut]
    return g, gr

def interactive_hess(g, gr):
    #Create initial figure and then close to prevent automatic blank popup
    fig, ax = plt.subplots(figsize= (6,6))
    plt.close(fig)
    #Define a function to make the hexbin plot which can then be repeatedly called
    def hexplt(gridsize = 100):
        #Clear the plot to be able to iterate
        ax.clear()
        #Using hexbin
        hex = ax.hexbin(x = gr, y = g, gridsize = gridsize, bins='log')
        #Setting axis labels and titles
        ax.set_xlabel('g - r')
        ax.set_ylabel('g')
        ax.set_title(f'Hess Diagram (gridsize={gridsize})')
        ax.invert_yaxis()
        #Making sure to render and display the image with new inputs
        fig.show()
        display(fig)
    #Creating an interactable output with the correct minimum, maximum and step sizing.
    interact(hexplt, gridsize=(50,300,1), continuous_update=False)