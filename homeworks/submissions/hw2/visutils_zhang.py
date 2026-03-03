import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from ipywidgets import interact

df = pd.read_csv('fieldA.csv')

g = df["g"]
r = df["r"]
gr = g - r

filter_data = (g > 14) & (g < 24) & (gr > -0.5) & (gr < 2.5)

g_clean = g[filter_data]
gr_clean = gr[filter_data]

def interactive_hess(g, gr):

    def plot(gridsize):
        plt.clf()
        plt.hexbin(gr, g, gridsize=gridsize, bins='log')
        plt.xlabel('g - r')
        plt.ylabel('g')
        plt.gca().invert_yaxis()
        plt.colorbar()
        plt.show()

    interact(plot, gridsize=(50, 300, 1))

interactive_hess(g_clean, gr_clean)
