# class that saves dictionary to file
import json
import time


def save_to_file(some_dict):
    timestr = time.strftime("%Y%m%d-%H%M%S")

    with open("result_"+timestr+".txt", 'w', encoding="utf-8") as file:
        file.write(json.dumps(some_dict))
        print('File '+"result_"+timestr+".txt created successfully")
