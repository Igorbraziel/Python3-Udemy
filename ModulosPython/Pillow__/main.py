from PIL import Image
from pathlib import Path

ROOT_PATH = Path(__file__).parent
ORIGINAL_IMAGE = ROOT_PATH / 'image.png'
NEW_IMAGE = ROOT_PATH / 'new_image.png'

pil_image = Image.open(ORIGINAL_IMAGE)
width, height = pil_image.size
info = pil_image.info

new_width = round(width * 3)
new_height = round(height * new_width / width)

new_image = pil_image.resize(size=(new_width, new_height))

new_image.save(
    NEW_IMAGE, 
    optmize= True,
)

