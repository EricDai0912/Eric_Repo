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
                in_status = True
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
    out_str_list.append(out_str + "," + str(keyboard.index(configuration)))
for result in out_str_list:
    if result.split(",")[0] == "":
        out_str_list.pop(out_str_list.index(result))
shortest_index = 0
for s in out_str_list:
    if len(s) < len(out_str_list[shortest_index]):
        shortest_index = out_str_list.index(s)
shortest_conf_index = out_str_list[shortest_index].split(",")[1]
print("Configuration used:\n")
print("The robot must perform the following operations:\n" + str(out_str_list[shortest_index].split(",")[0]))


    # check if user input is correct
    # if in_status:
    #     print("The robot must perform the following operations:\n" + out_str)
    # else:
    #     print("The string cannot be typed out.")
    #     break