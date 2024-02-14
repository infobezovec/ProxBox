
import argparse
import random
import sys
from termcolor import colored
from Creator import File_creator


version = '0.1'

#TODO WRITE FUNCTION WICH PLACES FILES AT DIRECTORIES USING SSH/
def place_files_remotly():
    pass

#TODO WRITE FUNCTION WICH PLACES FILES AT DIRECTORIES USING LOCAL
def place_files_localy():
    pass

#TESTED
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
    
#TESTED
def parce_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", required=True, help='Path to Malware sample')
    parser.add_argument("-t", type=int, help='Timeout for execution')
    arg = parser.parse_args()
    return arg

#TESTED
def read_file(path):
    with open(path, 'rb') as file:
        sample = file.read()
    return sample

def main():
    print_logo()
    argv = parce_arguments()
    timeout = argv.t
    file_path = argv.f


if __name__ == "__main__":
    main()