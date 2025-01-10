import bpy
import os
import sys
from datetime import datetime

def create_and_save_blend(base_path, file_name):
    """
    Creates folders and saves the current Blender file with validation and error checking.

    :param base_path: The base directory where the .blend file will be saved.
    :param file_name: The name of the .blend file to be saved.
    """
    try:
        # Ensure base path exists or create it
        if not os.path.exists(base_path):
            print(f"Creating directory: {base_path}")
            os.makedirs(base_path)
        else:
            print(f"Directory already exists: {base_path}")

        # Create subfolders for related assets
        subfolders = ["3D", "PSD", "Images", "Textures"]
        for folder in subfolders:
            folder_path = os.path.join(base_path, folder)
            if not os.path.exists(folder_path):
                print(f"Creating subdirectory: {folder_path}")
                os.makedirs(folder_path)

        # Build full path to the .blend file
        full_file_path = os.path.join(base_path, file_name)

        # Log existing file overwrite status
        if os.path.exists(full_file_path):
            print(f"Overwriting existing file: {full_file_path}")
        else:
            print(f"Saving new file: {full_file_path}")

        # Save the current Blender file
        bpy.ops.wm.save_as_mainfile(filepath=full_file_path, check_existing=False)
        print(f"File successfully saved at: {full_file_path}")

    except Exception as e:
        print(f"Error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    # Set base path and generate folder and file name
    base_path_root = "C:\\LazyBlender\\BlenderScene\\"
    current_time = datetime.now().strftime("Date_%d_%m_%Y_Time_%H_%M")
    project_folder = f"Scene_{current_time}"
    full_path = os.path.join(base_path_root, project_folder)
    file_name = f"Scene_{current_time}.blend"

    # Call the function to create folders and save the .blend file
    create_and_save_blend(full_path, file_name)
