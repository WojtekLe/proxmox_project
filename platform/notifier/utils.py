# utils.py>

import json

def check_json(file_path):    
    print("Checking json file...")
    with open(file_path) as f:
        data = json.load(f)
        ip = data["vm_ip"]["value"][0]
    print("Ip addess:{}".format(ip))