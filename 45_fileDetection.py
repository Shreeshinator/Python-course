import os

# Check if a file exists

file_path = "README.md"

if os.path.isfile(file_path):
    print(f"The file '{file_path}' exists.")
    if os.path.isfile(file_path):
        print(f"The file '{file_path}' is a regular file.")
else:
    print(f"The file '{file_path}' does not exist.")