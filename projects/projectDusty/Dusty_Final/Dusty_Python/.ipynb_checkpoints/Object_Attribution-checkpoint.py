#!/usr/bin/env python

import ipywidgets as widgets
from ipywidgets import interact, interact_manual
from IPython.display import display
import inspect
import os

from Dusty_Python import Dusty_Class
from Dusty_Python import Dusty_Widgets
from Dusty_Python import ExecuteButton

# A file that writes widget values to attributes of a created dusty object#

def clean_val(input_data):
    val = input_data.value if hasattr(input_data, 'value') else input_data
    try:    
        return round(float(val), 2)
    except (ValueError, TypeError):
        return val

def attribution ():
    ExecuteButton.file.temperatures = []
    ExecuteButton.file.luminosities = []
    ExecuteButton.file.pl_lambda = []
    ExecuteButton.file.pl_k = []
    ExecuteButton.file.comp_array = []
    ExecuteButton.file.file_additional_comp = []
    ExecuteButton.file.transition_radii = []
    ExecuteButton.file.power_indices = []
    ExecuteButton.file.fname_ixxx_wavelengths_array = []
    
    spec_val = Dusty_Widgets.spectrum.value
    sd_val = Dusty_Widgets.size_distribution.value
#    op_val = Dusty_Widgets.optical_properties.value  op_val,
    dd_val = Dusty_Widgets.density_distribution.value
    od_val = Dusty_Widgets.optical_depth.value
    selections = [spec_val, sd_val, dd_val, od_val]
    
    if '' in selections:
        print("Error: One or more dropdowns are unselected. Please verify all categories.")
        return
    
    ExecuteButton.file.name = Dusty_Widgets.input_name.value
#Black Body    
    ExecuteButton.file.spectrum = Dusty_Widgets.spectrum.value
    if Dusty_Widgets.spectrum.value == 1:
        ExecuteButton.file.number_of_bb = Dusty_Widgets.bb_slider.value
        temps_list = [w.strip() for w in Dusty_Widgets.temps_tb.value.split(",") if w.strip()]
        ExecuteButton.file.AddTemps(temps_list)
        lums_list = [w.strip() for w in Dusty_Widgets.lums.value.split(",") if w.strip()]
        ExecuteButton.file.AddLuminosity(lums_list)
        
    if Dusty_Widgets.spectrum.value == 2:
        ExecuteButton.file.pl_n = Dusty_Widgets.N_functions_itb.value
        lambdas_list = [w.strip() for w in Dusty_Widgets.lambdas_tb.value.split(",") if w.strip()]
        ExecuteButton.file.AddLambdas(lambdas_list)
        p_indicies_list = [w.strip() for w in Dusty_Widgets.power_indicies_tb.value.split(",") if w.strip()]
        ExecuteButton.file.AddKs(p_indicies_list)
    
    if Dusty_Widgets.spectrum.value == 3:
        ExecuteButton.file.tbb = Dusty_Widgets.tbb_temp_tb.value
        ExecuteButton.file.sio_fd = clean_val(Dusty_Widgets.sio_fd_slider.value)
    
    if Dusty_Widgets.spectrum.value >3 and Dusty_Widgets.spectrum.value <=6:
        ExecuteButton.file.file_er = Dusty_Widgets.er_files_tb.value
#Dust Properties
    
#Density Distribution
    ExecuteButton.file.density_type = Dusty_Widgets.density_distribution.value
    if Dusty_Widgets.density_distribution.value == 1:
        ExecuteButton.file.N_value = Dusty_Widgets.N_number.value
        transition_radii_list = [w.strip() for w in Dusty_Widgets.transition_radii.value.split(",") if w.strip()]
        ExecuteButton.file.add_radii(transition_radii_list)
        power_indices_list = [w.strip() for w in Dusty_Widgets.power_indices.value.split(",") if w.strip()]
        ExecuteButton.file.add_power_index(power_indices_list)

    if Dusty_Widgets.density_distribution.value == 2:
        ExecuteButton.file.radius = Dusty_Widgets.outer_boundary.value
        ExecuteButton.file.sigma = clean_val(Dusty_Widgets.sigma_value.value)

    if Dusty_Widgets.density_distribution.value == 3:
        ExecuteButton.file.radius = Dusty_Widgets.sob1_value.value

    if Dusty_Widgets.density_distribution.value == 4:
        ExecuteButton.file.radius = Dusty_Widgets.sob2_value.value

    if Dusty_Widgets.density_distribution.value == 5:
        ExecuteButton.file.file_dd = Dusty_Widgets.dd_file.value


#Optical Depth
    ExecuteButton.file.optical_depth = Dusty_Widgets.optical_depth.value
    if Dusty_Widgets.optical_depth.value >= 1 and Dusty_Widgets.optical_depth.value <= 2:
        ExecuteButton.file.lambda0 = Dusty_Widgets.lambda0_value.value
        ExecuteButton.file.tau_min = Dusty_Widgets.tau_min.value
        ExecuteButton.file.tau_max = Dusty_Widgets.tau_max.value
        ExecuteButton.file.model_count = Dusty_Widgets.model_number.value

    if Dusty_Widgets.optical_depth.value == 3:
        ExecuteButton.file.file_opt = Dusty_Widgets.od_file.value

#Accuracy and Output Control
    ExecuteButton.file.qaa = clean_val(Dusty_Widgets.accuracy_slider.value)
    ExecuteButton.file.verbosity = Dusty_Widgets.verbosity_bit.value
    ExecuteButton.file.fname_spp = Dusty_Widgets.fname_spp_bit.value
    ExecuteButton.file.fname_sxxx = Dusty_Widgets.fname_sxxx_bit.value
    ExecuteButton.file.fname_ixxx = Dusty_Widgets.fname_ixxx_bit.value
    if Dusty_Widgets.fname_ixxx_bit.value != 0:
        ExecuteButton.file.fname_ixxx_wavelengths = Dusty_Widgets.fname_ixxx_wavelengths_slider.value
        wavelengths_array = [w.strip() for w in Dusty_Widgets.fname_ixxx_wavelengths_tb.value.split(",") if w.strip()]
        ExecuteButton.file.AddWavelengths (wavelengths_array)
       
    ExecuteButton.file.fname_vxxx = Dusty_Widgets.fname_vxxx_bit.value
    ExecuteButton.file.fname_rxxx = Dusty_Widgets.fname_rxxx_bit.value
    ExecuteButton.file.fname_mxxx = Dusty_Widgets.fname_mxxx_bit.value
    
