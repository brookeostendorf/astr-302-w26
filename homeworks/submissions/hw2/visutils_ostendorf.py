import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from ipywidgets import interact, IntSlider


def load_and_prepare_cmd(filename):
    df = pd.read_csv(filename)

    g = df["g"].to_numpy()
    r = df["r"].to_numpy()
    gr = g - r

    mask = (
        (gr > -0.5) &
        (gr < 2.5) &
        (g > 14) &
        (g < 24)
    )

    return g[mask], gr[mask]


def interactive_hess(g, gr):

    def _plot(gridsize):
        plt.figure(figsize=(6, 8))
        hb = plt.hexbin(
            gr,
            g,
            gridsize=gridsize,
            bins= "log",
            cmap = "nipy_spectral"
        )
        plt.gca().invert_yaxis()
        plt.xlabel("g − r")
        plt.ylabel("g")
        plt.colorbar(hb, label="log(N)")
        plt.show()

    interact(_plot, gridsize=IntSlider(100, 50, 300, 1))
