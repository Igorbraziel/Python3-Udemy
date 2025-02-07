"""
TDD - Test driven development (Desenvolvimento dirigido a testes)

Red
Parte 1 -> Criar o teste e ver falhar

Green
Parte 2 -> Criar o código e ver o teste passar

Refactor
Parte 3 -> Melhorar meu código
"""
try:
    import os
    import sys
    
    sys.path.append(
        os.path.abspath(
            os.path.join(
                os.path.dirname(__file__),
                '../src'
            )
        )
    )
except: 
    raise

import unittest
from baconwitheggs import bacon_with_eggs

class TestBaconWithEggs(unittest.TestCase):
    def test_bacon_with_eggs_must_raise_assertion_error_if_not_receive_int(self):
        with self.assertRaises(AssertionError):
            bacon_with_eggs('1')
            
    def test_must_return_bacon_with_eggs_if_input_is_multiple_of_3_and_5(self):
        inputs = (15, 30, 45, 60)
        output = 'Bacon With Eggs'
        
        for _input in inputs:
            with self.subTest(_input=_input, output=output):
                self.assertEqual(
                    bacon_with_eggs(_input),
                    output,
                    msg=f"the input {_input} didn't returned {output}"
                )
                
    def test_must_return_starve_if_input_is_not_multiple_of_3_and_5(self):
        inputs = (1, 2, 4, 7, 8)
        output = 'Starve'
        
        for _input in inputs:
            with self.subTest(_input=_input, output=output):
                self.assertEqual(
                    bacon_with_eggs(_input),
                    output,
                    msg=f"the input {_input} didn't returned {output}"
                )
                
    def test_must_return_bacon_if_input_is_only_multiple_of_3(self):
        inputs = (3, 6, 9, 12, 18, 21)
        output = 'Bacon'
        
        for _input in inputs:
            with self.subTest(_input=_input, output=output):
                self.assertEqual(
                    bacon_with_eggs(_input),
                    output,
                    msg=f"the input {_input} didn't returned {output}"
                )
            
    def test_must_return_eggs_if_input_is_only_multiple_of_5(self):
        inputs = (5, 10, 20, 25, 35, 40)
        output = 'Eggs'
        
        for _input in inputs:
            with self.subTest(_input=_input, output=output):
                self.assertEqual(
                    bacon_with_eggs(_input),
                    output,
                    msg=f"the input {_input} didn't returned {output}"
                )
            

if __name__ == '__main__':
    unittest.main(verbosity=2)
