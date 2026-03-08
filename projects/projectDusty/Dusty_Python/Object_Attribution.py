#!/usr/bin/env python

import ipywidgets as widgets
from ipywidgets import interact, interact_manual
from IPython.display import display

# A file that writes widget values to attributes of a created dusty object#

def attribution ():
    file = Dusty_Class.Dusty()
    file.name = input_name.value
#Black Body    
    file.spectrum = spectrum.value
    if spectrum.value == 1:
        file.number_of_bb = bb_number.value
        temps_list = temps.value.split(", ")
        file.AddTemps(temps_list)
        lums_list = lums.value.split(", ")
        file.AddLuminosity(lums_list)
        
    if spectrum.value == 2:
        file.pl_n = N_functions.value
        lambdas_list = _lambdas.value.split(", ")
        file.AddLambdas(lambdas_list)
        p_indicies_list = power_indicies.value.split(", ")
        file.AddKs(p_indicies_list)
    
    if spectrum.value == 3:
        file.tbb = tbb_temp.value
        file.sio_fd = sio_fd.value
    
    if spectrum.value >3 and spectrum.value <=6:
        file.file = er_files.value
#Dust Properties
    
#Density Distribution

#Optical Depth

#Accuracy and Output Control
    file.qaa = accuracy_slider.value
    file.verbosity = verbosity_bit.value
    file.fname_spp = fname_spp_bit.value
    file.fname_sxxx = fname_sxxx_bit.value
    file.fname_ixxx = fname_ixxx_bit.value
    if file.fname_ixxx != 0:
        file.fname_ixxx_wavelengths = fname_ixxx_wavelengths_slider.value
        wavelengths_array = fname_ixxx_wavelengths_tb.value.split(", ")
        file.AddWavelengths (wavelengths_array)
       
    file.fname_vxxx = fname_vxxx_bit.value
    file.fname_rxxx = fname_rxxx_bit.value
    file.fname_mxxx = fname_mxxx_bit.value
    
