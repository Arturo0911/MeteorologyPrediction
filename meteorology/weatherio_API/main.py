import torch
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from urllib.request import urlopen
from urllib.error import HTTPError
from pprint import pprint
import requests


class Meteorology:
    
    def __init__(self) -> None:
        pass

    def initializer(self):
        pass



api_key = 'ba199bd058f45b1a54e0d25ba95d1ca9'
weatherbi_key = 'c96c2aa02b1b43e184580f8efe648f59' # fetch api data from historic, using latitude and longitude
#latitude = '-2.335017'
latitude = '-2.3352106'
#longitude = '-80.229769'
longitude = '-80.2300508'
weatherstack_key = 'e57f178396859a0e95647a48f82b4504'
url = 'https://api.weatherbit.io/v2.0/history/hourly?lat=-2.335017&lon=-80.229769&start_date=2020-11-18&end_date=2020-11-19&tz=local&key=c96c2aa02b1b43e184580f8efe648f59'

# time to start and end
# examples we use 2016 in October
time_start = '2016-10-21'
time_end = '2016-10-22'



url_parameters = 'https://api.weatherbit.io/v2.0/history/hourly?lat={}&lon={}&start_date={}&end_date={}&tz=local&key={}'.format(latitude,longitude,time_start,time_end,weatherbi_key)
response = requests.get(url_parameters).json()
pprint(response)
#pprint(response['data'])
