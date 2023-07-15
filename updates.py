from config import *
from data import save_json, load_json
import datetime
import requests, json, os
from os.path import isfile, join
from os import listdir
import glob



# TODO: Make install instance
def install_instance():
    pass

# * Getting files and time of changing from minecraft instance directory
def get_files(path, folders):
    files = []
    for folder in folders:
        for file in glob.glob(path+folder+'/**', recursive=True):
            if os.path.isfile(file): files.append({file.replace(path, '') : datetime.datetime.fromtimestamp(os.path.getmtime(file)).strftime("%d/%m/%Y %H:%M:%S")})
    # return the files
    return files

# * Comparing a clientside and serverside mods
def compare(clientside, serverside):
    return {'install': [ i for i in serverside if i not in clientside],'delete': [ i for i in clientside if i not in serverside] }

# * Getting a minecraft folder
def get_minecraft_folder(data, title):
    # Getting minecraft instance folder
    folder = data['folder']+title+'/'
    # if chosen launcher is MultiMC
    folder += '.minecraft/' if data['launcher'] == 'mc' else ''
    # return the folder
    return folder

# * Update instance function
def update_instance(data, server):
    minecraft_folder = get_minecraft_folder(data, server['title'])
    # for installing on client and for deleting from client lists
    install, delete = [], []
    # comparing serverside and clientside file
    out = compare(get_files(minecraft_folder, server['folders']),server['instance_files'])

# * Chosing installing, updating or skipping
def update(data, server):
    if data['current_version'] == server['version']:
        # Skip
        return
    elif data['current_version'] == 0:
        # Install instance
        # ! delete update_instance() here after tests
        update_instance(data, server)
        # install_instance()
    else:
        # Update instance
        update_instance(data, server)

# * Main update Loop
def update_loop():
    # getting data from json
    data = load_json(DATA_FILE)
    # getting latest version information using Cube-API
    server_data = get_server_latest()
    # update function
    update(data, server_data)
    
    
    
# * Get latest version information using Cube-API
def get_server_latest():
    # Creating request to the Cube-API
    request = json.loads(requests.get(CUBE_API_LATEST).text)
    # Returning structured information about latest verison
    return {
        'version': request[1], 
        'title': request[2], 
        'date': request[3], 
        'text': request[4], 
        'folders': json.loads(requests.get(CUBE_API_FOLDERS).text), 
        'instance_files': json.loads(requests.get(CUBE_API_INSTANCE_LIST).text)
        }