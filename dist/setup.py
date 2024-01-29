import argparse
import shutil
import os

def find_bin_path():
    # Get the directories that are in the system PATH
    path_directories = os.environ.get('PATH', '').split(os.pathsep)

    # Check each directory for the existence of 'bin' or 'Scripts'
    for directory in path_directories:
        bin_path = os.path.join(directory, 'bin')  # On Unix-like systems
        scripts_path = os.path.join(directory, 'Scripts')  # On Windows

        if os.path.exists(bin_path) and os.path.isdir(bin_path):
            return bin_path
        elif os.path.exists(scripts_path) and os.path.isdir(scripts_path):
            return scripts_path

    # If 'bin' or 'Scripts' directory is not found, return the first directory in PATH
    return path_directories[0]

def add_to_bin(source_exe, destination_bin):
    source_path = shutil.which(source_exe)

    if source_path:
        destination_path = os.path.join(destination_bin, source_exe)

        # Copy the executable to the 'bin' directory
        shutil.copy(source_path, destination_path)

        print(f"{source_exe} added to {destination_bin}")
    else:
        print(f"{source_exe} not found in the system PATH")

def main():
    parser = argparse.ArgumentParser(description='Add an executable to the system\'s bin directory')
    parser.add_argument('--add', help='Path to the executable file to be added', required=True)
    args = parser.parse_args()

    # Find the 'bin' or 'Scripts' directory in the system PATH
    bin_directory = find_bin_path()

    # Add the specified executable to the 'bin' directory
    add_to_bin(os.path.basename(args.add), bin_directory)

if __name__ == "__main__":
    main()
