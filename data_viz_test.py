import unittest
import data_viz

class TestDataViz(unittest.TestCase):
    
    def test_boxplot_no_array(self):
        out_file_name = 'out_file_box.png'
        r = data_viz.boxplot(None, out_file_name)
        self.assertEqual(r, None)
        
    def test_hist_no_array(self):
        out_file_name = 'out_file_hist.png'
        r = data_viz.histogram(None, out_file_name)
        self.assertEqual(r, None)
        
    def test_both_no_array(self):
        out_file_name = 'out_file_both.png'
        r = data_viz.boxplot(None, out_file_name)
        self.assertEqual(r, None)

        
        
if __name__ == '__main__':
    main()