#!/usr/bin/env python3

from i_o import doStuff
file = doStuff()

console = [["1", "2", "3"],             # [0][n]
            ["4", "5", "6"],            # [1][n]
            ["7", "8", "9"],            # [2][n]
            ["*", "0", "#"]]            # [3][n]

flattened_console = [["3", "6", "9", "#"],    # [0][n]
                    ["2", "5", "8", "0"],   # [1][n]
                    ["1", "4", "7", "*"]]   # [2][n]

def numberCheck() -> 'str':
    # Just a little extra effort to catch human input errors
    check_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']     # Since 0-9 are the only choices in a 900#

    while True:
        try:
            my_number = input("Please enter the last 6 digits of your 900#: ")
            for i in my_number:
                if i in check_list and len(my_number) == 6: # Have to make sure each num is in the list of exceptable nums AND is 6 digits long
                    return my_number
                else:
                    print("")
                    print("Invalid entry. Please enter a valid last 6 digits of your 900#: ")
                    print("")
                    break
        except:
            continue

def nameCheck() -> 'str':
    # This is extra credit right??? XD
    while True:
        try:
            my_name = input("Enter username and press enter: ").lower() # Store Agent name
            # To allow mistakes in capitalization
            my_name = my_name[0:1].upper() + my_name[1:len(my_name)-1] + my_name[len(my_name)-1:len(my_name)].upper()

            for i in file:  # Check if 'my_name' is inside the imported list of lists
                if my_name in i[0]:
                    return my_name
                else:
                    continue
            print("")   # If 'my_name' isn't inside the list, this line executes, followed by circling back to the input above
            print("Invalid entry. Enter username and press enter: ")
            print("")
        except:
            continue

def findAgent(my_name:'str') -> 'list':
    # This function fetches the codes associated with the agent name given 'nameCheck()' passes
    agent_codes = []
    for i in file:
        if my_name in i[0]:
            agent_codes.append(i[1])
            return agent_codes
        else:
            continue

def reduceCodes(agent_codes:'list') -> 'list':
    # break the list of lists of codes up into code0, code1, code2, etc
    code0 = []
    code1 = []
    code2 = []
    code3 = []
    code4 = []
    code5 = []
    code6 = []
    code7 = []
    code8 = []
    code9 = []
    for i in agent_codes:   # Appending each set of codes to its own list after locating the agent's set of codes
        code0.append(i[0][1])
        code1.append(i[1][1])
        code2.append(i[2][1])
        code3.append(i[3][1])
        code4.append(i[4][1])
        code5.append(i[5][1])
        code6.append(i[6][1])
        code7.append(i[7][1])
        code8.append(i[8][1])
        code9.append(i[9][1])
    return code0, code1, code2, code3, code4, code5, code6, code7, code8, code9

def splitSixDigits(my_number:'str') -> 'str':
    # split up the 6 digits of the 900 number into 6 different variables
    a,b,c,d,e,f = my_number[0], my_number[1], my_number[2], my_number[3], my_number[4], my_number[5]
    return a,b,c,d,e,f

def getArrowNum(f_code:'list') -> 'int':
    # Do a .count() on each arrow type for each set of codes
    for i in f_code:
        num_of_left = i.count("<")
        num_of_right = i.count(">")
        num_of_up = i.count("^")
        num_of_down = i.count("v")
        return num_of_down, num_of_left, num_of_right, num_of_up

def doTheComplexStuff(agent_codes:'list', my_number:'str') -> 'list':
    # Here's where the meat and potatos are served, ie the complex stuff
    final_list = [] # empty list to store the final values after all arrows = 0
    code_list = []  # empty list to store the agent's 9 codes available
    test_list = []  # empty list to store the agent's 6 digit 900#
    
    c0, c1, c2, c3, c4, c5, c6, c7, c8, c9 = reduceCodes(agent_codes)   # unpacking codes into variables
    for i in c0, c1, c2, c3, c4, c5, c6, c7, c8, c9:    # putting the codes back together into a single list
        code_list.append(i)

    a,b,c,d,e,f = splitSixDigits(my_number) # unpacking 900 number into variables

    for i in a,b,c,d,e,f:
        test_list.append(i)

    k = 0
    for i in test_list:
        f_code = code_list[int(i)]
        num_of_down, num_of_left, num_of_right, num_of_up = getArrowNum(f_code) # unpacking num of arrows given each 900# input

        for j, k in enumerate(console): # singling out which list inside the list your number is located for <, > directions
            if i in k:
                first = rightArrow(num_of_right, i, j)  # i is the starting value given each number input
                second = leftArrow(num_of_left, first, j)   # first is the starting value given where i landed
                break
            else:
                continue

        for x, y in enumerate(flattened_console):   # console flipped on its side to simulate up and down, using left and right
            if second in y:
                third = downArrow(num_of_down, second, x)   # second is the starting value given where first landed
                fourth = upArrow(num_of_up, third, x)   # third is the starting value given where second landed
                final_list.append(fourth)   # Final point where each set of arrows will ultimately land
                break
            else:
                continue

    return final_list
            
def rightArrow(num_of_right:'int', number_entered:'str', j:'int') -> 'str':
    # Takes number of > and iterates till > = 0
    lst = console[j]
    i = lst.index(number_entered)
    while num_of_right > 0:
        while i < len(lst):
            num_of_right -= 1
            i += 1
            if i == len(lst):
                i = 0 # force restart
            if num_of_right == 0:
                break

    return lst[i]

def leftArrow(num_of_left:'int', first:'str', j:'int') -> 'str':
    # Takes number of < and iterates till < = 0
    lst = console[j]
    i = lst.index(first)
    
    if i == 2:  # Have to swap the index since I'm reversing the list below
        i = 0
    elif i == 0:
        i = 2
    else:
        i = 1
    
    r_lst = lst[::-1]   # Here's where I reverse the list
   
    while num_of_left > 0:
        while i < len(r_lst):

            num_of_left -= 1
            i += 1
            if i == len(r_lst):
                i = 0
            if num_of_left == 0:
                break

    return r_lst[i]

def downArrow(num_of_down:'int', second:'str', x:'int') -> 'str':
    # Takes number of down arrows and iterates right till down = 0
    lst = flattened_console[x]
    i = lst.index(second)
    while num_of_down > 0:
        while i < len(lst):

            num_of_down -= 1
            i += 1
            if i == len(lst):
                i = 0 # force restart
            if num_of_down == 0:
                break

    return lst[i]

def upArrow(num_of_up:'int', third:'str', x:'int') -> 'str':
    # flip list, iterates again till up arrows = 0
    lst = flattened_console[x]
    i = lst.index(third)
    
    if i == 0:  # Have to swap the index since I'm reversing the list below
        i = 3
    elif i == 1:
        i = 2
    elif i == 2:
        i = 1
    else:
        i = 0
    
    r_lst = lst[::-1]   # Reverse the list since we're going up (iterating left)
    
    while num_of_up > 0:
        while i < len(r_lst):

            num_of_up -=1
            i += 1
            if i == len(r_lst):
                i = 0
            if num_of_up == 0:
                break

    return r_lst[i]

def bitwiseStuff(my_number:'str', dec_codes:'str') -> 'int':
    # Unpack the string into individual variables
    # Changing each variable into ASCII
    d1, d2, d3, d4, d5, d6 = ord(dec_codes[0]), ord(dec_codes[1]), ord(dec_codes[2]), ord(dec_codes[3]), ord(dec_codes[4]), ord(dec_codes[5])
    n1, n2, n3, n4, n5, n6 = ord(my_number[0]), ord(my_number[1]), ord(my_number[2]), ord(my_number[3]), ord(my_number[4]), ord(my_number[5])

    # Top left
    a = n2 & d3     # AND
    b = d1 ^ a      # XOR

    # Bottom left
    c = n4 | d5     # OR
    d = ~(c & n6)   # NAND
    e = b & d       # Ending left

    # Top Right
    f = d2 & n3
    g = n1 ^ f

    # Bottom Right
    h = d4 | n5
    i = ~(h & d6)
    j = g & i       # Ening Right

    final = e | j   # Ending Center

    return final

def main() -> None:
    print("")
    print("Please enter your first name and last initial with no spaces.")
    print("For example: JohnathonM")
    print("")
    my_name = nameCheck()   # Agent name
    agent_codes = findAgent(my_name)
    print("")
    my_number = numberCheck()   # Agent 900#
    print("")
    dec_codes = doTheComplexStuff(agent_codes, my_number)
    print(f"Agent {my_name} your 6 digit code is: ")
    print(dec_codes)
    print("*" * 30)
    print("")
    binary_code = bitwiseStuff(my_number, dec_codes)
    print(f"Set the switches with the following code: {binary_code:08b}")   # Final ASCII into binary, stripping 0b, making sure 8bit
    print("")


if __name__ == "__main__":
    main()
