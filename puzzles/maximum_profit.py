import sys


def find_buy_sell_stock_prices(array):

    print(f"Input array: {array}")

    if array is None or len(array) < 2:
        return -1, -1
    else:
        current_buy = array[0]
        best_sell = array[1]
        best_profit = best_sell - current_buy

        current_profit = -sys.maxsize - 1
        index = 1
        while index < len(array):
            print("##################################################3")
            print(f"Index: {index}")
            print(f"Array[index]: {array[index]}")
            print(f"Best prices before checks - buy: {current_buy}, sell: {best_sell}")

            current_profit = array[index] - current_buy

            if current_profit > best_profit:
                best_sell = array[index]
                best_profit = current_profit

            if current_buy > array[index]:
                current_buy = array[index]

            print(f"Best prices after checks - buy: {best_sell - best_profit}, sell: {best_sell}")
            index += 1

        return best_sell, best_sell - best_profit #Return a tuple with (high, low) price values