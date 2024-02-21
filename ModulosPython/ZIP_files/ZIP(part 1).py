# ZIP - Compactando / Descompactando arquivos com zipfile.ZipFile
import os
import shutil
from pathlib import Path
from zipfile import ZipFile

# Caminhos
CAMINHO_RAIZ = Path(__file__).parent
CAMINHO_ZIP_DIR = CAMINHO_RAIZ / 'aula_186_diretorio_zip'
CAMINHO_COMPACTADO = CAMINHO_RAIZ / 'aula186_compactado.zip'
CAMINHO_DESCOMPACTADO = CAMINHO_RAIZ / 'aula186_descompactado'

CAMINHO_ZIP_DIR.mkdir(exist_ok=True)

def cria_arquivos(qtd: int, path_: Path):
    for i in range(qtd):
        texto = f'file{i}.txt'
        new_path = path_ / texto
        with open(new_path, 'w') as file_:
            message = f'Text Number {i}'
            file_.write(message)
            
cria_arquivos(10, CAMINHO_ZIP_DIR)

with ZipFile(CAMINHO_COMPACTADO, 'w') as zip_file:
    for root, dirs, files in os.walk(CAMINHO_ZIP_DIR):
        for file in files:
            zip_file.write(os.path.join(root, file), file)
            
with ZipFile(CAMINHO_COMPACTADO, 'r') as zip:
    for file in zip.namelist():
        print(file)
    zip.extractall(CAMINHO_DESCOMPACTADO)
   
            
#shutil.rmtree(CAMINHO_ZIP_DIR, ignore_errors=True)
#CAMINHO_COMPACTADO.unlink()
#shutil.rmtree(CAMINHO_DESCOMPACTADO, ignore_errors=True)
#shutil.rmtree(str(CAMINHO_COMPACTADO).replace('.zip', ''), ignore_errors=True)



