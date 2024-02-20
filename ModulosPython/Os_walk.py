import os

current_path = os.path.abspath('.')
#print(current_path)
path_ = os.path.join(current_path, 'EXEMPLO')
#print(path_)

for root, dirs, files in os.walk(current_path):
    print(root)
    print(dirs)
    print(files)