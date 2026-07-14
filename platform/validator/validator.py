import sys
from utils import *


def main():

    file_path = sys.argv[1] 

    request = load_yaml(file_path)

    print(request)

if __name__ == "__main__":
    main()    