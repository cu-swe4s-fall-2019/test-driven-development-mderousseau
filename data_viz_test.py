import unittest
import data_viz

class TestDataViz(unittest.TestCase):
    
    def test_file_already_exists(self):
        L = [1, 2, 3, 4]
        open('a_file.png', 'a').close()
        out_file_name = 'a_file.png'
        r = data_viz.boxplot(L, out_file_name)
        self.assertEqual(r, None)
        
        
if __name__ == '__main__':
    unittest.main()