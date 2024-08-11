"""
This is program that asks the user to input a string, and then plans the actions of 
Robbie the robot so that it can type this string on a keyboard.
"""
# Initialize the keyboard
keyboard = ["abcdefghijklm",\
            "nopqrstuvwxyz"]
in_str = list(input("Enter a string to type: "))

# set a boolean variable defaultly as Ture for checking the user input status
in_status = True

# use a list to store each letter's position of the user input
in_str_loc = []

# use a string to store the output of robot operation
out_str = ""

# use for loop to convert user's input into each letter's postion
for c in in_str:

    # set a variable to store the line index
    line_index = None

    for line in keyboard:
        if c in line:
            line_index = keyboard.index(line)
            in_str_loc.append(str(line_index) + str(line.index(c)))

    # if it cannot be found in any line
    if line_index == None:
        # record there is a wrong input by setting False
        in_status = False

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

# check if user input is correct
if in_status:
    print("The robot must perform the following operations:\n" + out_str)
else:
    print("The string cannot be typed out.")