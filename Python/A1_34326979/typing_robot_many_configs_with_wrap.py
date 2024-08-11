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
    This method is for converting the characters into the index of each configuration
    """

    # use a list to store each letter's index of the user input
    in_str_index = []

    for c in input_string:
        for line in configuration:
            if c in line:
                # append the index into in_str_index as a list if charactor is found
                in_str_index.append([(configuration.index(line)) , line.index(c)])
                break
    calculate_operation(in_str_index, configuration)

def move_cursor_horizontally(left_move, right_move, col, cursor_position, position, operation):
    """
    This method is for move the cursor horizontally based on the right and left moves meanwhile store the operation
    """

    # if right moves are shorter than left OR it's close to the right border when left == right(do the 'rw' rather than 'r')
    if right_move < left_move or (right_move == left_move and cursor_position[1] > col - cursor_position[1] - 1):
        # keep moving the cursor before it's in position
        while cursor_position[1] != position[1]:
            # detact when cursor reach the border everytime cursor moves
            if cursor_position[1] == col - 1:
                operation += "rw"
                cursor_position[1] = 0
            else:
                operation += "r"
                cursor_position[1] += 1
    else:
        while cursor_position[1] != position[1]:
            if cursor_position[1] == 0:
                operation += "lw"
                cursor_position[1] = col - 1
            else:
                operation += "l"
                cursor_position[1] -= 1

    return cursor_position, operation

def move_cursor_vertically(up_move, down_move, row, cursor_position, position, operation):
    """
    This function is for move the cursor vertically based on the up and down moves meanwhile return the operation
    """

    # if up moves are shorter than down OR it's close to the top border when up == down(do the 'uw' rather than 'u')
    if up_move < down_move or (up_move == down_move and cursor_position[0] < row - cursor_position[0] - 1):
        while cursor_position[0] != position[0]:
            if cursor_position[0] == 0:
                operation += "uw"
                cursor_position[0] = row - 1
            else:
                operation += "u"
                cursor_position[0] -= 1 
    else:
        while cursor_position[0] != position[0]:
            if cursor_position[0] == row - 1:
                operation += "dw"
                cursor_position[0] = 0
            else:
                operation += "d"
                cursor_position[0] += 1

    # when moving ends check if cursor reach the destination
    if cursor_position == position:
        operation += "p"
    
    return cursor_position, operation

def calculate_operation(in_str_index, configuration):
    """
    This function is for calculate the operations in each configuration based on the indices by simulating a cursor and replace the final_operation if shorter
    """
    # use the global final_operation for the assignment latter instead of creating a local final_operation
    global final_operation

    # Initialize a cursor and set the position defaultly as [0,0]
    cursor_position = [0,0]
    # use a string to store the robot operation
    operation = ""
    col = len(configuration[0])
    row = len(configuration)
    for position in in_str_index:
        # if target position is on the right of the cursor
        if position[1] >= cursor_position[1]:
            # calculate the movements for both directions
            right_move = position[1] - cursor_position[1]
            left_move = col - right_move

            # move the cursor
            cursor_position, operation = move_cursor_horizontally(left_move, right_move, col, cursor_position, position, operation)
        # else if target is on the left of cursor
        else:
            left_move = cursor_position[1] - position[1]
            right_move = col - left_move
            cursor_position, operation = move_cursor_horizontally(left_move, right_move, col, cursor_position, position, operation)

        # After horizontal operation check if target position is below the cursor
        if position[0] >= cursor_position[0]:
            # calculate the movements for both directions
            down_move = position[0] - cursor_position[0]
            up_move = row - down_move
            cursor_position, operation = move_cursor_vertically(up_move, down_move, row, cursor_position, position, operation)
        else:
            up_move = cursor_position[0] - position[0]
            down_move = row - up_move
            cursor_position, operation = move_cursor_vertically(up_move, down_move, row, cursor_position, position, operation)

    # add the configuration index along with the corresponding operation split by ","
    operation = operation + "," + str(keyboard.index(configuration))

    # Only replace the final_operation if every charactor is found and if operation is shorter or final_operation is empty
    if operation.count("p") == len(in_str) and (len(operation) - operation.count("w") < len(final_operation) - final_operation.count("w") or final_operation == ""):
        final_operation = operation

in_str = list(input("Enter a string to type: "))

# store the shortest operation
final_operation = ""

# convert the index then calculate and store the shortest operation with all configurations
for configuration in keyboard:
    plan_the_actions(in_str, configuration)

# check whether there is any keyboard matched or not
if final_operation != "":
    print("Configuration used:")
    display_configuration(int(final_operation.split(",")[1]))
    print("The robot must perform the following operations:\n" + final_operation.split(",")[0])
else:
    print("The string cannot be typed out.")