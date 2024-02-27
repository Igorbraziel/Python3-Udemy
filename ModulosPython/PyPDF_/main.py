# # PyPDF2 para manipular arquivos PDF (Instalação)
# PyPDF2 é uma biblioteca de manipulação de arquivos PDF feita em Python puro,
# gratuita e de código aberto. Ela é capaz de ler, manipular, escrever e unir
# dados de arquivos PDF, assim como adicionar anotações, transformar páginas,
# extrair texto e imagens, manipular metadados, e mais.
# A documentação contém todas as informações necessárias para usar PyPDF2.
# Link: https://pypdf2.readthedocs.io/en/3.0.0/
# Ative seu ambiente virtual
# pip install pypdf2
from pathlib import Path
from PyPDF2 import PdfReader, PdfWriter

ROOT_PATH = Path(__file__).parent
ORIGINAL_PDF_FOLDER = ROOT_PATH / 'original_pdf'
NEW_FOLDER = ROOT_PATH / 'new_folder'
PDF_FILE = ORIGINAL_PDF_FOLDER / 'R20240216.pdf'

Path.mkdir(NEW_FOLDER, exist_ok=True)

reader = PdfReader(PDF_FILE)
writer = PdfWriter()

with open(NEW_FOLDER / 'copy.pdf', 'wb') as file:
    for page in reader.pages:
        writer.add_page(page)
    writer.write(file)
