import os, shutil, glob

source_dir = r'C:\\PythonLabs'
dest_dir = 'C:\\Texts'

for root, dirnames, filenames in os.walk(source_dir):
    for file in filenames:
        (shortname, extension) = os.path.splitext(file)
        if extension == ".txt" :
            shutil.copy2(os.path.join(root,file), os.path.join(dest_dir,
                         os.path.relpath(os.path.join(root,file),source_dir)))