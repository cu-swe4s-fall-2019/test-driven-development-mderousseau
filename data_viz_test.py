import unittest
import data_viz

class TestDataViz(unittest.TestCase):
    
    def test_file_already_exists(self):
        L = [1, 2, 3, 4]
        open('a_file.png', 'a').close()
        out_file_name = 'a_file.png'
        r = data_viz.boxplot(L, out_file_name)
        a = data_viz.histogram(L, out_file_name)
        b = data_viz.combo(L, out_file_name)
        # repeat test in here just because its so redundant/simple
        self.assertEqual(r, None)
        self.assertEqual(a, None)
        self.assertEqual(b, None)
   
if __name__ == '__main__':
    unittest.main()