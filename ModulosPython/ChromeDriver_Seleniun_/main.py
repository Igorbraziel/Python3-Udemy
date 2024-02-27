from pathlib import Path
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

ROOT_FOLDER = Path(__file__).parent
path_chrome_drive = ROOT_FOLDER / 'drivers' / 'chromedriver'

chrome_options = webdriver.ChromeOptions()
chrome_service = Service(executable_path=str(path_chrome_drive))
chrome_browser = webdriver.Chrome(
    options = chrome_options, 
    service = chrome_service
)

chrome_browser.get('https://google.com.br/')

