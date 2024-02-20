import os

path_ = os.path.join('Documentos', 'GitHub', 'Python3-Udemy', 'ModulosPython', 'teste.txt')
directory, file_ = os.path.split(path_)
#print(path_)
print(directory)
print(file_)
print(os.path.exists(path_))