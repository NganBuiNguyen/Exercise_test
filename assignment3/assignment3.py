import os
import json
import sys
import glob


"""
This is function to get list file json in activities directory
input: location of activities directory
"""
def get_list_file(location):
    for file_name in glob.glob(location + "/*.json"):
        yield open(os.path.join(location, file_name))
"""
This is function to load categories file
"""
def get_categories_file():
    return json.load(open("/home/nganbui/Documents/Job/assignment3/items_categories.json","r"))
     
"""
This is funtion to get activity clicked and get category 
"""
def num_of_clicked_categories(data):
    list_categories = list()
    name = ''
    if data['activity'] == 'clicked':
        for item in get_categories_file():
            if data['productId'] == item['item_id']:
                print(item['category'])
        return True
"""
This is function to read content json file
"""
def read_json_file(location_file_json):
    data_json = list()
    for file in get_list_file(location_file_json):
        data_json = json.load(file)
        print(len(list(filter(num_of_clicked_categories, data_json))))

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Please give me full info!!!")
        sys.exit()

    location_file_json = sys.argv[1]
    
    read_json_file(location_file_json)

