import unittest

from puzzles.merge_overlapping_intervals import merge_intervals, Pair
from puzzles.move_zeroes import move_zeros_to_left


class MergeOverlappingIntervalsTest(unittest.TestCase):
    def standard_case_test(self):
        input_data = [Pair(1, 2), Pair(2, 3), Pair(3, 4), Pair(10, 20), Pair(15, 25)]
        output_data = [Pair(1, 4), Pair(10, 25)]
        self.assertEqual(merge_intervals(input_data), output_data)

    def empty_array_test(self):
        input_data = []
        self.assertEqual(merge_intervals(input_data), input_data)

    def no_overlap_test(self):
        input_data = [Pair(1, 2), Pair(3, 4), Pair(5, 6), Pair(7, 8)]
        self.assertEqual(merge_intervals(input_data), input_data)

    def single_element_test(self):
        input_data = [Pair(1, 2)]
        self.assertEqual(merge_intervals(input_data), input_data)


if __name__ == '__main__':
    unittest.main()
