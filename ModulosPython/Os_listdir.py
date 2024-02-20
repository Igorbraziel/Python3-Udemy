import os

file_name = 'teste.txt'
current_path = os.path.abspath('.')
directory, _file = os.path.split(current_path)
used_path = os.path.join(directory, file_name)
#print(used_path)
print(directory)
#print(current_path)
#print(_file)

for itens in os.listdir(directory):
    caminho_completo = os.path.join(directory, itens)
    if not os.path.isdir(caminho_completo):
        continue
    for item in os.listdir(caminho_completo):
        print(item)
