import unittest

from puzzles.convert_binary_tree import convert_to_linked_list, Element


class MergeOverlappingIntervalsTest(unittest.TestCase):
    def standard_case_test(self):
        input_tree = Element(100,
                             Element(50,
                                     Element(25,
                                             None,
                                             Element(30, None, None)
                                             ),
                                     Element(75,
                                             Element(60, None, None),
                                             None)
                                     ),
                             Element(200,
                                     Element(125, None, None),
                                     Element(350, None, None))
                             )
        output_list = [Element(25, None, 30),
                       Element(30, 25, 50),
                       Element(50, 30, 60),
                       Element(60, 50, 75),
                       Element(75, 60, 100),
                       Element(100, 75, 125),
                       Element(125, 100, 200),
                       Element(200, 125, 350),
                       Element(350, 200, None)]
        self.assertEqual(convert_to_linked_list(input_tree), output_list)

    def empty_tree_test(self):
        input_data = None
        self.assertEqual(convert_to_linked_list(input_data), [])


if __name__ == '__main__':
    unittest.main()
