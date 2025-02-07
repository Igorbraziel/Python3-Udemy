import requests

class Person:
    def __init__(self, name, last_name):
        self.name = name
        self.last_name = last_name
        self.data_obtained = False
        
    def get_all_data(self):
        response = requests.get('fake_url')
        
        if response.ok:
            self.data_obtained = True
            return 'CONECTED'
        
        self.data_obtained = False
        return '404 PAGE NOT FOUND' 