import os
import subprocess

def run_program(program_path):
    """
    Runs a program in Windows.
    
    :param program_path: The full path to the program executable.
    """
    if os.name == 'nt':  # Check if the operating system is Windows
        if os.path.isfile(program_path):
            subprocess.run(program_path, shell=True)
            print(f"Program '{program_path}' launched successfully.")
        else:
            print(f"Error: The program '{program_path}' does not exist.")
    else:
        print("Error: This script is designed for Windows systems.")

# Example usage
program_path = r"C:\Program Files\Krita (x64)\bin\krita.exe"  # Path to Microsoft Paint
run_program(program_path)
