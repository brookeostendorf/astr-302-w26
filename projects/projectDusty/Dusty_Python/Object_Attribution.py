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
    file.density_distribution = density_distribution.value
    if density_distribution.value == 1:
        file.N_value = N_number.value
        transition_radii_list = transition_radii.value.split(",")
        file.add_radii(transition_radii_list)
        power_indices_list = power_indices.value.split(",")
        file.add_power_index(power_indices_list)

    if density_distribution.value == 2:
        file.radius = outer_boundary.value
        file.sigma = sigma_value.value

    if density_distribution == 3:
        file.radius = sob1_value.value

    if density_distribution == 4:
        file.radius = sob2_value.value

    if density_distribution == 5:
        file.file = dd_file.value


#Optical Depth
    file.optical_depth = optical_depth.value
    if optical_depth.value >= 1 and optical_depth.value <= 2:
        file.tau_grid = tau_grid.value
        file.lamba0 = lambda0_value.value
        file.tau_min = tau_min.value
        file.tau_max = tau_max.value
        file.model_count = model_number.value

    if optical_depth.value == 3:
        file.file = od_file.value

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
    
