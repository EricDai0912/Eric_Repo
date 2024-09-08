from tabulate import tabulate

def read_data(file_list):
    """
    Reads data from a list of CSV files and returns a list of data tables.

    Parameters:
        file_list (list of str): A list of file paths to CSV files.

    Returns:
        data_list (list of list of lists): A list where each element is a list representing
                                           the data from one file, split into rows and columns.
    """
    data_list = []  # Initialize an empty list to store data from all files
    for each_file in file_list:
        with open(each_file, "r") as f:
            data = []
            # Read each line from the file and split by comma
            for i, each_line in enumerate(f.readlines()):
                data.append(each_line.split(","))
            # Remove newline character from the last column of the first row
            data[0][-1] = data[0][-1].replace("\n", "")
            data_list.append(data)  # Append the data to the main list
    return data_list

def list_tables(data_list):
    """
    Lists the table information including index, number of columns, and number of rows for each table.

    Parameters:
        data_list (list of list of lists): The list of data tables.
    """
    table_info = []
    # Collect information about each table
    for index, each_file_data in enumerate(data_list):
        col = len(each_file_data[0])  # Number of columns in the table
        row = len(each_file_data)  # Number of rows in the table
        table_info.append([index, col, row])  # Append table info to the list
    header = ["Index", "Columns", "Rows"]  # Define table header
    # Print the table info using tabulate
    print(tabulate(table_info, headers=header))

def display_table():
    """
    Prompts the user to choose a table index and displays the selected table.
    """
    while True:
        try:
            index = int(input("Choose a table index (to display):\n"))  # Get the table index from user
            if index >= 0 and index < len(data_list):
                data = data_list[index]  # Select the table based on index
                header = data[0]  # Extract header row
                # Display the table using tabulate, excluding the header row from data
                print(tabulate(data[1:], headers=header))
                break
            else:
                raise ValueError  # Raise error if index is out of range
        except ValueError:
            print("Incorrect table index. Try again.")  # Error message for invalid index
            continue  # Prompt again

def duplicate_table():
    """
    Prompts the user to choose a table index and duplicates the selected table.
    """
    while True:
        try:
            index = int(input("Choose a table index (to duplicate):\n"))  # Get the table index from user
            if index >= 0 and index < len(data_list):
                data_list.append(data_list[index])  # Duplicate the selected table
                break
            else:
                raise ValueError  # Raise error if index is out of range
        except ValueError:
            print("Incorrect table index. Try again.")  # Error message for invalid index

# List of file paths to read data from
file_list = ['grades.csv', 'class_students.csv', 'rabbytes_club_students.csv', 'rabbytes_data.csv']
data_list = read_data(file_list)  # Read data from the files

while True:
    # Display menu and get user choice
    choice = input("==================================\n\
Enter your choice:\n\
1. List tables.\n\
2. Display table.\n\
3. Duplicate table.\n\
0. Quit.\n\
==================================\n")
    
    # Perform actions based on user's choice
    if choice == "1":
        list_tables(data_list) 
    elif choice == "2":
        display_table() 
    elif choice == "3":
        duplicate_table() 
    elif choice == "0":
        break  # Exit the loop and end the program