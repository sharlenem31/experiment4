import unittest2 
import calc 

class TestClass(unittest2.TestCase): 
    def test_add(self): 
        result = calc.add(10, 5) 
        self.assertEqual(result, 15) 
        self.assertEqual(calc.add(10, 1), 11) 
        
    def test_subtract(self): 
        result = calc.subtract(10, 5) 
        self.assertEqual(result, 5) 
        
    def test_divide(self): 
        self.assertEqual(calc.divide(10, 2), 5) 
        
        with self.assertRaises(ValueError): 
            calc.divide(10, 0)

    def test_multiply(self): 
        self.assertEqual(calc.multuply(12, -3), -36) 
        
if __name__ == "__main__": 
    unittest2.main()
