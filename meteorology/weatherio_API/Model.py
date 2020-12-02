import torch
import numpy as np
import pandas as pd






class Prediction_model:

    def __init__(self, path):

        self.dataframe = pd.read_csv(path)
        self.weathersubset = None
        self.weathersubset_more_parameters = self.dataframe[['Light_rain','Broken_clouds']]

        self.stats = None
        

    

    # Behavior methods
    def read_file(self):
        
        return self.dataframe, self.dataframe.columns

    def get_subset(self, parameter):

        """the subset will be return the type of parameter to be studied"""
        self.weathersubset = self.dataframe[parameter]

        return self.weathersubset

    def return_stats(self, parameter):

        try:
            self.stats = self.dataframe[self.weathersubset > parameter]
            return self.stats
        except Exception as e:
            return str(e)

        else:
            return None

    
    def return_stats_string_parameter(self, parameter):

        # method to get the filter, using strings as paramters
        # to be filtered example: time start or time end
        try:
            self.stats = self.dataframe[self.weathersubset == parameter]
            return self.stats
        except Exception as e:
            return str(e)

        else:
            return None





PATH_BEHAVIOR = 'csv/behavior/{}/{}.csv'.format(2017,2017)
PATH_VALUES = 'csv/values/{}/{}.csv'.format(2017,2017)


behavior_model = Prediction_model(PATH_BEHAVIOR)
#values_model = Prediction_model(PATH_VALUES)



print(behavior_model.dataframe)

# SET THE PARAMETER
print(behavior_model.get_subset('Light_rain'))
# print(behavior_model.dataframe.columns)


# WE GONNA TO PRINT USING MORE PARAMETERS AS SUBSET
print(behavior_model.weathersubset_more_parameters)



# NOW IN THE STATS MODEL, PUT 2 AS MAIN PARAMETER TO
# TO FECH THE FILTER BETWEEN LIGHT RAIN AND BROKEN CLOUDS
        
    