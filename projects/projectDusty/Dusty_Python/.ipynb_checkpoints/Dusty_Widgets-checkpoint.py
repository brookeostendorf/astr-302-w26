#!/usr/bin/env python

import ipywidgets as widgets
from ipywidgets import interact, interact_manual
from IPython.display import display

# A file that conatins the code for all the ipywidgets in the input notebook #

#Notebook Header
title = widgets.Label(value='Dusty Input',style=dict(font_size="30px"),layout=widgets.Layout(height='35px') )

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

er_box = widgets.VBox([widgets.Label("External Radiation", style=dict(font_size="25px")), 
                       spectrum_dd,
                       er_section
])


#####################################################################

#
#Dust Properties
#

#Chemical Composition Types

#Standard ISM
w_sil_ow = widgets.BoundedFloatText(
    value=0.0,
    min=0,
    max=1.0,
    step=0.001,
    disabled=False,
    layout=widgets.Layout(width='50px', margin='0 5px 0 5px')
)

w_sil_oc = widgets.BoundedFloatText(
    value=0.0,
    min=0,
    max=1.0,
    step=0.001,
    disabled=False,
    layout=widgets.Layout(width='50px', margin='0 5px 0 5px')
)

w_sil_dl = widgets.BoundedFloatText(
    value=0.53,
    min=0,
    max=1.0,
    step=0.001,
    disabled=False,
    layout=widgets.Layout(width='50px', margin='0 5px 0 5px')
)

w_grf_dl = widgets.BoundedFloatText(
    value=0.47,
    min=0,
    max=1.0,
    step=0.001,
    disabled=False,
    layout=widgets.Layout(width='50px', margin='0 5px 0 5px')
)

w_amc_hn = widgets.BoundedFloatText(
    value=0.0,
    min=0,
    max=1.0,
    step=0.001,
    disabled=False,
    layout=widgets.Layout(width='50px', margin='0 5px 0 5px')
)

w_sic_pg = widgets.BoundedFloatText(
    value=0.0,
    min=0,
    max=1.0,
    step=0.001,
    disabled=False,
    layout=widgets.Layout(width='50px', margin='0 5px 0 5px')
)

abundances_top_row = widgets.HBox([
    widgets.Label("Sil-Ow", layout=widgets.Layout(width='50px', justify_content='center', margin='0 5px 0 5px')),
    widgets.Label("Sil-Oc", layout=widgets.Layout(width='50px', justify_content='center', margin='0 5px 0 5px')),
    widgets.Label("Sil-DL", layout=widgets.Layout(width='50px', justify_content='center', margin='0 5px 0 5px')),
    widgets.Label("grf-DL", layout=widgets.Layout(width='50px', justify_contents='center', margin='0 5px 0 5px')),
    widgets.Label("amC-Hn", layout=widgets.Layout(width='50px', justify_content='center', margin='0 5px 0 5px')),
    widgets.Label("SiC-Pg", layout=widgets.Layout(width='50px', justify_content='center', margin='0 5px 0 5px')),
])

abundances_bottom_row = widgets.HBox([
    w_sil_ow, w_sil_oc, w_sil_dl, w_grf_dl, w_amc_hn, w_sic_pg
])

abundances_box = widgets.VBox([widgets.Label("Abundances for supported grain types:", style=dict(font_size="16px")), abundances_top_row, abundances_bottom_row])

#Modified Files
mcc_files_number_bit = widgets.BoundedIntText(
            value=1,
            min=0,
            max=10,
            step=1,
            disabled=False
)

mcc_file_tb = widgets.Textarea(
    placeholder='Type names separated by commas (e.g. amC-zb1.nk, amC-zb2.nk)',
    layout=widgets.Layout(width='320px')
)

mcc_file_abundances_tb = widgets.Text(
    placeholder='Type numbers separated by commas (e.g. 0.45, 0.23)',
    layout=widgets.Layout(width='320px')
)

mcc_files_box = widgets.VBox([
widgets.Label("Additional Grain Type Files", style=dict(font_size="16px")),
widgets.HBox([widgets.Label(value='Number of Additonal Components:'), mcc_files_number_bit]),
widgets.HBox([widgets.Label(value='File Names:'), mcc_file_tb]),
widgets.HBox([widgets.Label(value='Abundances of Additional Components:'), mcc_file_abundances_tb])
])

#Full Properties File
cc_files_tb = widgets.Text(
    layout=widgets.Layout(width='320px')
)

cc_file_box = widgets.VBox([
widgets.Label("File", style=dict(font_size="16px")),
widgets.HBox([widgets.Label(value='File Name:'), cc_files_tb])
])

#Grain Size Distribution

#Modified MRN
mrn_power_index = widgets.BoundedFloatText(
    value=3.5,
    min=-5.0,
    max=10.0,
    step=0.1,
    disabled=False
)

mrn_lower_lim = widgets.BoundedFloatText(
    value=0.005,
    min=0.001,
    max=10.0,
    step=0.001,
    disabled=False
)

upper_lim = widgets.BoundedFloatText(
    value=0.25,
    min=0.01,
    max=1000.0,
    step=0.01,
    disabled=False
)

mrn_box = widgets.VBox([
widgets.Label("Modified MRN Distribution", style=dict(font_size="16px")),
widgets.HBox([widgets.Label(value='Power Index (q):'), mrn_power_index]),
widgets.HBox([widgets.Label(value='Lower Limit (a(min))'), mrn_lower_lim]),
widgets.HBox([widgets.Label(value='Upper Limit (a(max)):'), upper_lim])
])

#KMH
kmh_power_index = widgets.BoundedFloatText(
    value=3.5,
    min=-5.0,
    max=10.0,
    step=0.1,
    disabled=False
)

kmh_lower_lim = widgets.BoundedFloatText(
    value=0.005,
    min=0.001,
    max=10.0,
    step=0.001,
    disabled=False
)

char_size = widgets.BoundedFloatText(
    value=0.2,
    min=0.01,
    max=1000.0,
    step=0.01,
    disabled=False
)

kmh_box = widgets.VBox([
widgets.Label("KMH Distribution", style=dict(font_size="16px")),
widgets.HBox([widgets.Label(value='Power Index (q):'), kmh_power_index]),
widgets.HBox([widgets.Label(value='Lower Limit (a(min))'), kmh_lower_lim]),
widgets.HBox([widgets.Label(value='Characteristic Size (a0):'), char_size])
])

#Size Distribution
size_distribution_values = [
    ('--Select Optical Property Type--', ''),
    ('Standard MRN Distribution', 1),
    ('Modified MRN Distribution', 2),
    ('KMH Distribution', 3),
]

label_size_distribution = widgets.Label(value='Size Distribution:')
size_distribution = widgets.Dropdown(
    options=size_distribution_values,
    value='',
    continuous_update=True,
    disabled=False)

gsd_section = widgets.VBox([])

def gsd_visibility(change):
            value = change['new']
            gsd_section.children = []
            if value == 1:
                gsd_section.children = []
            elif value == 2:
                gsd_section.children = [mrn_box]
            elif value == 3:
                gsd_section.children = [kmh_box]
            else:
                gsd_section.children = []

size_distribution.observe(gsd_visibility, names='value')

gsd_visibility({'new': size_distribution.value})

def on_change(change):
    if change['type'] == 'change' and change['name'] == 'value':
        print(f"Selected label: {size_distribution.label}") # Access the label
        print(f"Selected value: {change['new']}") # Access the value
        if len(file) > 1:
            file[1].size_distribution = change['new']

size_distribution.observe(on_change, names='value')

size_distribution_dd = widgets.HBox([label_size_distribution, size_distribution])

sd_box = widgets.VBox([widgets.Label("Grain Size Distribution", style=dict(font_size="20px")), 
                       size_distribution_dd,
                       gsd_section
])

#Dust Temps on Inner Boundary

inner_temp = widgets.BoundedFloatText(
    value=1000,
    min=0.01,
    max=3000,
    step=0.01,
    disabled=False
)

inner_temp_box = widgets.HBox([widgets.Label(value='Boundary Temp:'), inner_temp])

dtib_box = widgets.VBox([widgets.Label("Dust Temperature on Inner Boundary", style=dict(font_size="20px")), 
                       inner_temp_box
])


#Optical Properties Index

optical_properties_values = [
    ('--Select Optical Property Type--', ''),
    ('Standard ISM Mixture Abundances', 1),
    ('Modified ISM Mixture Abundances', 2),
    ('File: Includes Absorbption and Cross Sections', 3),
]

label_optical_properties = widgets.Label(value='Optical Property:')
optical_properties = widgets.Dropdown(
    options=optical_properties_values,
    value='',
    continuous_update=True,
    disabled=False)

cc_section = widgets.VBox([])

def cc_visibility(change):
            value = change['new']
            cc_section.children = []
            if value == 1:
                cc_section.children = [abundances_box,sd_box]
            elif value == 2:
                cc_section.children = [abundances_box, mcc_files_box, sd_box]
            elif value == 3:
                cc_section.children = [cc_file_box]
            else:
                cc_section.children = []

optical_properties.observe(cc_visibility, names='value')

cc_visibility({'new': optical_properties.value})

def on_change(change):
    if change['type'] == 'change' and change['name'] == 'value':
        print(f"Selected label: {optical_properties.label}") # Access the label
        print(f"Selected value: {change['new']}") # Access the value
        if len(file) > 1:
            file[1].optical_properties = change['new']

optical_properties.observe(on_change, names='value')

optical_properties_dd = widgets.HBox([label_optical_properties, optical_properties])

cc_box = widgets.VBox([widgets.Label("Chemical Composition", style=dict(font_size="20px")), 
                       optical_properties_dd,
                       cc_section
])

#Structure

dp_box = widgets.VBox([widgets.Label("Dust Properties", style=dict(font_size="25px")), 
                       cc_box,
                       dtib_box
])

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

#Accuracy
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

#Output Control Flags
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

#Structure

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
    widgets.Label("Accuracy and Output Control Flags", style=dict(font_size="25px")),
    acc_box,
    ocf_box
])

#####################################################################

#
#Parameters Directory
#
                
parameters_directory = widgets.Tab()                

parameters_directory.children = [er_box, dp_box, dd_box, od_box, aocf_box]

pm_titles = ["External Radiation", "Dust Properties", "Density Distribution", "Optical Depth", "Accuracy and Output Control Flags"]
for x, pm_title in enumerate(pm_titles):
    parameters_directory.set_title(x, pm_title)

#####################################################################

#
#Display Function
#

def ShowWidgets():
    display(title)
    display(name_tb)
    display(parameters_directory)
