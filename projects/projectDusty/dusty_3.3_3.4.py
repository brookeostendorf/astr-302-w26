#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#scratch for building the subclasses of physical paramters

#skeletons of the variables defined 

#the methods are the parent classes that feed into the parameter that then parent the master Dusty class!!


# In[ ]:


class Density_Distribution(broken_PL, exp_decay, exact_RDW, approx_RDW, dd_file):
    def __init__ (self, density_distribution=None, **kwargs):
        super().__init__(**kwargs)
        self.density = density_distribution

class broken_PL:
     def __init__ (self, N_value = None, transition_radii = None, power_indices = None, **kwargs): #defaults the values to None!
        self.N_value = N_value #defines how many pieces you want to break the radius into
        self.transition_radii = []  #the radius at which you want to look at or change the density fall off
        self.power_indices = [] #one power index for each transition value, need to make the amounts here flexible!

        def add_radii(self,transition_radii): #multiple values here depending on how many radii you define, how many shells you want to break into
            for radii in transition_radii:
                self.transition_radii.append(radii)

        def add_power_index(self,power_indices): 
            for power_index in power_indices:
                self.power_indices.append(power_index)

class exponential_decay: #method 2/5
    def __init__ (self, radius = None, sigma = None, **kwargs):
        self.radius = radius #radius of your outer boundary
        self.sigma = sigma  #e^-sigma for the exp decay function

class exact_RDW: #RDW = Radiatively driven winds, find eqns for this maybe?? method 3/5

    def __init__ (self, radius = None, **kwargs):
        self.radius = radius

class approx_RDW: #same parameter as exact RDW, but run thru diff equation method 4/5

    def __init__(self, radius = None, **kwargs):
        self.radius = radius

class dd_file(Density_Distribution): #method 5/5

    def __init__(self, dd_file = None, **kwargs):
        self.file = dd_file #see collapse.dat for what this file should look like!   


# In[ ]:


class Optical_Depth(step_function, file):
    def __init__ (self, optical_depth =None, **kwargs):
        super().__init__(**kwargs)
        self.density = optical_depth



class step_function: #method 1/2
    #include blueprints/examples for linear vs logarithmic, but both methods use the same value types & eqns!

    def __init__(self, tau_grid = None, lamba0 = None, tau_min = None, tau_max = None, model_count = None, **kwargs):
        self.tau_grid = tau grid #=1 or =2
        self.lamba0 = lamba0
        self.tau_min = tau_min
        self.tau_max = tau_max
        self.model_count = model_count

class optical_file: #method 2/2 (technically the third method)

    def __init__(self,optical_file = None, **kwargs):
        self.file = optical_file #taugrid.dat as an example!! 

