import os
import json
import sys
import glob

files = []
"""
This is function to get list file json in activities directory
input: location of activities directory
"""
def get_list_file(location):
    for file_name in glob.glob(location + "/*.json"):
        yield open(os.path.join(location, file_name))

"""
This is function to read content json file
"""
def read_json_file(location_file_json):
    list_file = list()
    for file in get_list_file(location_file_json):
        data_json = json.load(file)
    

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Please give me full info!!!")
        sys.exit()

    location_file_json = sys.argv[1]
    
    read_json_file(location_file_json)

