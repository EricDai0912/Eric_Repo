import keyword

def print_program():
    """
    Prints the Python program entered by the user, line by line.
    """
    print("Program:")
    for each_line in program:
        print(each_line)

def identify_variable():
    """
    Identifies potential variable names from the entered Python program.
    
    Returns:
        variable_set (set): A set containing identified variable names.
    """
    variable_set = set()  # Set to store unique variable names
    for each_line in program:
        line = each_line.split(" ")  # Split the line into words
        for each_string in line:
            # Check if the string is a potential variable
            if ("_" in each_string or each_string.isalpha()) and each_string not in keyword.kwlist:
                variable_set.add(each_string)
    return variable_set

def list_varables(variable_set):
    """
    Prints the list of variables that were identified from the Python program.

    Parameters:
        variable_set (set): The set of identified variable names.
    """
    print("Variables:")
    # Print each variable name in alphabetical order
    for each_variable in sorted(variable_set):
        print(each_variable)

def format_varable(variable_set):
    """
    Allows the user to pick a variable from the identified set, and formats it to snake_case.
    The program is updated with the new variable name.

    Parameters:
        variable_set (set): The set of identified variable names.

    Returns:
        Updated set of variable names after formatting.
    """
    while True:
        print("Pick a variable:")
        variable = input()
        if variable in variable_set:
            # Convert the selected variable to snake_case
            formated_variable = []
            for each_char in list(variable):
                if each_char.isupper():  # If a character is uppercase
                    if len(formated_variable) == 0:
                        # Convert the first uppercase character to lowercase
                        formated_variable.append(each_char.lower())
                    else:
                        # Add an underscore before subsequent uppercase letters and convert them to lowercase
                        formated_variable.append("_" + each_char.lower())
                else:
                    formated_variable.append(each_char)  # Keep lowercase characters unchanged
            # Replace the old variable name with the newly formatted variable in the program
            for each_line in program:
                line = each_line.split(" ")
                for each_string in line:
                    if variable == each_string:
                        line[line.index(variable)] = "".join(formated_variable)
                program[program.index(each_line)] = " ".join(line)
            # Re-identify the variables after updating the program
            variable_set = identify_variable()
            break
        else:
            print("This is not a variable name.")
            continue

    return variable_set

def rename_variable(variable_set):
    flag = True
    while flag:
        print("Pick a variable:")
        variable = input()
        if variable in variable_set:
            while True:
                print("Pick a new variable name:")
                new_variable_name = input()
                if new_variable_name not in variable_set:
                    for each_line in program:
                        line = each_line.split(" ")
                        for each_string in line:
                            if variable == each_string:
                                line[line.index(variable)] = new_variable_name
                        program[program.index(each_line)] = " ".join(line)
                    variable_set = identify_variable()
                    flag = False
                    break
                else:
                    print("This is already a variable name.")      
        else:
            print("This is not a variable name.")
            continue
    return variable_set

program = []  # List to store the Python program entered by the user
variable_set = set()  # Set to store identified variables

# User enters their Python program line by line
print("Enter the Python program to analyze, line by line. Enter 'end' to finish.")
while True:
    line = input()
    if line == "end":
        # Identify variables once the user finishes entering the program
        variable_set = identify_variable()
        break
    else:
        program.append(line)

# Main menu loop to allow the user to interact with their program
while True:
    print("==================================")
    print("Enter your choice:")
    print("1. Print program.")
    print("2. List.")
    print("3. Format.")
    print("4. Rename.")
    print("0. Quit.")
    print("==================================")
    choice = input()
    if choice == "1":
        print_program()
    elif choice == "2":
        list_varables(variable_set)
    elif choice == "3":
        variable_set = format_varable(variable_set)
    elif choice == "4":
        variable_set = rename_variable(variable_set)
    elif choice == "0":
        break
    else:
        # Continue if an invalid choice is made
        continue