import unittest
import get_data
import sys


class TestGetData(unittest.TestCase):

    # test for no file
    def test_stdin_no_file(self):
        sys.stdin = 'not_a_file.csv'
        with self.assertRaises(FileNotFoundError) as ex:
            get_data.read_stdin_col(0)
        self.assertEqual(str(ex.exception), sys.stdin + 'was not found.')
