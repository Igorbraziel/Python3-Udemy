import os
import shutil

path_ = os.path.abspath('.')
original_folder = os.path.join(path_, 'EXEMPLO')
new_test_folder = os.path.join(path_, 'NEW_FOLDER')

if os.path.exists(new_test_folder) == False:
    os.makedirs(new_test_folder)
    
for root, dirs, files in os.walk(original_folder):
    for dir_ in dirs:
        new_path = os.path.join(new_test_folder, dir_)
        os.makedirs(new_path, exist_ok=True)
    
    for file_ in files:
        current_path_file = os.path.join(root, file_)
        new_path = os.path.join(
            root.replace('EXEMPLO', 'NEW_FOLDER'), file_
        )
        shutil.copy(current_path_file, new_path)