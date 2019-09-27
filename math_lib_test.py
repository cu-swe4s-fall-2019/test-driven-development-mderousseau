import unittest
import math_lib
import random
import statistics
import math
import numpy


class TestMathLib(unittest.TestCase):

    # test for empty list
    def test_list_mean_empty_list(self):
        r = math_lib.list_mean(None)
        self.assertEqual(r, None)

    # test mean on known constants
    def test_mean_constants(self):
        r = math_lib.list_mean([1, 1, 1, 1])
        self.assertEqual(r, 1)

    # test stdev on known constants
    def test_stdev_constants(self):
        r = math_lib.list_stdev([1, 2, 3, 4])
        self.assertTrue(math.isclose(r, 1.1180339887499))

    # test mean with random ints
    def test_list_mean_rand_ints(self):
        L = []
        for i in range(100):
            for j in range(10):
                L.append(random.randint(0, 100))
            r = math_lib.list_mean(L)
            e = statistics.mean(L)
            self.assertEqual(r, e)

    # test stdev with random ints
    def test_list_stdev_rand_ints(self):
        L = []
        for i in range(100):
            for j in range(10):
                L.append(
                    random.randint(0, 100))
            r = math_lib.list_stdev(L)
            e = numpy.std(L)
        self.assertTrue(math.isclose(e, r, rel_tol=1e-03))
    
    #test mean with random floats
    def test_list_mean_rand_floats(self):
        L = []
        for i in range(100):
            for j in range(10):
                L.append(
                    random.uniform(0, 100))
            r = math_lib.list_mean(L)
            e = statistics.mean(L)
            self.assertTrue(math.isclose(r, e))
    
    # test stdev with random floats
    def test_list_stdev_rand_floats(self):
        L = []
        for i in range(100):
            for j in range(10):
                L.append(
                    random.uniform(0, 100))
            r = math_lib.list_mean(L)
            e = statistics.mean(L)
            self.assertTrue(math.isclose(r, e))

    # test for error handling with non integers
    def test_list_mean_non_int_in_list(self):
        L = []
        for i in range(10):
            L.append(random.randint(0, 100))
        L.append('X')
        r = math_lib.list_mean(L)
        self.assertRaises(TypeError, r)

    # test stdev for nonintegers
    def test_list_stdev_non_int_in_list(self):
        L = []
        for i in range(10):
            L.append(random.randint(0, 100))
        L.append('X')
        r = math_lib.list_stdev(L)
        self.assertRaises(TypeError, r)


if __name__ == '__main__':
    unittest.main()
