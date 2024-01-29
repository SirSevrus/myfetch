import platform
import socket
import os
import psutil
import pyfiglet
from colorama import Fore, init
from datetime import datetime

init(autoreset=True)  # Setting autoreset to True

def get_system_info():
    system = platform.system()
    release = platform.release()
    hostname = socket.gethostname()
    username = os.getlogin()
    return system, release, hostname, username

def get_cpu_usage():
    cpu_usage = psutil.cpu_percent()
    return round(cpu_usage, 1)

def get_memory_info():
    memory = psutil.virtual_memory()
    used_memory = round(memory.used / (1024 ** 2), 1)  # Convert to MB with one decimal place
    total_memory = round(memory.total / (1024 ** 2), 1)
    return used_memory, total_memory

def get_storage_info():
    partitions = psutil.disk_partitions()
    total_storage = 0
    used_storage = 0

    for partition in partitions:
        usage = psutil.disk_usage(partition.mountpoint)
        total_storage += usage.total
        used_storage += usage.used

    converted_used_storage = round(used_storage / (1024 ** 3), 1)  # Convert to GB with one decimal place
    total_storage = round(total_storage / (1024 ** 3), 1)
    return converted_used_storage, total_storage

def get_resolution():
    try:
        if platform.system() == "Windows":
            import ctypes
            user32 = ctypes.windll.user32
            resolution = f"{user32.GetSystemMetrics(0)}x{user32.GetSystemMetrics(1)}"
        else:
            import platform_specific_module  # Replace with the actual module for getting resolution based on OS
            resolution = platform_specific_module.get_resolution()
    except ImportError:
        resolution = "N/A"
    return resolution

def get_time_zone():
    return datetime.now().astimezone().tzinfo

def display_system_info():
    system, release, hostname, username = get_system_info()
    cpu_usage = get_cpu_usage()
    used_memory, total_memory = get_memory_info()
    converted_used_storage, total_storage = get_storage_info()
    resolution = get_resolution()
    time_zone = get_time_zone()

    print(Fore.YELLOW + "System Information:")
    print(Fore.GREEN + f"  OS: {system}")
    print(Fore.GREEN + f"  Release: {release}")
    print(Fore.GREEN + f"  Hostname: {hostname}")
    print(Fore.GREEN + f"  Username: {username}")
    print(Fore.GREEN + f"  CPU Usage: {cpu_usage}%")
    print(Fore.GREEN + f"  Memory Usage: {used_memory} MB / {total_memory} MB")
    print(Fore.GREEN + f"  Storage: {converted_used_storage} GB / {total_storage} GB")
    print(Fore.GREEN + f"  Resolution: {resolution}")
    print(Fore.GREEN + f"  Time Zone: {time_zone}")

if __name__ == "__main__":
    display_system_info()
