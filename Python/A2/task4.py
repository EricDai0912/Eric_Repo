import keyword

def print_program():
    print("Program:")
    for each_line in program:
        print(each_line)

def list_varables():
    variable_set = set()
    for each_line in program:
        line = each_line.split(" ")
        for each_string in line:
            if (("_" in each_string) or (each_string.isalpha() and each_string not in keyword.kwlist)):
                variable_set.add(each_string)
    print("Variables:")
    for each_variable in sorted(variable_set):
        print(each_variable)

program = []
print("Enter the Python program to analyze, line by line. Enter 'end' to finish.")
while True:
    line = input()
    if line == "end":
        break
    else:
        program.append(line)
while True:
    print("==================================\nEnter your choice:\n1. Print program.\n2. List.\n0. Quit.\n==================================")
    choice = input()
    if choice == "1":
        print_program()
    elif choice == "2":
        list_varables()
    elif choice == "0":
        break
    else:
        continue