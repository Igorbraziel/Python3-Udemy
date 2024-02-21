from dotenv import load_dotenv
import os

load_dotenv()

print(os.getenv("BD_USER"))