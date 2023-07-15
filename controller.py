from config import *
import datetime
from data import save, load
import os

# Get current files and directories on pc function
'''
def get_current():
    files = {}
    for directory in os.listdir(CURRENT_INSTANCE):
        temp_files = []
        for file in os.listdir(CURRENT_INSTANCE+'/'+directory):
            temp_files.append({file : datetime.datetime.fromtimestamp(os.path.getmtime(CURRENT_INSTANCE+'/'+directory+'/'+file))})
        files[directory] = temp_files
    return files

def get_server():
    return ['']

def compare():
    print(get_current())
'''
