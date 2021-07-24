import unittest

from puzzles.move_zeroes import move_zeros_to_left

class MoveZeroesTest(unittest.TestCase):
    def standard_test(self):
        input = [0, 1, 0, 2, 0, 3]
        output = [0, 0, 0, 1, 2, 3]
        self.assertEqual(move_zeros_to_left(input), output)

    def empty_array_test(self):
        input = []
        self.assertEqual(move_zeros_to_left(input), input)

    def no_zeroes_test(self):
        input = [1, 2, 3]
        self.assertEqual(move_zeros_to_left(input), input)

    def only_zeroes_test(self):
        input = [0, 0 ,0]
        self.assertEqual(move_zeros_to_left(input), input)


if __name__ == '__main__':
    unittest.main()
