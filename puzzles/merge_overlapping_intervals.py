class Pair:
    def __init__(self, first, second):
        self.first = first
        self.second = second

    def __repr__(self):
        return f"Pair({self.first}, {self.second})"

    def __eq__(self, other):
        if self.first == other.first and self.second == other.second:
            return True
        else:
            return False


def merge_intervals(v):
    result = []
    length = len(v)
    if length > 0:
        v_index = 1
        lower_bound = v[0].first
        upper_bound = v[0].second
        while v_index < length:
            next_pair = v[v_index]
            if next_pair.first <= upper_bound < next_pair.second:
                upper_bound = next_pair.second
            else:
                result.append(Pair(lower_bound, upper_bound))
                lower_bound = next_pair.first
                upper_bound = next_pair.second
            v_index += 1

        result.append(Pair(lower_bound, upper_bound))

    return result
