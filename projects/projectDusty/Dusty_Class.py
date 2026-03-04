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
    def __init__(self, sil_ow=None, sil_oc=None, sil_dl=None, grf_dl=None, amc_hn=None, sic_pg=None, **kwargs):
        super().__init__(**kwargs)
        self.gt_sil_ow = sil_ow
        self.gt_sil_oc = sil_oc
        self.gt_sil_dl = sil_dl
        self.gt_grf_dl = grf_dl
        self.gt_amc_hn = amc_hn
        self.gt_sic_pg = sic_pg
        self.comp_array = []
        self.file_additional_comp = []
        
    def AddFile(self, ac_files):
        for ac_file in ac_files:
            self.file_additional_comp.append(ac_file)

    def FillCompArray(self):
        self.comp_array.append(self.gt_sil_ow)
        self.comp_array.append(self.gt_sil_oc)
        self.comp_array.append(self.gt_sil_dl)
        self.comp_array.append(self.gt_grf_dl)
        self.comp_array.append(self.gt_amc_hn)
        self.comp_array.append(self.gt_sic_pg)
            
    def standard_mixture(self):
        self.gt_sil_ow = 0.00
        self.gt_sil_oc = 0.00
        self.gt_sil_dl = 0.53
        self.gt_grf_dl = 0.47
        self.gt_amc_hn = 0.00
        self.gt_sic_pg = 0.00

class dust_input_comp:
    def __init__(self, dc_file=None, **kwargs):
        super().__init__(**kwargs)
        self.file_dust_comp = dc_file

class dust_chem_comp(dust_input_comp, dust_base_comp, optical_properties_index):
    pass

class size_distribution:
    def __init__(self, size_dist=None, **kwargs):
        super().__init__(**kwargs)
        self.size_distrubution = size_dist

class mrn_size():
    def __init__(self, expo=None, a_min=None, a_max=None, **kwargs):
        super().__init__(**kwargs)
        self.expo = expo
        self.a_min = a_min
        self.a_max = a_max

    def standard_size(self):
        self.expo.value = 3.5
        self.a_min.value = 0.005
        self.a_max.value = 0.25

class KMH_dist_size:
    def __init__(self, expo=None, a_min=None, a0=None, **kwargs):
        super().__init__(**kwargs)
        self.expo = expo
        self.a_min = a_min
        self.a0 = a0

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


class density_type:
    def __init__(self, density_type=None, **kwargs):
        super().__init__(**kwargs)
        self.denstiy_type = density_type
    
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
  
class Density_Distribution(dd_file, approx_RDW, exact_RDW, exponential_decay, broken_PL, density_type):
    def __init__ (self, **kwargs):
        super().__init__(**kwargs)


#        
# OpticalDepth
#


class grid_type:
    def __init__(self, grid_type=None, **kwargs):
        super().__init__(**kwargs)
        self.grid_type = grid_type
        
class optical_file:
    def __init__(self, optical_file = None, **kwargs):
        super().__init__(**kwargs)
        self.file_opt = optical_file 

class step_function: 
    def __init__(self, tau_grid = None, lamba0 = None, tau_min = None, tau_max = None, model_count = None, **kwargs):
        super().__init__(**kwargs)
        self.tau_grid = tau_grid 
        self.lamba0 = lamba0
        self.tau_min = tau_min
        self.tau_max = tau_max
        self.model_count = model_count 

class Optical_Depth(optical_file, step_function, grid_type):
    def __init__ (self, **kwargs):
        super().__init__(**kwargs)


#
# Dusty
#

        
class Dusty(Optical_Depth, Density_Distribution, dust_properties, External_Radiation):
    def __init__(self,name=None, **kwargs):
        super().__init__(**kwargs)
        self.name = name
