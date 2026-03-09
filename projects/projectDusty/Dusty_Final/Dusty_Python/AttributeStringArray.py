#!/usr/bin/env python

#Function that reads the atrributes of an object, converts the values of defined attributes into properly formatted text strings, and puts the strings in an array#

def inspect_attributes(obj):
    dusty_order = [
    # 1. External_Radiation (Rightmost Parent)
    'spectrum',                       # From Spectrum
    'number_of_bb', 'temperatures', 'luminosities', # From Combination_BB
    'pl_n', 'pl_lambda', 'pl_k',      # From Broken_PL
    'tbb', 'sio_fd',                  # From BB_Engelke_Marengo
    'file_er',                        # From ER_Files

    # 2. dust_properties
    'optical_properties_index',       # From optical_properties_index
    'gt_sil_ow', 'gt_sil_oc', 'gt_sil_dl', 'gt_grf_dl', 
    'gt_amc_hn', 'gt_sic_pg', 'comp_array', 
    'additional_comp', 'file_additional_comp', # From dust_base_comp
    'file_dust_comp',                 # From dust_input_comp
    'size_distribution',              # From size_distribution (Note typo in your class: distrubution)
    'expo', 'a_min', 'a_max',         # From mrn_size
    'a0',                             # From KMH_dist_size (expo/a_min overlap)
    'temp_inner',                     # From dust_temp

    # 3. Density_Distribution
    'density_type',                   # From density
    'N_value', 'transition_radii', 'power_indices', # From broken_PL
    'radius', 'sigma',                # From exponential_decay / exact_RDW / approx_RDW
    'file_dd',                        # From dd_file

    # 4. Optical_Depth
    'tau_grid', 'lambda0', 'tau_min', 'tau_max', 'model_count', # From step_function
    'file_opt',                       # From optical_file

    # 5. Acc_and_Output_Ctrl
    'qacc',                           # From Accuracy
    'verbosity', 'fname_spp', 'fname_sxxx', 'fname_ixxx', 
    'fname_ixxx_wavelengths', 'fname_ixxx_wavelengths_array', 
    'fname_vxxx', 'fname_rxxx', 'fname_mxxx', # From Output_Ctrl_Flags

    # 6. Dusty (The final class)
    'name'                            # Defined in Dusty.__init__
]

    
    content = []

    for attr in dusty_order:
        if hasattr(obj, attr):
            value = getattr(obj, attr)
            
            # Skip if the attribute is None (not used in this run)
            if value is None:
                continue

            if attr.startswith("file"):
                if isinstance(value, list):
                    for item in value:
                        content.append(f"{item}")
                else: 
                    content.append(f"{value}")
                continue
                
            # Handle List formatting (like for temperatures/wavelengths)
            if isinstance(value, list):
                if len(value) > 0:
                    list_str = ", ".join(str(item) for item in value)
                    content.append(f"{attr}= {list_str}")
            else:
                content.append(f"{attr}= {value}")
                
    return content