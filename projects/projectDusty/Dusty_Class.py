#!/usr/bin/env python

##                                                                          ##
## FOR ATTRIBUTE INSPECTION, ALL PARENT CLASSES CALLED IN DEFINING CLASSES  ##
##   MUST HAVE REVERSED ORDER TO DUSTY MANUAL                               ##
##   (e.g.) class x(Z,Y,X):                                                 ##
##                                                                          ##

# External Radiation

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

class Files:
    def __init__(self, file=None, **kwargs):
        super().__init__(**kwargs)
        self.file = file

class External_Radiation(Files, BB_Engelke_Marengo, Broken_PL, Combination_BB, Spectrum):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

# Dust_Properties

class dust_base_comp():
    def __init__(self, sil_ow=None, sil_oc=None, sil_dl=None, grf_dl=None, amc_hn=None, sic_pg=None, textfile=None, **kwargs):
        super().__init__(**kwargs)
        self.sil_ow = sil_ow
        self.sil_oc = sil_oc
        self.sil_dl = sil_dl
        self.grf_dl = grf_dl
        self.amc_hn = amc_hn
        self.sic_pg = sic_pg
        self.textfile = np.array(textfile) if textfile is not None else None

    def standard_mixture(self):
        self.sil_ow.value = 0.00
        self.sil_oc.value = 0.00
        self.sil_dl.value = 0.53
        self.grf_dl.value = 0.47
        self.amc_hn.value = 0.00
        self.sic_pg.value = 0.00

class dust_input_comp():
    def __init__(self, file=None, **kwargs):
        super().__init__(**kwargs)
        self.file = np.array(file)

class dust_chem_comp(dust_base_comp, dust_input_comp):
    pass

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

class KMH_dist_size():
    def __init__(self, expo=None, a_min=None, a0=None, **kwargs):
        super().__init__(**kwargs)
        self.expo = expo
        self.a_min = a_min
        self.a0 = a0

class dust_grain_size(mrn_size, KMH_dist_size):
    pass

class dust_temp():
    def __init__(self,temp_inner=None, **kwargs):
        super().__init__(**kwargs)
        self.temp_inner = temp_inner

class dust_properties(dust_base_comp, dust_grain_size, dust_temp):
    pass

# Density Distribution

# OpticalDepth


# Dusty
class Dusty(External_Radiation, dust_properties):
    def __init__(self,name=None, **kwargs):
        super().__init__(**kwargs)
        self.name = name

    