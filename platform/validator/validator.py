import sys
from utils import load_yaml, validate_request


def main():

    if len(sys.argv) > 2: 
        print("Too many arguments. Please provide one yaml file name.")
        exit(1)
    else:    
        file_path = sys.argv[1] 

    try:

        request = load_yaml(file_path)
        if request is None:
            print("Yaml file empty.")    
            exit(2)

        sizes = load_yaml("platform\\validator\\sizes.yml")

        errors = validate_request(request, sizes)

        if errors:
            for error in errors:
                print(error)
            exit(1)
        else:
            print("Validation successful")        

    except FileNotFoundError:

        print("Request file not found.")

        exit(1)

if __name__ == "__main__":
    main()