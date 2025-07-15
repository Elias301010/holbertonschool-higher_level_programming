#!/usr/bin/python3
#!/usr/bin/python3
def element_at(my_list, idx):
    if idx < 0:
        return None
    elif idx >= len(my_list):
        return None
    return my_list[idx]
# Example usage:
my_list = [1, 2, 3, 4, 5]
print("Element at index {:d} is {}".format(3, element_at(my_list, 3)))
