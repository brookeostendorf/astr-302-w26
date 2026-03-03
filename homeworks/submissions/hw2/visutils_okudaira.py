#--------------------------------------------------------------------------------------------------#
# visutils_okudaira.py | ASTR 302 WINTER 2026 Homework-02                                          #
# Developed by Kiyoaki Okudaira * University of Washington                                         #
#--------------------------------------------------------------------------------------------------#
# History                                                                                          #
#--------------------------------------------------------------------------------------------------#
# coding 2026.02.02: 1st coding                                                                    #
#--------------------------------------------------------------------------------------------------#

#--------------------------------------------------------------------------------------------------#
# Libraries                                                                                        #
#--------------------------------------------------------------------------------------------------#
from astropy.table import Table
import numpy as np
import matplotlib.pyplot as plt
from ipywidgets import interact,fixed

#--------------------------------------------------------------------------------------------------#
# Main                                                                                             #
#--------------------------------------------------------------------------------------------------#
def load_and_prepare_cmd(
        filename : str
        ):
    """
    Load star table, filter data (-0.5<g-r<2.5 and 14<g<24) and return g and g-r array

    Parameters
    ----------
    filename: `str`
        PATH of star table file
    
    Returns
    -------
    g: `np.ndarray`
        array of g
    gr: `np.ndarray`
        array of g - r

    Notes
    -----
        This function was written for University of Washington ASTR 302 homework 2
        (c) 2026 Kiyoaki Okudaira - University of Washington
    """
    data = Table.read(filename)
    data["g-r"] = data["g"] - data["r"]
    mask = (14 < data["g"]) & (data["g"] < 24) & (-0.5 < data["g-r"]) & (data["g-r"] < 2.5)
    masked_data = data[mask]
    g = np.array(masked_data["g"])
    gr = np.array(masked_data["g-r"])
    return g,gr

def interactive_hess(
        g : np.ndarray,
        gr : np.ndarray
        ):
    """
    Generate an interactive Hess diagram given the data in g and g-r

    Parameters
    ----------
    g: `np.ndarray`
        array of g
    gr: `np.ndarray`
        array of g - r

    Notes
    -----
        This function was written for University of Washington ASTR 302 homework 2
        (c) 2026 Kiyoaki Okudaira - University of Washington
    """
    def plot_hess(g,gr,init_gridsize):
        fig, ax = plt.subplots(figsize=(7, 6))
        plt.subplots_adjust(bottom=0.18)
        
        hb = ax.hexbin(gr, g, gridsize=init_gridsize, bins="log")
        
        cbar = fig.colorbar(hb, ax=ax)
        cbar.set_label("log10(N)")
        
        ax.set_xlabel("g - r")
        ax.set_ylabel("g")
        ax.invert_yaxis()
        ax.set_title(f"Hess Diagram (gridsize={init_gridsize})")
    interact(plot_hess, g=fixed(g), gr=fixed(gr), init_gridsize=(50, 300, 1), continuous_update=True)

#--------------------------------------------------------------------------------------------------#
# Test                                                                                             #
#--------------------------------------------------------------------------------------------------#