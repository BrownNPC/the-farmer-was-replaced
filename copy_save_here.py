import os
from shutil import copytree, rmtree

save_dir = "C:\\Users\\linus\\AppData\\LocalLow\\TheFarmerWasReplaced\\TheFarmerWasReplaced\\Saves\\Save0"
destination_dir = "./src"

# Ensure the destination directory does not already exist
if os.path.exists(destination_dir):
    if os.path.isfile(destination_dir):
        os.remove(destination_dir)
    else:
        rmtree(destination_dir)

# Copy the entire directory
copytree(save_dir, destination_dir)
