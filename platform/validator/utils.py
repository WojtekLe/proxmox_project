# utils.py>

import yaml

def load_yaml(path):
    try:
        with open(path, 'r') as f:
            data = yaml.save_load(f)
            return data
    except FileNotFoundError:        
        print("File {} not found".format(path))