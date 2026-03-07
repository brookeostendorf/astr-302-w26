#!/usr/bin/env python

import ipywidgets as widgets
from ipywidgets import interact, interact_manual
from IPython.display import display, HTML

# A file that conatins the code for all the ipywidgets in the input notebook #

#Notebook Header
title = widgets.Label(value='Dusty Input',style=dict(font_size="28px"))

#File Name
label_input_name = widgets.Label(value='Input File Name:')
input_name = widgets.Text(
                placeholder='Name File',
                disabled=False
            )
name_tb = widgets.HBox([label_input_name, input_name])

##################################################################

#
#External Radiation
#

#Spectrum Types

#Combination Black Body
bb_slider = widgets.IntSlider(
                value=1,
                min=1,
                max=10,
                step=1,
                disabled=False,
                continuous_update=False,
                orientation='horizontal',
                readout=True,
                readout_format='d'
            )

temps_tb = widgets.Text(
    placeholder='Type numbers separated by commas (e.g. 100, 200)',
    layout=widgets.Layout(width='320px')
)

lums = widgets.Text(
    placeholder='Type numbers separated by commas (e.g. 100, 200)',
    layout=widgets.Layout(width='320px')
)
    
lums_tb = widgets.HBox([])
def lums_visibility(change):
    value = change['new']
    lums_tb.children = []
    if value == 1:
        lums_tb.children = [] 
    else:
        lums_tb.children = [
            widgets.Label(value='Fractional Luminosities:'),
            lums
        ]

bb_slider.observe(lums_visibility, names='value')

lums_visibility({'new': bb_slider.value})

cbb_box = widgets.VBox([
widgets.Label("Combination Black Body", style=dict(font_size="16px")),
widgets.HBox([widgets.Label(value='Number of Black Bodies:'), bb_slider]),
widgets.HBox([widgets.Label(value='Temperatures (K):'), temps_tb]),
widgets.HBox([lums_tb])
])

#Broken Power Law
N_functions_itb = widgets.BoundedIntText(
            value=1,
            min=1,
            step=1,
            disabled=False
)

lambdas_tb = widgets.Text(
    placeholder='Type numbers separated by commas (e.g. 100, 200)',
    layout=widgets.Layout(width='320px')
)

power_indicies_tb = widgets.Text(
    placeholder='Type numbers separated by commas (e.g. 100, 200)',
    layout=widgets.Layout(width='320px')
)

bpl_box = widgets.VBox([
widgets.Label("Broken Power Law", style=dict(font_size="16px")),
widgets.HBox([widgets.Label(value='Number of Power Law segments:'), N_functions_itb]),
widgets.HBox([widgets.Label(value='Breakpoint Wavelengths (λ in µm)'), lambdas_tb]),
widgets.HBox([widgets.Label(value='Power Indicies (k):'), power_indicies_tb])
])

#Engelke-Marengo Function
tbb_temp_tb = widgets.Text(
    layout=widgets.Layout(width='320px')
)

sio_fd_slider = widgets.FloatSlider(
                value=1.0,
                min=0.1,
                max=100.0,
                step=0.1,
                disabled=False,
                continuous_update=False,
                orientation='horizontal',
                readout=True,
                readout_format='.1f'
)

emf_box = widgets.VBox([
widgets.Label("Engelke-Marengo Function", style=dict(font_size="16px")),
widgets.HBox([widgets.Label(value='Temperature (K):'), tbb_temp_tb]),
widgets.HBox([widgets.Label(value='SiO Feature Depth (%):'), sio_fd_slider])
])

#File: lambdaFvlambda, Fvlambda, Fvv vs. lambda
er_files_tb = widgets.Text(
    layout=widgets.Layout(width='320px')
)

er_file_box = widgets.VBox([
widgets.Label("File", style=dict(font_size="16px")),
widgets.HBox([widgets.Label(value='File Name (file must have λ in µm):'), er_files_tb])
])


#Spectrum
spectrum_values = [
    ('--Select Spectrum Type--', ''),
    ('Combination Black Body', 1),
    ('Broken Power Law', 2),
    ('Engelke-Marengo Function', 3),
    ('File: λ F_λ', 4),
    ('File: F_λ', 5),
    ('File: F_ν vs. λ', 6)  
]

label_spectrum = widgets.Label(value='Spectrum Type:')
spectrum = widgets.Dropdown(
    options=spectrum_values,
    value='',
    continuous_update=True,
    disabled=False)

er_section = widgets.VBox([])

def er_visibility(change):
            value = change['new']
            er_section.children = []
            if value == 1:
                er_section.children = [cbb_box]
            elif value == 2:
                er_section.children = [bpl_box]
            elif value == 3:
                er_section.children = [emf_box]
            elif value in [4, 5, 6]:
                er_section.children = [er_file_box]
            else:
                er_section.children = []

spectrum.observe(er_visibility, names='value')

er_visibility({'new': spectrum.value})

def on_change(change):
    if change['type'] == 'change' and change['name'] == 'value':
        print(f"Selected label: {spectrum.label}") # Access the label
        print(f"Selected value: {change['new']}") # Access the value
        if len(file) > 1:
            file[1].spectrum = change['new']

spectrum.observe(on_change, names='value')

spectrum_dd = widgets.HBox([label_spectrum, spectrum])

#Structure
er_box = widgets.VBox([widgets.Label("External Radiation", style=dict(font_size="22px")), 
                       spectrum_dd,
                       er_section
])


#####################################################################

#
#Dust Properties
#

dp_box = widgets.VBox([widgets.Label("Dust Properties Content")])

#####################################################################

#
#Density Distribution
#

dd_box = widgets.VBox([widgets.Label("Density Distribution Content")])

#####################################################################

#
#Optical Depth
#

od_box = widgets.VBox([widgets.Label("Optical Depth Content")])

#####################################################################

#
#Accuracy and Output Control Flags
#

accuracy_slider = widgets.FloatSlider(
                value=0.05,
                min=0.01,
                max=0.1,
                step=0.01,
                disabled=False,
                orientation='horizontal',
                readout=True,
)

acc_box = widgets.VBox([
    widgets.Label("Accuracy", style=dict(font_size="16px")),
    widgets.HBox([widgets.Label(value='Numerical Accuracy (0.05 recommended):'), accuracy_slider])
])

verbosity_bit = widgets.BoundedIntText(
    value=1,
    min=0,
    max=3,
    step=1,
    disabled=False
)

fname_spp_bit = widgets.BoundedIntText(
    value=0,
    min=0,
    max=1,
    step=1,
    disabled=False
)

fname_sxxx_bit = widgets.BoundedIntText(
    value=0,
    min=0,
    max=3,
    step=1,
    disabled=False
)

fname_ixxx_bit = widgets.BoundedIntText(
    value=0,
    min=0,
    max=2,
    step=1,
    disabled=False
)

fname_ixxx_wavelengths_slider = widgets.IntSlider(
                value=1,
                min=1,
                max=20,
                step=1,
                disabled=False,
                continuous_update=False,
                orientation='horizontal',
                readout=True,
                readout_format='d'
            )

fname_ixxx_wavelengths_tb = widgets.Text(
                placeholder='Type numbers separated by commas (e.g. 100, 200)',
                layout=widgets.Layout(width='320px')
            )

fname_ixxx_ws_box = widgets.HBox([])
fname_ixxx_wtb_box = widgets.HBox([])

ws_spacer = widgets.Box(layout=widgets.Layout(height='0px'))
wtb_spacer = widgets.Box(layout=widgets.Layout(height='0px'))

def fname_ixxx_visibility(change):
    value = change['new']
    fname_ixxx_ws_box.children = []
    fname_ixxx_wtb_box.children = []
    
    if value != 0:
        fname_ixxx_ws_box.children = [
            widgets.HBox([widgets.Label(value='Number of Wavelengths:'), fname_ixxx_wavelengths_slider])
        ]
        fname_ixxx_wtb_box.children = [
            widgets.HBox([widgets.Label(value='Wavelengths:'), fname_ixxx_wavelengths_tb])
        ]
        ws_spacer.layout.height = '32px' 
        wtb_spacer.layout.height = '32px'
    else:
        fname_ixxx_ws_box.children = []
        fname_ixxx_wtb_box.children = []
        ws_spacer.layout.height = '0px'
        wtb_spacer.layout.height = '0px'

    
fname_ixxx_bit.observe(fname_ixxx_visibility, names='value')

fname_ixxx_visibility({'new': fname_ixxx_bit.value})

fname_vxxx_bit = widgets.BoundedIntText(
    value=0,
    min=0,
    max=3,
    step=1,
    disabled=False
)

fname_rxxx_bit = widgets.BoundedIntText(
    value=0,
    min=0,
    max=2,
    step=1,
    disabled=False
)

fname_mxxx_bit = widgets.BoundedIntText(
    value=0,
    min=0,
    max=2,
    step=1,
    disabled=False
)

file_des_box = widgets.VBox([
    widgets.HBox([widgets.Label(value='Verbosity:')]),
    widgets.HBox([widgets.Label(value='Properties of Emerging Spectra;')]),
    widgets.HBox([widgets.Label(value='Detailed Spectra for Each Model;')]),
    widgets.HBox([widgets.Label(value='Images at Specified Wavelengths;')]),
    fname_ixxx_ws_box,
    fname_ixxx_wtb_box,
    widgets.HBox([widgets.Label(value='Visibility Function at Specific Wavelengths;')]),
    widgets.HBox([widgets.Label(value='Radial Profiles for Each Model;')]),
    widgets.HBox([widgets.Label(value='Detailed Run-time Messages;')]),
],layout=widgets.Layout(width='420px'))  

flag_box = widgets.VBox([
    widgets.HBox([widgets.Label(value='verbose:'), verbosity_bit]),
    widgets.HBox([widgets.Label(value='(fname.spp):'), fname_spp_bit]),
    widgets.HBox([widgets.Label(value='(fname.s###):'), fname_sxxx_bit]),
    widgets.HBox([widgets.Label(value='(fname.i###):'), fname_ixxx_bit]),
    ws_spacer,   
    wtb_spacer,
    widgets.HBox([widgets.Label(value='(fname.v###):'), fname_vxxx_bit]),
    widgets.HBox([widgets.Label(value='(fname.r###):'), fname_rxxx_bit]),
    widgets.HBox([widgets.Label(value='(fname.m###):'), fname_mxxx_bit]),
],layout=widgets.Layout(width='400px', align_items='flex-end'))  

ocf_columns = widgets.HBox([file_des_box, flag_box])

ocf_box = widgets.VBox([
    widgets.Label("Output Control Flags", style=dict(font_size="16px")),
    ocf_columns
])  

aocf_box = widgets.VBox([
    widgets.Label("Accuracy and Output Control Flags", style=dict(font_size="22px")),
    acc_box,
    ocf_box
])

#####################################################################

#
#Parameters Directory
#
                
parameters_directory = widgets.Tab()                

parameters_directory.children = [er_box, dp_box, dd_box, od_box, aocf_box]

titles = ["External Radiation", "Dust Properties", "Density Distribution", "Optical Depth", "Accuracy and Output Control Flags"]
for x, title in enumerate(titles):
    parameters_directory.set_title(x, title)

def ShowWidgets():
    display(parameters_directory)
