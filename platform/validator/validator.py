import sys
from utils import load_yaml, validate_request, get_vm_size, create_tfvars, check_files_exists
import os


def main():

    print("Verify arguments...")
    if len(sys.argv) > 4: 
        print("Too many arguments. Please provide two arguments.")
        exit(1)
    else:    
        file_path = sys.argv[1]
        sizes_file = sys.argv[2]
        templates_file = sys.argv[3]

    print("Verify yaml files...")
    try:
        current_directory = os.getcwd()
        print("The current working directory is:", current_directory)

        check_files_exists(file_path)

        request = load_yaml(file_path)
        if request is None:
            print("Yaml file {} is empty.".format(file_path))    
            exit(2)

        check_files_exists(sizes_file)

        sizes = load_yaml(sizes_file)
        if sizes is None:
            print("Yaml file sizes.yml is empty.".format(sizes_file))    
            exit(2)

        check_files_exists(templates_file)

        template = load_yaml(templates_file)
        if template is None:
            print("Yaml file sizes.yml is empty.".format(templates_file))    
            exit(2)    

        errors = validate_request(request, sizes)

        if errors:
            for error in errors:
                print(error)
            exit(1)
        else:
            print("Validation yaml files successful")        

    except FileNotFoundError:
        print("Request file not found.")
        exit(1)

    print("Verify vm size...")
    vm_config = get_vm_size(
        request["vm"]["size"],
        sizes
    )

    cpu = vm_config["cpu"]
    memory = vm_config["memory"]
    disk = vm_config

    print(cpu, memory, disk)

    print("Create tfvars...")
    create_tfvars(request, sizes, template)
        

if __name__ == "__main__":
    main()