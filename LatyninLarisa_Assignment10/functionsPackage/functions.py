# Name: Nicole Price, Zavier DePillo, Mariangel Betancourt
# email: pricenm@mail.uc.edu, depillzj@mail.uc.edu, betancmg@mail.uc.edu
# Assignment Title: Assignment 10
# Course: IS 4010
# Semester/Year: Spring 2023
# Brief Description: Use of an API to pull data on an asteroid speed
# Citations: https://api.nasa.gov
# Anything else that's relevant: Group project

def iterate_dictionary(myDictionary):
    for k, v in myDictionary.items():
        print ("key is " + str(type(k)) + ", value is " + str(type(v)))
        if isinstance(v, dict):
            iterate_dictionary(v)
        else:
            print("{0} : {1}".format(k, v))
            if (isinstance(v, list)):
                for vv in v:
                    if (isinstance(vv, dict)):
                        iterate_dictionary(vv)