# utils.py>

import yaml

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
