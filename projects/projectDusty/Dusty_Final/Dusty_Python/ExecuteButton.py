#!/usr/bin/env python

import ipywidgets as widgets
from ipywidgets import interact, interact_manual
from IPython.display import display
import os

from Dusty_Python import Dusty_Class
from Dusty_Python import Dusty_Widgets
from Dusty_Python import Object_Attribution
from Dusty_Python import AttributeStringArray
from Dusty_Python import FileWriter

# A file that defines a button widget that runs functions to create the input file when clicked #

file = Dusty_Class.Dusty()

create_file_button = widgets.Button(
    description='Create Input File',
    button_style='success',
    style=dict(font_size="20px"),
    layout = widgets.Layout(width='200px', height='70px', margin='20px 0 30px 0', padding='10px',)
)

output = widgets.Output()

def on_button_clicked(b):
    with output:
        output.clear_output()
        Object_Attribution.attribution()
        contents = AttributeStringArray.inspect_attributes(file)
        FileWriter.write_inp_file(contents, folder_name="inp Files")
        print("File created successfully.")

create_file_button.on_click(on_button_clicked)


def Button():
    display(create_file_button, output)