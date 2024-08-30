import keyword

def print_program():
    print("Program:")
    for each_line in program:
        print(each_line)

def identify_variable():
    variable_set = set()
    for each_line in program:
        line = each_line.split(" ")
        for each_string in line:
            if ("_" in each_string or each_string.isalpha()) and each_string not in keyword.kwlist:
                variable_set.add(each_string)
    return variable_set

def list_varables(variable_set):
    print("Variables:")
    for each_variable in sorted(variable_set):
        print(each_variable)

def format_varable(variable_set):
    while True:
        print("Pick a variable:")
        variable = input()
        if variable in variable_set:
            formated_variable = list(variable)
            for each_char in formated_variable:
                if each_char.isupper():
                    if formated_variable.index(each_char) != 0:
                        formated_variable[formated_variable.index(each_char)] = "_" + each_char.lower()
                    else:
                        formated_variable[formated_variable.index(each_char)] = each_char.lower()
            formated_variable = "".join(formated_variable)
            for each_line in program:
                line = each_line.split(" ")
                for each_string in line:
                    if variable == each_string:
                        line[line.index(variable)] = formated_variable
                program[program.index(each_line)] = " ".join(line)
            variable_set = identify_variable()
            break
        else:
            print("This is not a variable name.")
            continue

    return variable_set


program = []
variable_set = set()
print("Enter the Python program to analyze, line by line. Enter 'end' to finish.")
while True:
    line = input()
    if line == "end":
        variable_set = identify_variable()
        break
    else:
        program.append(line)
while True:
    print("==================================\nEnter your choice:\n1. Print program.\n2. List.\n3. Format.\n0. Quit.\n==================================")
    choice = input()
    if choice == "1":
        print_program()
    elif choice == "2":
        list_varables(variable_set)
    elif choice == "3":
        variable_set = format_varable(variable_set)
    elif choice == "0":
        break
    else:
        continue