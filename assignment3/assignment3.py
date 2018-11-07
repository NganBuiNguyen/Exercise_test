import os
import json
import sys
import glob
import re
from collections import Counter

location_file_categories = os.getcwd() + "/assignment3/items_categories.json"
"""
This is function to get list file json in activities directory
input: location of activities directory
"""
def get_list_file(location):
    for file_name in glob.glob(location + "/*.json"):
        yield open(file_name)                

"""
This is funtion to get activity clicked and get category 
"""
def num_of_clicked(data):
    data_category = json.load(open(location_file_categories,"r"))
    name = ''
    if data['activity'] == 'clicked':
        for item in data_category:
            if data['productId'] == item['item_id']:
                data['productId'] = item['category']
        return True

def count_categorie(list_click):
    list_category = list()
    for item in list_click:
        list_category.append(item['productId'])    
    return list_category
    
def num_of_click_by_categorie(list_click):
    list_result = list()
    dict_json_result_click = dict()
    for item in list_click:
        dict_json_result_click['date'] = item['date']
        dict_json_result_click['category'] = item['productId']
        list_count = count_categorie(list_click)
        dict_json_result_click['clicks'] = list_count.count(item['productId'])
    list_result.append(dict_json_result_click)
    print(list_result)

def count_categorie_user(product_id, list_click):
    list_user = list()
    for item in list_click:
        if product_id == item['productId']:
            list_user.append(item['userId'])
    return list_user


def num_of_users_by_categorie(list_click):
    list_result = list()
    dict_json_result_click = dict()
    for item in list_click:
        dict_json_result_click['date'] = item['date']
        dict_json_result_click['category'] = item['productId']
        dict_json_result_click['users'] = item['userId']
        list_user = count_categorie_user(item['productId'], list_click)
        dict_json_result_click['num_users'] = list_user.count(item['userId'])
    list_result.append(dict_json_result_click)
    print(list_result)


"""
This is function to read content json file
"""
def read_json_file(location_file_json, choose):
    data_json = list()
    dict_json_result_click = dict()
    dict_json_result_user = dict()
    for file in get_list_file(location_file_json):
        date_tiem = str(file.name).split('/')[-1].split('.')[0]
        data_json = json.load(file)
        list_click = list(filter(num_of_clicked, data_json))
        if choose == 0:
            num_of_click_by_categorie(list_click)
        elif choose == 1:
            num_of_users_by_categorie(list_click)


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Please give me full info!!!")
        sys.exit()

    location_file_json = sys.argv[1]
    choose = int(sys.argv[2])

    read_json_file(location_file_json, choose)

