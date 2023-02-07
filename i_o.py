#!/usr/bin/env python3

def doStuff() -> 'list':
    from itertools import groupby # in order to create a list separating at an empty newline
    
    with open('codes.txt', 'r') as codes: # duh
        lines = codes.read()
        lines = lines.strip().split('\n')


    line = [list(sub) for e, sub in groupby(lines, key = bool) if e] # my function using the itertools lib

    new_list = [] # to store all the names for referencing later
    new_list_two = [] # to store the list of codes


    for i in line:
        if len(i) == 3: # because only the lists with 3 elements have names, hence codes start at index 1
            new_list.append(i[0])
            new_list_two.append(i[1:])
        else:
            new_list_two.append(i)

    # because theres a list of 10 codes per person...
    # I had to separate the codes by 10s into a new list
    new_list_three = [new_list_two[i:i+10] for i in range(0, len(new_list_two), 10)]

    # zipping the two lists together, name to a list of 10 codes...
    # shoulda just used a dictionary... but here we are
    final_list = [list(zipped) for zipped in zip(new_list, new_list_three)]

    return final_list

# doStuff()
if __name__ == "__main__":
    lst = doStuff()
    print(lst)