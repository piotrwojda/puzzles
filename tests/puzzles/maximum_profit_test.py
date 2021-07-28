import unittest

from puzzles.maximum_profit import find_buy_sell_stock_prices


class MaximumProfitTest(unittest.TestCase):
    def profit_test(self):
        input_data = [10, 7, 8, 9, 5, 20, 3, 10]
        output_data = (20, 5)
        self.assertEqual(find_buy_sell_stock_prices(input_data), output_data)

    def loss_test(self):
        input_data = [20, 18, 17, 15, 13, 11, 5, 0]
        output_data = (17, 18)
        self.assertEqual(find_buy_sell_stock_prices(input_data), output_data)

    def empty_test(self):
        self.assertEqual(find_buy_sell_stock_prices([]), (-1, -1))

    def simple_array_test(self):
        self.assertEqual(find_buy_sell_stock_prices([1, 2]), (2, 1))


if __name__ == '__main__':
    unittest.main()
