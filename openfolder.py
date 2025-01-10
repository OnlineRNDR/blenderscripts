import os
import subprocess

def open_folder_in_explorer(folder_path):
    """
    Opens a folder in Windows Explorer.
    
    :param folder_path: The path to the folder to open.
    """
    if os.name == 'nt':  # Check if the operating system is Windows
        if os.path.isdir(folder_path):
            subprocess.run(f'explorer "{folder_path}"', shell=True)
            print(f"Folder '{folder_path}' opened in Windows Explorer.")
        else:
            print(f"Error: The folder '{folder_path}' does not exist.")
    else:
        print("Error: This script is designed for Windows systems.")

# Example usage
folder_path = r"C:\Scripts"  # Replace with the path to your folder
open_folder_in_explorer(folder_path)
