# utils.py>

import yaml
import json
import os

def load_yaml(path):
    with open(path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)

def validate_request(request, sizes):

    errors = []

    size = request.get("vm", {}).get("size")

    if not size:
        errors.append("Missing vm.size")

    elif size not in sizes:
        errors.append(
            f"Invalid vm.size '{size}'. "
            f"Allowed values: {', '.join(sizes.keys())}"
        )

    return errors


def get_vm_size(size_name, sizes):
    try:
        return sizes[size_name]
    except KeyError:
        raise ValueError(f"Unknown VM size: {size_name}")


def create_tfvars(request, sizes, templates):

    vm_size_name = request["vm"]["size"]

    vm_size = sizes[vm_size_name]

    vm_id = templates[request["vm"]["template"]]

    tfvars = {
        "project": request["project"],
        "owner": request["owner"],
        "template": request["vm"]["template"],
        "cpu": vm_size["cpu"],
        "memory": vm_size["memory"],
        "disk": vm_size["disk"],
        "vm_id": vm_id["vmid"]
    }

    with open("requests/terraform.tfvars.json", "w") as f:
        json.dump(tfvars, f, indent=2)


def check_files_exists(file_path):
    if os.path.exists(file_path):
        print("The file {} exists.".format(file_path))
    else:
        print("The file {} does not exist.".format(file_path))