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

def display_configuration(i):
    """
    display the confuguration keyboard with the boarder
    """
    print("-" * (len(keyboard[i][0])+4))
    for line in keyboard[i]:
        print(f"| {line} |")
    print("-" * (len(keyboard[i][0])+4))

def  plan_the_actions(input_string, configuration):
    """
    This function is for converting the characters into the index of each configuration
    """

    # use a list to store each letter's index of the user input
    in_str_index = []

    for c in input_string:
        for line in configuration:
            if c in line:
                # append the index into in_str_index if charactor is found
                in_str_index.append(str(configuration.index(line)) + str(line.index(c)))
                break
    calculate_operation(in_str_index, configuration)

def calculate_operation(in_str_index, configuration):
    """
    This function is for calculate the operations in each configuration based on the indices
    by simulating a cursor and replace the final_operation if shorter
    """
    # use the global final_operation for the change of value
    global final_operation
    # Initialize a cursor and set the position defaultly as 00
    cursor_position = "00"
    # use a string to store the output of robot operation
    operation = ""
    for position in in_str_index:
        # if destination position is on the right of the cursor(maybe double digits)
        if int(position[1:]) - int(cursor_position[1:]) > 0:
            # store the go right action into the ouput string
            operation += "r" * (int(position[1:]) - int(cursor_position[1:]))
            # update the current cursor postion
            cursor_position = cursor_position[0] + position[1:]      
        elif int(position[1:]) - int(cursor_position[1:]) < 0:
            operation += "l" * (int(cursor_position[1:]) - int(position[1:]))
            cursor_position = cursor_position[0] + position[1:]
        # if destination position is below the cursor
        if int(position[0]) - int(cursor_position[0]) > 0:
            operation += "d" * (int(position[0]) - int(cursor_position[0]))
            cursor_position = position[0] + cursor_position[1:]  
        elif int(position[0]) - int(cursor_position[0]) < 0:
            operation += "u" * (int(cursor_position[0]) - int(position[0]))
            cursor_position = position[0] + cursor_position[1:]
        # after moving horizontally and vertically check if cursor arrive the desination
        if cursor_position == position:
            # append press action after cursor arrive destination
            operation += "p"
    # add the configuration into operation to compare the len for the shortes one
    operation = operation + "," + str(keyboard.index(configuration))
    # replace the final_operation if every charactor is found and if operation is shorter or final_operation is empty
    if operation.count("p") == len(in_str) and (len(operation) < len(final_operation) or final_operation == ""):
        # store the belong configuration into the final_operation split by ","
        final_operation = operation
        print("final:" + final_operation)

in_str = list(input("Enter a string to type: "))

# store the operation of each configuration into a list
final_operation = ""

# convert the index then calculate and store the operation in each configuration
for configuration in keyboard:
    plan_the_actions(in_str, configuration)

# check if there is no keyboard matched(user input is expected among all keyboards)
if final_operation != "":
    # # set the original shortest operation index as 0
    # shortest_index = 0
    # # find out the shorter operation and record its index of the operation_list
    # for s in operation_list:
    #     if len(s) < len(operation_list[shortest_index]):
    #         shortest_index = operation_list.index(s)

    # shortest_conf_index = int(operation_list[shortest_index].split(",")[1])

    # # store the final operation setps in a String
    # final_operation = str(operation_list[shortest_index].split(",")[0])
    print("Configuration used:")
    display_configuration(int(final_operation.split(",")[1]))
    print("The robot must perform the following operations:\n" + final_operation.split(",")[0])
else:
    print("The string cannot be typed out.")