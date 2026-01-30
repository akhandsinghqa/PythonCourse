import os

# Specify the directory path
path = "/home/akhand/Downloads"  
# Change this to the directory you want to list

try:
    # Get the list of files and folders
    contents = os.listdir(path)
    
    # Print directory contents
    print(f"Contents of '{path}':")
    for item in contents:
        print(item)

except FileNotFoundError:
    print(f"Error: The directory '{path}' does not exist.")
except PermissionError:
    print(f"Error: Permission denied for accessing '{path}'.")

# This the end of the program.
# Please enjoy
