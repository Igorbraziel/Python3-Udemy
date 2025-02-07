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
from calculator import soma 

class TestCalculator(unittest.TestCase):
    def test_soma_5_e_5_deve_retornar_10(self):
        self.assertEqual(soma(5, 5), 10)
        
    def test_soma_5_e_10_deve_retornar_15(self):
        self.assertEqual(soma(5, 10), 15)
        
    def soma_x_nao_inteiro__com_y_inteiro_e_retorna_assertionerror(self):
        with self.assertRaises(AssertionError):
            soma('1', 2)
        
if __name__ == '__main__':
    unittest.main(verbosity=2)