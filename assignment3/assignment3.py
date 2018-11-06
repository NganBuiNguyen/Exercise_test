import os
import json
import sys
import glob
import re
from collections import Counter

"""
This is function to get list file json in activities directory
input: location of activities directory
"""
def get_list_file(location):
    for file_name in glob.glob(location + "/*.json"):
        yield open(file_name)
"""
This is function to load categories file
"""
def get_categories_file(list_click, location_file_categories):
    list_category_click = list()
    data_category = json.load(open(location_file_categories,"r"))
    for item_productId in list_click:
        for item in data_category:
            if item_productId['productId'] == item['item_id']:
                list_category_click.append(item['category'])
    return list_category_click                 
     
"""
This is funtion to get activity clicked and get category 
"""
def num_of_clicked_categories(data):
    name = ''
    if data['activity'] == 'clicked':
        return True
"""
This is function to read content json file
"""
def read_json_file(location_file_json, location_file_categories):
    data_json = list()
    dict_json_result = dict()
    for file in get_list_file(location_file_json):
        date_tiem = str(file.name).split('/')[-1].split('.')[0]
        data_json = json.load(file)
        list_click = list(filter(num_of_clicked_categories, data_json))
        list_category = get_categories_file(list_click, location_file_categories)
        dict_json_result[date_tiem] = dict(Counter(list_category))
    print(json.dumps(dict_json_result, sort_keys=True, indent=4))

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Please give me full info!!!")
        sys.exit()

    location_file_json = sys.argv[1]
    location_file_categories = sys.argv[2]

    read_json_file(location_file_json, location_file_categories)

