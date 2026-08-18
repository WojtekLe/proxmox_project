# utils.py>

from urllib3 import request
import yaml
import json
import os

def load_yaml(path):
    with open(path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)

def validate_request(request, sizes):

    errors = []
    for vm in request["vms"]:
        size = vm["size"]

        if size not in sizes:
            errors.append(f"Invalid VM size: {size}")

        elif size not in sizes:
            errors.append(
                f"Invalid vm.size '{size}'. "
                f"Allowed values: {', '.join(sizes.keys())}"
        )

    return errors



# def get_vm_size(size_name, sizes):
#     try:
#         return sizes[size_name]
#     except KeyError:
#         raise ValueError(f"Unknown VM size: {size_name}")


def create_tfvars(request, sizes, templates):
    tfvars = {
        "vms": []
    }

    for vm in request["vms"]:
        vm_size = sizes[vm["size"]]
        vm_template = templates[vm["template"]]

        tfvars["vms"].append({
            "project": request["project"],
            "owner": request["owner"],
            "template": vm["template"],
            "cpu": vm_size["cpu"],
            "memory": vm_size["memory"],
            "disk": vm_size["disk"],
            "vm_id": vm_template["vmid"]
        })

    with open("requests/terraform.tfvars.json", "w") as f:
        json.dump(tfvars, f, indent=2)


def check_files_exists(file_path):
    if os.path.exists(file_path):
        print("The file {} exists.".format(file_path))
    else:
        print("The file {} does not exist.".format(file_path))