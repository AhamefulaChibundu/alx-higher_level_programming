#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    temp_val = 0
    div = []
    for m in range(list_length):
        try:
            temp_val = my_list_1[m] / my_list_2[m]
        except TypeError:
            temp_val = 0
            print("wrong type")
        except ZeroDivisionError:
            temp_val  = 0
            print("division by 0")
        except IndexError:
            temp_val = 0
            print("out of range")
        finally:
            pass
        div.append(temp_val)
    return div
