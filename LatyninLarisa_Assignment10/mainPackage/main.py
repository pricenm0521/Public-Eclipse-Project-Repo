# Name: Nicole Price, Zavier DePillo, Mariangel Betancourt
# email: pricenm@mail.uc.edu, depillzj@mail.uc.edu, betancmg@mail.uc.edu
# Assignment Title: Assignment 10
# Course: IS 4010
# Semester/Year: Spring 2023
# Brief Description: Use of an API to pull data on an asteroid speed
# Citations: https://api.nasa.gov
# Anything else that's relevant: Group project

import requests
import json
from functionsPackage.functions import *

response = requests.get('https://api.nasa.gov/neo/rest/v1/neo/3542519?api_key=LF7AWzCRisZrPqDcUPDGBRRafPqwRwIBcNgzPJLO') # makes a request to web server
json_string = response.content # stores the response
    
parsed_json = json.loads(json_string) # dictionary created with the data
    
print(parsed_json)
print(parsed_json['close_approach_data'][0]['relative_velocity']) # getting jut the close approach data we need

print("The speeds taken for asteroid # 3542519 are:") # makine sure our data can be understood
for asteroid in parsed_json['close_approach_data']: 
    print(asteroid["relative_velocity"]) # narrows the data down to the relative velocity