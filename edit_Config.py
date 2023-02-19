'''
Created By: Caleb Malcarne
Program: Invoice Filler 


'''

import json

def getConfigData():
    with open("config.cfg", "r") as config_file:
        config_str = config_file.read()
    config = json.loads(config_str)
    return config

def writeConfigData(config):
    with open("config.cfg", "w") as config_file:
        config_str = json.dumps(config, indent=4)
        config_file.write(config_str)    