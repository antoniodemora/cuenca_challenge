import unittest
from nqueen import find_nqueen

class NQueenTestCase(unittest.TestCase):
    def test_invalid_n(self):
        with self.assertRaises(ValueError): find_nqueen(4, False)

    def test_solution_count(self):
        n = 8
        expected_count = 92
        solution_count, solution_set = find_nqueen(n, False)
        self.assertEqual(expected_count, solution_count)

        n = 10
        expected_count = 724
        solution_count, solution_set = find_nqueen(n, False)
        self.assertEqual(expected_count, solution_count)

    def test_solution_set(self):
        # for N=8, we are going to test 5 out of 12 of the "fundamental" solutions:
        solution_count, solution_set = find_nqueen(display=False)

        # Fundamental solution #1
        expected_set = (6, 4, 2, 0, 5, 7, 1, 3)
        self.assertIn(expected_set, solution_set)

        # Fundamental solution #2
        expected_set = (7, 1, 4, 2, 0, 6, 3, 5)
        self.assertIn(expected_set, solution_set)

        # Fundamental solution #3
        expected_set = (7, 1, 3, 0, 6, 4, 2, 5)
        self.assertIn(expected_set, solution_set)

        # Fundamental solution #4
        expected_set = (4, 7, 3, 0, 6, 1, 5, 2)
        self.assertIn(expected_set, solution_set)

        # Fundamental solution #5
        expected_set = (3, 7, 0, 4, 6, 1, 5, 2)
        self.assertIn(expected_set, solution_set)


if __name__ == "__main__":
    unittest.main()