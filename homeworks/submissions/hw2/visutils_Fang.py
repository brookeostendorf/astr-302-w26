import pandas as pd
from ipywidgets import interact, fixed
import matplotlib.pyplot as plt

def load_and_prepare_cmd(filename):
    """
    Load a csv file into a pandas dataframe
    Filter out g and g-r columns with a value range
    Output a dataframe with g and g-r columns
    """
    try:
        raw_df = pd.read_csv(filename)
    except FileNotFoundError:
        print(f"Error: Input file not found.")
        return None, None

    raw_df['g-r'] = raw_df['g'] - raw_df['r']
    flt_df = raw_df.query("24 > g > 14 and 2.5 > `g-r` > -0.5")
    return flt_df['g'], flt_df['g-r']

def plt_hess(g, gr, gridsize = 100):
    """
    Takes in a dataframe (g, gr) and outputs a Hess diagram with g-r on the x-axis and g on the y-axis
    gridsize is kept as a variable for ipywidgets
    """
    if g is None or len(g) == 0:
        print("No data")
        return
    
    fig, ax = plt.subplots(
    figsize = (8, 8), 
    constrained_layout = True
    )
        
    hess = ax.hexbin(
    x = gr,
    y = g,
    gridsize = gridsize,
    bins='log',
    cmap='magma',
    )

    ax.invert_xaxis()
    ax.invert_yaxis()
    ax.set_xlabel("g - r (color)",
                    fontfamily = 'serif',
                    fontsize = 13)
    
    ax.set_ylabel("g (mag)",
                    fontfamily = 'serif',
                    fontsize = 13)
        
    ax.set_title("g-r vs g",
                    fontfamily = 'serif',
                    fontsize = 17);

def interactive_hess(g, gr):
    """
    Generate a grid size slider for the Hess diagram
    slider range: 50 to 300 with 100 default
    """
    interact(plt_hess, g=fixed(g), gr=fixed(gr), gridsize=(50, 300, 1), continuous_update=False)