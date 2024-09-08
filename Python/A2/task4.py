import keyword

def print_program():
    """
    Prints the entire program stored in the 'program' list.
    """
    print("Program:")
    for each_line in program:
        print(each_line)

def list_varables():
    """
    Identifies and lists variables in the program.
    
    It adds these words to a set to ensure uniqueness and prints them in sorted order.
    """
    variable_set = set()
    # Iterate over each line in the program
    for each_line in program:
        # Split each line by spaces
        line = each_line.split(" ")
        # Check each string in the line
        for each_string in line:
            # Identify potential variables based on naming conventions
            if (("_" in each_string) or (each_string.isalpha() and each_string not in keyword.kwlist)):
                variable_set.add(each_string)
    
    # Output the sorted list of identified variables
    print("Variables:")
    for each_variable in sorted(variable_set):
        print(each_variable)

# Initialize an empty list to store the program lines
program = []

# Prompt the user to input lines of Python code, ending with 'end'
print("Enter the Python program to analyze, line by line. Enter 'end' to finish.")
while True:
    line = input()
    # Stop input when the user types 'end'
    if line == "end":
        break
    else:
        # Add each line to the 'program' list
        program.append(line)

# Main menu loop to let the user choose actions
while True:
    print("==================================\nEnter your choice:\n1. Print program.\n2. List.\n0. Quit.\n==================================")
    
    try:
        # Get the user's choice
        choice = int(input())
        
        if choice == 1:
            # Option 1: Print the stored program
            print_program()
        elif choice == 2:
            # Option 2: List the variables in the program
            list_varables()
        elif choice == 0:
            # Option 0: Exit the program
            break
        else:
            # Raise an exception if the input is invalid
            raise ValueError
    except ValueError:
        # If the input is invalid (non-integer), the loop will continue
        continue