#!/usr/bin/python3

#Fxn that returns element of a list at a particular index[idx]

def element_at(my_list, idx):
    for i in my_list:
        if idx < 0:
            return None
        elif idx > len(my_list) - 1:
            return None
        else:
            return my_list[idx]

