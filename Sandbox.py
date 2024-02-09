
import argparse
import random
from termcolor import colored
from Creator import File_creator

linux_paths = []
version = '0.1'

def generate_path(file_type, id):
    path_list = ['']

    if file_type == 'xls':
        path = path_list[1][id]
    elif file_type == 'docx':
        path = path_list[2][id]
    elif file_type == 'pptx':
        path = path_list[3][id]
    elif file_type == 'txt':
        path = path_list[4][id]
    elif file_type == 'txt':
        path = path_list[5][id]
    return path

#TODO WRITE FUNCTION WICH PLACES FILES AT DIRECTORIES USING SSH/
def place_files_remotly():
    pass

#TODO WRITE FUNCTION WICH PLACES FILES AT DIRECTORIES USING LOCAL
def place_files_localy():
    pass

def print_logo():
    color = ['green', 'yellow', 'blue', 'magenta', 'cyan']
    print(colored("""
 _______                                _______                      
/       \                              /       \                     
$$$$$$$  | ______    ______   __    __ $$$$$$$  |  ______   __    __ 
$$ |__$$ |/      \  /      \ /  \  /  |$$ |__$$ | /      \ /  \  /  |
$$    $$//$$$$$$  |/$$$$$$  |$$  \/$$/ $$    $$< /$$$$$$  |$$  \/$$/ 
$$$$$$$/ $$ |  $$/ $$ |  $$ | $$  $$<  $$$$$$$  |$$ |  $$ | $$  $$<  
$$ |     $$ |      $$ \__$$ | /$$$$  \ $$ |__$$ |$$ \__$$ | /$$$$  \ 
$$ |     $$ |      $$    $$/ /$$/ $$  |$$    $$/ $$    $$/ /$$/ $$  |
$$/      $$/        $$$$$$/  $$/   $$/ $$$$$$$/   $$$$$$/  $$/   $$/ 
""", color[random.randint(0, len(color)-1)]))
    print (colored("ProxMox based all authomatic open-source sandbox", "green", attrs=['bold']))
    print (colored('by USERNAME' + '\t\t\t\t\t\tversion:' + version))
    
#TODO add help and all args to mode
def print_help():
    pass

def main():
    print_logo()

if __name__ == "__main__":
    main()