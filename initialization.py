from config import *
import json, os.path
from data import load_json, save_json
from updates import update_loop

# * Main init function
def init():
    data_init() if not os.path.isfile(DATA_FILE) else main_loop()

# * get username function
def get_username():
    # Greeting message
    print('\nДавайте познакомимся, это займет немного времени\n\nУкажите, как я смогу к вам обращаться\n')
    # Getting username
    return input('>> ')

# * Get launcher function
def get_launcher():
    while True:
        print('\nДавайте приступим к параметрам запуска, выберите лаунчер, который вы используете или который вам по душе, а точнее его сокращенную аббривиатуру\n\ntl - Tlauncher Legacy\ncf - CurseForge\nmc - MultiMC\n')
        # Getting launcher
        priority_launcher = input('>> ')
        # return priotity_launcher if this launcher type exists
        if priority_launcher in ['tl', 'cf', 'mc']: return priority_launcher
        else: print('\nПопробуйте еще раз...\n')

# * Get launcher path function
def get_launcher_path():
    while True:
        print('\nТеперь укажите путь до папки версий (установок/модпаков) вашего лаунчера: \n\nTlauncher Legacy: ../.minecraft/versions\n(например: C:/Users/someuser/AppData/Roaming/.minecraft/versions)\n\nCurseForge: ../*Название папки с CurseForge*/minecraft/Instances\n(например: C:/Program Files (x86)/Overwolf/CurseForge/minecraft/Instances)\n\nMultiMC: ../MultiMC/instances\n(напримерр: C:/MultiMC/instances)\n')
        # Getting launcher path
        folder = input('>> ')
        # Correcting path if it needed
        folder += '/' if folder[-1] != '/' else ''
        # return priotity_launcher if this launcher type exists
        if os.path.isdir(folder): return folder
        else: print('\nПопробуйте еще раз...\n')

# * Data init function
def data_init():
    # Setting data to base json
    data = BASE_JSON
    # Get username
    data['username'] = get_username()
    # Get launcher settings
    data['launcher'] = get_launcher()
    # Get launcher path
    data['folder'] = get_launcher_path()
    # Saving json file with collected data
    save_json(DATA_FILE, data)
    main_loop()

# * Printing greeting out
def print_greetings(data):
    print(f'\nПриветствуем, {data["username"]}\nПроверка обновлений в {LAUNCHERS_DECODES[data["launcher"]]}...\n')

# * Main loop
def main_loop():
    data = load_json(DATA_FILE)
    print_greetings(data)
    update_loop()
