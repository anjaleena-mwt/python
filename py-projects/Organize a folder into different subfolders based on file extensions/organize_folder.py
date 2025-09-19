import os
import shutil

to_organize_folder = "C:/Users/MT102/Documents/MWT/VS/python/Python Projects/organize_folder/to_organize"

#Make folder if not exists
def make_folder(path):
    if not os.path.exists(path): 
        os.makedirs(path)

# Organizing the files
def organize(folder):
    for filename in os.listdir(folder):         # go through each item in the folder
        filepath = os.path.join(folder, filename)  #  lists all files and subfolders inside the given folder

        if os.path.isdir(filepath):   # if it's a folder, then it will skip it
            continue

        # Gets the file extension (eg: .txt, .jpg, .pdf)
        ext = os.path.splitext(filename)[1].lower()

        # Decides the folder name based on extension
        if ext == "":   # if file has no extension
            new_folder = os.path.join(folder, "no_extension")
        else:
            new_folder = os.path.join(folder, ext[1:])  # remove the dot (.) from extension

        # Create folder if it doesn’t exist
        make_folder(new_folder)

        # Moves the file into the right folder
        shutil.move(filepath, os.path.join(new_folder, filename))


organize(to_organize_folder)
print("✅ Completed organizing files in:", to_organize_folder)
