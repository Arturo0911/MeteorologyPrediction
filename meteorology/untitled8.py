# -*- coding: utf-8 -*-
"""Untitled8.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1vQWM4jsxp4hv46hvzOfiVPt2ItG2-yVA
"""

from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

url = 'http://en.wikipedia.org/wiki/Kevin_Bacon'
html = urlopen(url)

bs_obj = BeautifulSoup(html)

for link in bs_obj.findAll('a'):
  
  if ('href' in link.attrs):
    print(link.attrs['href'])

for link in bs_obj.find('div', {'id': 'bodyContent'}).findAll('a', href=re.compile('^(/wiki/)((?!:).)*$')):

  if 'href' in link.attrs:
    print(link['href'])

try:
  new_url = 'http://www.uagraria.edu.ec/'
  weather_url = 'https://es.weatherspark.com/h/y/146933/2010/Tiempo-hist%C3%B3rico-durante-2010en-Aeropuerto-Internacional-Jos%C3%A9-Joaqu%C3%ADn-de-Olmedo-Ecuador'
  second_url = 'https://aulavirtual.uagraria.edu.ec/'
  bs_obj = BeautifulSoup(urlopen(weather_url))
  
  #print(bs_obj.find_all('a'))

  for x in bs_obj.find_all('a'):
    #print(x['href'])
    print(x)

except Exception as e:
  print(e)