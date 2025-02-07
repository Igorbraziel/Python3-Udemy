"""
class Pessoa
    __init__
        nome str
        sobrenome str
        dados_obtidos bool (inicia False)

    API:
        obter_todos_os_dados -> method
            OK
            404

            (dados_obtidos se torna True se dados obtidos com sucesso)
"""

import unittest
from unittest.mock import patch
from person import Person

class TestPerson(unittest.TestCase):
    def setUp(self):
        self.person = Person('Igor', 'Braziel')
        return super().setUp()
    
    def test_attr_name_have_the_correct_value(self):
        self.assertEqual(self.person.name, 'Igor')
        
    def test_attr_last_name_have_the_correct_value(self):
        self.assertEqual(self.person.last_name, 'Braziel')
        
    def test_attr_data_obtained_start_false(self):
        self.assertFalse(self.person.data_obtained)
        
    def test_attr_name_is_str(self):
        self.assertIsInstance(self.person.name, str)
        
    def test_attr_last_name_is_str(self):
        self.assertIsInstance(self.person.last_name, str)
        
    def test_get_all_data_success_OK(self):
        with patch('requests.get') as fake_request:
            fake_request.return_value.ok = True
            self.assertEqual(self.person.get_all_data(), 'CONECTED')
            self.assertTrue(self.person.data_obtained)
            
    def test_get_all_data_failure_404(self):
        with patch('requests.get') as fake_request:
            fake_request.return_value.ok = False
            self.assertEqual(self.person.get_all_data(), '404 PAGE NOT FOUND')
            self.assertFalse(self.person.data_obtained)

if __name__ == '__main__':
    unittest.main(verbosity=2)