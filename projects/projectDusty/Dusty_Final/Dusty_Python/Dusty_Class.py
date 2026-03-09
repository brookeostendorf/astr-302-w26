#!/usr/bin/env python

##                                                                          ##
## FOR ATTRIBUTE INSPECTION, ALL PARENT CLASSES CALLED IN DEFINING CLASSES  ##
##   MUST HAVE REVERSED ORDER TO DUSTY MANUAL                               ##
##   (e.g.) class x(Z,Y,X):                                                 ##
##                                                                          ##


#
# External Radiation
#


class Spectrum:
    def __init__(self, spectrum=None, **kwargs):
        super().__init__(**kwargs)
        self.spectrum = spectrum

class Combination_BB:
    def __init__(self, number_of_bb=None, **kwargs):
        super().__init__(**kwargs)
        self.number_of_bb = number_of_bb
        self.temperatures = []
        self.luminosities = []

    def AddTemps(self, temps):
        for temp in temps:
            self.temperatures.append(temp)

    def AddLuminosity(self, lums):
        for lum in lums:
            self.luminosities.append(lum)    

class Broken_PL:
    def __init__(self, pl_n=None, **kwargs):
        super().__init__(**kwargs)
        self.pl_n = pl_n
        self.pl_lambda = []
        self.pl_k = []

    def AddLambdas(self, _lambdas):
        for _lambda in _lambdas:
            self.pl_lambda.append(_lambda)

    def AddKs(self, _ks):
        for _k in _ks:
            self.pl_k.append(_k)    

class BB_Engelke_Marengo:
    def __init__(self, tbb=None, sio_fd=None, **kwargs):
        super().__init__(**kwargs)
        self.tbb = tbb
        self.sio_fd = sio_fd

class ER_Files:
    def __init__(self, er_file=None, **kwargs):
        super().__init__(**kwargs)
        self.file_er = er_file

class External_Radiation(ER_Files, BB_Engelke_Marengo, Broken_PL, Combination_BB, Spectrum):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


#        
# Dust_Properties
#


class optical_properties_index:
    def __init__(self, index=None, **kwargs):
        super().__init__(**kwargs)
        self.optical_properties_index = index
        
class dust_base_comp:
    def __init__(self, sil_ow=None, sil_oc=None, sil_dl=None, grf_dl=None, amc_hn=None, sic_pg=None, ad_c=None, **kwargs):
        super().__init__(**kwargs)
        self.gt_sil_ow = sil_ow
        self.gt_sil_oc = sil_oc
        self.gt_sil_dl = sil_dl
        self.gt_grf_dl = grf_dl
        self.gt_amc_hn = amc_hn
        self.gt_sic_pg = sic_pg
        self.comp_array = []
        self.additional_comp = ad_c
        self.file_additional_comp = []
        self.add_comp_abundance = []

    def FillCompArray(self, comps):
        for comp in comps:
            self.comp_array.append(comp)
    
    def AddCompFile(self, ac_files):
        for ac_file in ac_files:
            self.file_additional_comp.append(ac_file)
            
    def AddCompAbundance(self, abundances):
        for abd in abundances:
            self.add_comp_abundance.append(abd)


class dust_input_comp:
    def __init__(self, dc_file=None, **kwargs):
        super().__init__(**kwargs)
        self.file_dust_comp = dc_file

class dust_chem_comp(dust_input_comp, dust_base_comp, optical_properties_index):
    pass

class size_distribution:
    def __init__(self, size_dist=None, **kwargs):
        super().__init__(**kwargs)
        self.size_distribution = size_dist

class mrn_size():
    def __init__(self, mrn_expo=None, mrn_a_min=None, mrn_a_max=None, **kwargs):
        super().__init__(**kwargs)
        self.mrn_expo = mrn_expo
        self.mrn_a_min = mrn_a_min
        self.mrn_a_max = mrn_a_max

class KMH_dist_size:
    def __init__(self, kmh_expo=None, kmh_a_min=None, kmh_a0=None, **kwargs):
        super().__init__(**kwargs)
        self.kmh_expo = kmh_expo
        self.kmh_a_min = kmh_a_min
        self.kmh_a0 = kmh_a0

class dust_grain_size(KMH_dist_size, mrn_size, size_distribution):
    pass

class dust_temp:
    def __init__(self,temp_inner=None, **kwargs):
        super().__init__(**kwargs)
        self.temp_inner = temp_inner

class dust_properties(dust_temp, dust_grain_size, dust_chem_comp):
    pass


#
# Density Distribution
#


class density:
    def __init__(self, density_type=None, **kwargs):
        super().__init__(**kwargs)
        self.density_type = density_type
    
class dd_file: 
    def __init__(self, dd_file = None, **kwargs):
        super().__init__(**kwargs)
        self.file_dd = dd_file

class approx_RDW: 
    def __init__(self, radius = None, **kwargs):
        super().__init__(**kwargs)
        self.radius = radius

class exact_RDW: 
    def __init__ (self, radius = None, **kwargs):
        super().__init__(**kwargs)
        self.radius = radius

class exponential_decay:
    def __init__ (self, radius = None, sigma = None, **kwargs):
        super().__init__(**kwargs)
        self.radius = radius 
        self.sigma = sigma
        
class broken_PL:
    def __init__ (self, N_value = None, transition_radii = None, power_indices = None, **kwargs): 
        super().__init__(**kwargs)
        self.N_value = N_value 
        self.transition_radii = [] 
        self.power_indices = [] 
        
    def add_radii(self,transition_radii): 
        for radii in transition_radii:
            self.transition_radii.append(radii)

    def add_power_index(self,power_indices): 
        for power_index in power_indices:
            self.power_indices.append(power_index)
  
class Density_Distribution(dd_file, approx_RDW, exact_RDW, exponential_decay, broken_PL, density):
    def __init__ (self, **kwargs):
        super().__init__(**kwargs)


#        
# OpticalDepth
#

#I removed the grid type class, as the tau_grid IS the grid type
class optical_file:
    def __init__(self, optical_file = None, **kwargs):
        super().__init__(**kwargs)
        self.file_opt = optical_file 

class step_function: 
    def __init__(self, tau_grid = None, lambda0 = None, tau_min = None, tau_max = None, model_count = None, **kwargs):
        super().__init__(**kwargs)
        self.tau_grid = tau_grid 
        self.lambda0 = lambda0
        self.tau_min = tau_min
        self.tau_max = tau_max
        self.model_count = model_count 

class Optical_Depth(optical_file, step_function):
    def __init__ (self, **kwargs):
        super().__init__(**kwargs)


#
#Accuracy and Output Control Flags
#


class Accuracy():
    def __init__(self, qacc = None, **kwargs):
        super().__init__(**kwargs)
        self.qacc = qacc

class Output_Ctrl_Flags():
    def __init__(self, verb=0, spp=0, sxxx=0, ixxx=0, wavelengths=None, vxxx=0, rxxx=0, mxxx=0, **kwargs):
        super().__init__(**kwargs)
        self.verbosity = verb #0-3
        self.fname_spp = spp #0-1
        self.fname_sxxx = sxxx #0-3
        self.fname_ixxx = ixxx #0-2
        self.fname_ixxx_wavelengths = wavelengths #1-20
        self.fname_ixxx_wavelengths_array = [] 
        self.fname_vxxx = vxxx #0-3
        self.fname_rxxx = rxxx #0-2
        self.fname_mxxx = mxxx #0-2

    def AddWavelengths(self, wavelengths):
        for wavelength in wavelengths:
            self.fname_ixxx_wavelengths_array.append(wavelength)


class Acc_and_Output_Ctrl(Output_Ctrl_Flags, Accuracy):
    def __init__ (self, **kwargs):
        super().__init__(**kwargs)


#
# Dusty
#

        
class Dusty(Acc_and_Output_Ctrl, Optical_Depth, Density_Distribution, dust_properties, External_Radiation):
    def __init__(self,name=None, **kwargs):
        super().__init__(**kwargs)
        self.name = name
