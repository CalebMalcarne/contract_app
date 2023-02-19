'''
Created By: Caleb Malcarne
Program: Invoice Filler 


'''

from edit_Config import *
import os

def checkPaths():
    if not os.path.exists("config.cfg"):
        with open("config.cfg", "w") as f:
            settings = {
                    "template_path": "docs/Contract.docx",
                    "window_size": "Large",
                    "image_size_thresh": "500",
                    "deposit_percent": "30"
                    }
            config_str = json.dumps(settings, indent=4)
            f.write(config_str) 
        f.close()

    if not os.path.exists("temp"):
        os.mkdir("temp")


contract_info = {
            "date"        : "2/2/2022",
            "client"      : "Jane Doe",
            "estimate_num" : "A1234",
            "start_date"  : "2/2/2022",
            "end_date"    : "2/3/2022",
            "estiamte_amount": 20000,
            "time_important" : False,
            "hourly_rate": 125,
            "deposit": '',
        }

checkPaths()
config = getConfigData()

#-----------------#
allowances = {}
#-----------------#
imageLis = []
#-----------------#
image_threshold = int(config["image_size_thresh"])

depost_percent = int(config["deposit_percent"])

widnow_size = config["window_size"]
#-----------------#

