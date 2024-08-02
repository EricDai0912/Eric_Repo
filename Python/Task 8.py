"""
This is a program that asks the user to input a string, then choose a keyboard, 
then plans the actions of Robbie the robot so that it can type this string on a keyboard.
"""
# Initialize the keyboards
keyboard_0 = ["abcdefghijklm",\
            "nopqrstuvwxyz"]
keyboard_1 = ["789",    \
            "456",  \
            "123",  \
            "0.-"]
keyboard_2 = ["chunk",  \
            "vibex",    \
            "gymps",    \
            "fjord",    \
            "waltz"]
keyboard_3 = ["bemix",  \
            "vozhd",    \
            "grypt",    \
            "clunk",    \
            "waqfs"]

# put all the configuration into one list
keyboard = [keyboard_0,keyboard_1,keyboard_2,keyboard_3]

in_str = list(input("Enter a string to type: "))
out_str_list = []

def display_configuration(i):
    """
    display the confuguration keyboard with the boarder
    """
    print("-" * (len(keyboard[i][0])+4))
    for line in keyboard[i]:
        print(f"| {line} |")
    print("-" * (len(keyboard[i][0])+4))

for configuration in keyboard:
    # use a list to store each letter's position of the user input
    in_str_loc = []
    # use a string to store the output of robot operation
    out_str = ""

    # use for loop to convert user's input into each letter's postion
    for c in in_str:
    # set a variable to store the line index
        for line in configuration:
            if c in line:
                in_str_loc.append(str(configuration.index(line)) + str(line.index(c)))
    
    # Initialize a cursor and set the position defaultly as 00
    cursor_loc = "00"
    for loc in in_str_loc:
        # if destination position is on the right of the cursor(maybe double digits)
        if int(loc[1:]) - int(cursor_loc[1:]) > 0:
            # store the go right action into the ouput string
            out_str += "r" * (int(loc[1:]) - int(cursor_loc[1:]))
            # update the current cursor postion
            cursor_loc = cursor_loc[0] + loc[1:]      
        elif int(loc[1:]) - int(cursor_loc[1:]) < 0:
            out_str += "l" * (int(cursor_loc[1:]) - int(loc[1:]))
            cursor_loc = cursor_loc[0] + loc[1:]
        # if destination position is below the cursor
        if int(loc[0]) - int(cursor_loc[0]) > 0:
            out_str += "d" * (int(loc[0]) - int(cursor_loc[0]))
            cursor_loc = loc[0] + cursor_loc[1:]  
        elif int(loc[0]) - int(cursor_loc[0]) < 0:
            out_str += "u" * (int(cursor_loc[0]) - int(loc[0]))
            cursor_loc = loc[0] + cursor_loc[1:]
        # after moving horizontally and vertically check if cursor arrive the desination
        if cursor_loc == loc:
            # append press action after cursor arrive destination
            out_str += "p"
    # append the current letter movement(out_str) into out_str_list with the configuration index split by ","
    out_str_list.append(out_str + "," + str(keyboard.index(configuration)))

# remove the empty or not matched operation by pop the element starting from the last one
for i in range(len(out_str_list)-1,-1,-1):
    if out_str_list[i].split(",")[0].count("p") != len(in_str):
        # pop out the empty opration that didn't match
        out_str_list.pop(i)

# check if there is no keyboard matched(user input is expected among all keyboards)
if len(out_str_list) > 0:
    # set the original shortest operation index as 0
    shortest_index = 0
    # find out the shorter operation and record its index of the out_str_list
    for s in out_str_list:
        if len(s) < len(out_str_list[shortest_index]):
            shortest_index = out_str_list.index(s)

    shortest_conf_index = int(out_str_list[shortest_index].split(",")[1])

    # store the final operation setps in a String
    final_operation = str(out_str_list[shortest_index].split(",")[0])

    print("Configuration used:")
    display_configuration(shortest_conf_index)
    print("The robot must perform the following operations:\n" + final_operation)
else:
    print("The string cannot be typed out.")