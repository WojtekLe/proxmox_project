import sys
from utils import load_yaml


def main():

    if len(sys.argv) > 2: 
        print("Too many arguments. Please provide one yaml file name.")
        exit(1)
    else:    
        file_path = sys.argv[1] 

    try:

        request = load_yaml(file_path)
        if request == None:
            print("Yaml file empty.")    
            exit(2)
        print(request)

    except FileNotFoundError:

        print("Request file not found.")

        exit(1)

if __name__ == "__main__":
    main()    