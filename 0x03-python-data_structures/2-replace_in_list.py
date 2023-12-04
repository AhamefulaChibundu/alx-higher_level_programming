#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    my_list_last_index = len(my_list) - 1

    if idx < 0 or idx > my_list_last_index:
        pass
    else:
        my_list[idx] = element
    return my_list
