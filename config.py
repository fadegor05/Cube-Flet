# Title of app
TITLE = 'CubeFlet'
# Flet Version
CUBEFLET_VERSION = 0
# Main data file name
DATA_FILE = 'data.json'
# Current instance directory (temporarily)
CURRENT_INSTANCE = './../versions'
# Base Json File
BASE_JSON = {
    "info": {
        "username": "",
        "priority_launcher": "",
        "cubeflet_version": CUBEFLET_VERSION,
    },
    "launchers": {
        "tl": {
            "is_active": False,
            "current_version" : 0,
            "folder" : "",

        },
        "cf": {
            "is_active": False,
            "current_version" : 0,
            "folder" : "",
        },
        "mc": {
            "is_active": False,
            "current_version" : 0,
            "folder" : "",
        }
    }
}