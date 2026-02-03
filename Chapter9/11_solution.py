# Write a python program to rename a file to “renamed_by_ python.txt

from pathlib import Path

# Create a path object for the file
file_path = Path("copyfile.txt")

# Check if it exists before renaming
if file_path.exists():
    file_path.rename("renamed_by_python.txt")
    print("File renamed successfully!")
else:
    print("The source file does not exist.")

