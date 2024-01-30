#!/usr/bin/env python3
import os
import platform
import time
from colorama import Fore, init

init(autoreset = True) # Setting Autorest to True

def process_deps(list_name):
    cmd = ''
    for dep in list_name:
        print(Fore.CYAN + '[LIB] ' + Fore.YELLOW + f'{dep}')
        cmd = cmd + dep + ' '
    os.system(f'pip install {cmd} --no-warn-script-location')

deps = ['pyfiglet', 'colorama', 'psutil']

usr_bin = '/usr/bin'

# Checking that is user is running with sudo or not
if os.geteuid() != 0:
    print(Fore.RED + '[ERROR]' + Fore.YELLOW + ' This setup must be runned with sudo!')
    exit(1)

platform_name = platform.system()

if platform_name != 'Linux':
    print(Fore.RED + '[ERROR]' + Fore.YELLOW + f' The Setup You are using is a linux based setup!\nPlease Use a favourable setup for your os type.\nYour OS Type :- {platform_name}')
    time.sleep(2)

elif platform_name == 'Linux':
    os.system('cls')
    print(Fore.CYAN + '[INFO]' + Fore.GREEN + ' Wait a sec i am just looking into your system,a new install is coming on your side...')
    time.sleep(1)
    print(Fore.CYAN + '[SETUP] ' + Fore.MAGENTA + 'Installing Libraries...')
    process_deps(deps)
    print(Fore.CYAN + '[SETUP] ' + Fore.GREEN + 'Installed Libraries...')
    time.sleep(2)
    print(Fore.CYAN + '[SETUP] ' + Fore.MAGENTA + f'Copying the program to {usr_bin} ...')
    os.system(f'cp myfetch.py {usr_bin}/myfetch')
    time.sleep(1)
    print(Fore.CYAN + '[INFO] ' + Fore.GREEN + 'Install Complete from Our side...')
    time.sleep(1)
    print(Fore.CYAN + '[TEST] ' +  Fore.YELLOW + "Running command 'myfetch'...")
    time.sleep(1)
    os.system('myfetch')
