""" IN THIS FILE, WE GONNA TEST THE DATA, USING COMPARATIONS BETWEEN DATAS, AND PARAMETERS
    
"""

import numpy as np
import pandas as pd
import torch
from pprint import pprint

""" Libraries of the data storage """

# this one return the list o behavior to be instantiated.
from Interface_objects import make_list 



class Init_test:     

    def __init__(self,cloud_parameter, year_consult):
        # initialize the parameters to be the query
        
        self.path = '.csv/.clouds_parameters/.'+ cloud_parameter+'/.'+str(year_consult)+'/.'+str(year_consult)+'.csv'
        self._path = '.csv/.clouds_parameters/.{}/.{}/.{}.csv'
        self.dataframe_weather = pd.read_csv(self.path)
        

    def read_dataframe(self):
        # Return the dataframe with all the values in the data
        
        return self.dataframe_weather

    def make_subset(self, object_parameters):
        # get the parameters with the object parameters
        # set cloud parameters in differents years
        # create variables to avoid big names into the methods
        # the variable first_param_year will be used two times, because the directory and the file has the same name
        """

        Structure of the parameters to be evaluated
        object_parameters = {

            'value': {'cloud_parameter': Behavior cloud: Broken_clouds, Light_rain, Clear_Sky, 'year_activity': None, 'filter': 'the filter is the header 
                    of each column to be evaluated'}
        }
        """
        
        first_param_cloud = object_parameters['values']['cloud_parameter']
        first_param_year = object_parameters['values']['year_activity']
        first_param_filter = object_parameters['values']['filter']

        first_data_frame_subset = pd.read_csv(self._path.format(first_param_cloud,first_param_year
        ,first_param_year))


        # taking the first_data_parameter, put the parameter to be filtered

        subset_first = self.read_dataframe()[first_param_filter]


        #return first_data_frame_subset , second_data_frame_subset

        # this one gonna return the subset with the filter
        return subset_first


    def set_parameters(self, object_parameters, range):

        subset = self.make_subset(object_parameters)

        data_range = self.dataframe_weather[subset >= 20]


        return data_range

object_parameters = {

    'values': {
        'cloud_parameter': 'Broken_clouds', 
        'year_activity': 2017, 
        'filter': 'temperature'
        }
    }
test_init = Init_test('Broken_clouds', 2017)
pprint(object_parameters)

firstparam = test_init.make_subset(object_parameters)

print(firstparam)
print(test_init.set_parameters(object_parameters, 20))
#print(test_init.read_dataframe())
# first_parameter, second_parameter = test_init.make_subset('Broken_cloud', 'Ligth_rain')



#print(first_parameter)








