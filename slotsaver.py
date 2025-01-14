import bpy
import os

# Define the output folder as the location of the current `.blend` file
output_folder = bpy.path.abspath("//renders")

# Ensure the folder exists
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Access the Render Result image
render_result = bpy.data.images.get("Render Result")

if render_result is None:
    print("Render Result image not found!")
else:
    # Loop through all render slots and save them
    for i in range(len(render_result.render_slots)):  # Iterate over available render slots
        # Set the active render slot
        render_result.render_slots.active_index = i

        # Check if the active render slot has data
        if render_result.has_data:
            # Define the file path for saving
            filename = f"render_slot_{i+1}.png"  # Adjust numbering (1-based)
            filepath = os.path.join(output_folder, filename)

            # Save the render slot
            try:
                render_result.save_render(filepath)
                print(f"Saved: {filepath}")
            except RuntimeError as e:
                print(f"Failed to save Render Slot {i+1}: {e}")
        else:
            print(f"Render Slot {i+1} is empty or has no data.")

print("All render slots processed.")