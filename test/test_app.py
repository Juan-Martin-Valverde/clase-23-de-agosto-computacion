import unittest

from app.multi import multiplicacion

class test_multi(unittest.TestCase):
    def test_multiplicacion(self):
        self.assertEqual(multiplicacion(2,3), 6)

if __name__=='__main__':
    unittest.main()

#