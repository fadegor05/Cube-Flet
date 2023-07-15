#
# *   DO NOT CHANGE ANYTHING IF YOU DO NOT KNOW WHAT YOU ARE DOING   *
#
# * Title of app
TITLE = 'CubeFlet'
# * Flet Version
CUBEFLET_VERSION = 0
# * Main data file name
DATA_FILE = 'data.json'
# * Cube-API Addresses (Cube-API: https://github.com/fadegor05/Cube-API)
# Cube-API getting information about latest instance version
CUBE_API_LATEST = 'http://127.0.0.1:5000/get_latest'
# Cube-API getting list of all files from latest instance version
CUBE_API_INSTANCE_LIST = 'http://127.0.0.1:5000/get_instance_list'
# Cube-API getting list of folders that requires updates or checking
CUBE_API_FOLDERS = 'http://127.0.0.1:5000/get_folders'
# * Decodes of launcher abbreviations
LAUNCHERS_DECODES = {
    'tl': 'TLauncher Legacy',
    'cf': 'CurseForge',
    'mc': 'MultiMC'
}
# * Base Json File
BASE_JSON = {
    "username": "",
    "launcher": "",
    "cubeflet_version": CUBEFLET_VERSION,
    "current_version": "",
    "folder": ""
}