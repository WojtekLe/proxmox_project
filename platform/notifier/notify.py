
from utils import check_json

import sys

def main():

    print("Verify arguments...")
    if len(sys.argv) > 2: 
        print("Too many arguments. Please provide one arguments.")
        exit(1)
    else:    
        file_path = sys.argv[1]

    # check json
    check_json(file_path)

    # send email
    # send_email()


if __name__ == "__main__":
    main()