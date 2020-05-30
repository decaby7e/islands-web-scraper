import json

##################################################################
# General Configuration
##################################################################

with open("secrets.json") as secrets:
    secrets_json = json.load(secrets)
    USERNAME = secrets_json["username"]
    PASSWORD = secrets_json["password"]

VERBOSE = True

##################################################################
# Villager Constraints
#
# These constants need to be set depending on what your desired
# sample is to be. (e.g. only males between 20 and 49)
##################################################################

VILLAGE = 'Gordes'

HOUSE_LIST = [
    1,2,3,11,19,
    26,27,30,49,51,
    69,70,74,83,91,
    100,101,104,106,112,
    113,118,122,125,148,
    150,152,158,162,177,
    179,192,205,206,219,
    223,225,234,236,240,
    245,246,249,251,253,
    257,268,269,271,275,
]

GENDER = 'male'
