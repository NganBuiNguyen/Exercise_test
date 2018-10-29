import os
import sys
from datetime import datetime
from collections import defaultdict
import json
import collections

"""
This is funtion to load json users_online file
"""
def load_json_users_online(location_file_user_online):
    with open(location_file_user_online) as f:
        data_users_online = json.load(f)
    return data_users_online

"""
This is funtion to load json users_vendor file
"""
def load_json_users_vendor(location_file_vendor):
    with open(location_file_vendor) as f:
        data_users_vendor = json.load(f)
    return data_users_vendor    

"""
This is funtion to get users online every day.
    input: location of json users_online file 
    output: Dictionary with key is date and value is profile_id
"""
def get_users_online(location_file_user_online):
    count_users = 0
    list_profile_id = list()
    dict_date_user = defaultdict(list)
    data_users_online = load_json_users_online(location_file_user_online)
    for data_user in data_users_online:
        datetime_object = datetime.strptime(data_user['date'], \
                                                        '%Y-%m-%d %H:%M:%S')
        list_profile_id.append((datetime_object.date(), \
                                                data_user['profile_id']))
    for key, value in list_profile_id:
        dict_date_user[key].append(value)
    return dict_date_user

"""
This is funtion to get vendor base on profile_id.
    input: Dictionary with key is date and value is profile_id
           Location of json users_vendor file  
"""
def get_vendor(dict_date_user, location_file_vendor):
    list_count_vendor = list()
    print("=============================== SUM TOTAL ====================")
    for date, value in dict_date_user.items():
        print("Number of user online on " + str(date) + " is " + \
                                                            str(len(value)))
        if len(value) >= 1:
            data_users_vendor = load_json_users_vendor(location_file_vendor)
            list_vendor = list()
            for profile_id in value:
                for data_vendor in data_users_vendor:
                    if profile_id == data_vendor['id']:
                        list_vendor.append(data_vendor['vendorid'])
            for item, count in collections.Counter(list_vendor).items():
                print(" with vendor " + item)
    print("================================ END ============" + \
                                                            "============")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Please give me full info!!!")
        sys.exit()

    # location of json users_online file
    location_file_user_online = sys.argv[1]

    # location of json users_vendor file
    location_file_vendor = sys.argv[2] 
    
    dict_date_user = get_users_online(location_file_user_online)
    get_vendor(dict_date_user, location_file_vendor)