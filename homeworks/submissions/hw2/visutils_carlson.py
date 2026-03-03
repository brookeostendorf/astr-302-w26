def load_and_prepare_cmd(filename):
    import pandas as pd
    
    fieldA = pd.read_csv('fieldA.csv')                    

    #defines a new column of values 'g-r'
    fieldA['g-r'] = fieldA['g'] - fieldA['r']                 

    #creates new table with the given parameters
    filtered_fieldA = fieldA[                                 
        (fieldA['g-r'] > -0.5) &
        (fieldA['g-r'] < 2.5) &
        (fieldA['g'] > 14) &
        (fieldA['g'] < 24)]

    #returns just 'g' and 'g-r' values within the parameters
    return filtered_fieldA['g'], filtered_fieldA['g-r']

(g, gr) = load_and_prepare_cmd('fieldA.csv')




def interactive_hess(g, gr):
    import matplotlib.pyplot as plt
    from ipywidgets import interact, interactive, fixed
    import ipywidgets as widgets

    #creates plot with variable gridsize
    def plot(gridsize):
        plt.figure(figsize=(10, 8))
        plt.hexbin(gr, g, bins='log', gridsize=gridsize, cmap='viridis')
        
        plt.xlabel('g-r')
        plt.ylabel('g')
        plt.gca().invert_yaxis()
        plt.colorbar(label='log10')
        plt.show()
        
    #creates slider to change gridsize
    widgets.interact(plot, gridsize = widgets.IntSlider(min=50, max=300, step=1, value=100))