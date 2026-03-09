#!/usr/bin/env python

import ipywidgets as widgets
from ipywidgets import interact, interact_manual
from IPython.display import display
import os

#Function that creates a new file and writes strings from an array into said file#

def write_inp_file(contents, folder_name="inp Files"):
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)
    
    last_item = contents[-1] 
    file_name_val = last_item.split('=')[-1].strip().replace("'", "").replace('"', "")

    file_path = os.path.join(folder_name, f"{file_name_val}.inp")
    
    with open(file_path, "w", encoding="utf-8") as f:
        f.write('\n'.join(contents))
        
    return