import unittest
import data_viz

class TestDataViz(unittest.TestCase):
    
    def test_no_array(self):
        out_file_name = 'out_file_name.png'
        r = data_viz.boxplot(None, out_file_name)
        self.assertEqual(r, None)
        
        
if __name__ == '__main__':
    main()