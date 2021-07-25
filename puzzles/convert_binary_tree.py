class Element:
    def __init__(self, value, left_node, right_node):
        self.value = value
        self.l = left_node
        self.r = right_node

    def __repr__(self):
        return f"Element({self.value}, {self.l}, {self.r})"

    # Overriding eq operator so that tests can correctly compare objects
    def __eq__(self, other):
        if self.value == other.value and self.r == other.r and self.l == other.l:
            return True
        else:
            return False


def convert_to_linked_list(root: Element):
    result = []

    if root is None:
        return []
    else:
        print("###############################################")
        print(f"Checking tree element: {root}")

        left_list = convert_to_linked_list(root.l)
        previous_value = get_list_element_value(left_list, -1)
        right_list = convert_to_linked_list(root.r)
        next_value = get_list_element_value(right_list, 0)

        update_last_list_pointer(left_list, root.value)
        update_first_list_pointer(right_list, root.value)
        print(f"Left list: {left_list}")
        print(f"This element: {Element(root.value, previous_value, next_value)}")
        print(f"Right list: {right_list}")
        print("###############################################")
        result += left_list
        result.append(Element(root.value, previous_value, next_value))
        result += right_list

    return result


def get_element_value(e: Element):
    if e is None:
        return None
    else:
        return e.value


def get_list_element_value(l: [Element], index: int):
    if (index >= 0 and index >= len(l)) or (index < 0 and abs(index) > len(l)):
        return None
    else:
        return get_element_value(l[index])


def update_last_list_pointer(l: [Element], new_value: int):
    if len(l) > 0:
        print(f"Updating {l[len(l) - 1]}'s r pointer to: {new_value}")
        l[len(l) - 1].r = new_value


def update_first_list_pointer(l: [Element], new_value: int):
    if len(l) > 0:
        print(f"Updating {l[0]}'s l pointer to: {new_value}")
        l[0].l = new_value
