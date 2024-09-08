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
            for each_line in f.readlines():
                data.append(each_line.split(","))
            # Remove newline character from the last column of the first row
            data[0][-1] = data[0][-1].replace("\n", "")
            data_list.append(data)  # Append the data to the main list
    return data_list

def list_tables():
    """
    Lists the table information including index, number of columns, and number of rows for each table.
    """
    table_info = []
    # Collect information about each table
    for table_index, each_file_data in enumerate(data_list):
        row = len(each_file_data)
        if row > 0:
            col = len(each_file_data[0])
            table_info.append([table_index, col, row])
    header = ["Index", "Columns", "Rows"]  # Define table header
    # Print the table info using tabulate
    print(tabulate(table_info, headers=header))

def display_table():
    """
    Prompts the user to choose a table index and displays the selected table.
    """
    while True:
        try:
            table_index = int(input("Choose a table index (to display):\n"))  # Get the table index from user
            if table_index >= 0 and table_index < len(data_list) and data_list[table_index] != []:
                data = data_list[table_index]  # Select the table based on index
                header = data[0]  # Extract header row
                # Display the table using tabulate, excluding the header row from data
                print(tabulate(data[1:], headers=header))
                break
            else:
                raise ValueError  # Raise error if index is out of range or table is empty
        except ValueError:
            print("Incorrect table index. Try again.")  # Error message for invalid index
            continue  # Prompt again

def duplicate_table():
    """
    Prompts the user to choose a table index and duplicates the selected table.
    """
    while True:
        try:
            table_index = int(input("Choose a table index (to duplicate):\n"))  # Get the table index from user
            if table_index >= 0 and table_index < len(data_list) and data_list[table_index] != []:
                data_list.append(data_list[table_index])  # Duplicate the selected table
                break
            else:
                raise ValueError  # Raise error if index is out of range or table is empty
        except ValueError:
            print("Incorrect table index. Try again.")  # Error message for invalid index

def create_table():
    """
    Prompts the user to choose a table index and create a new table from selected columns of the chosen table.
    """
    while True:
        try:
            table_index = int(input("Choose a table index (to create from):\n"))  # Get the table index from user
            if table_index >= 0 and table_index < len(data_list) and data_list[table_index] != []:
                col_index_list = input("Enter the comma-separated indices of the columns to keep:\n").split(",")
                # Convert column indices from strings to integers
                for i, each_index in enumerate(col_index_list):
                    col_index_list[i] = int(each_index)
                # Check if column indices are within valid range
                if max(col_index_list) < len(data_list[table_index][0]) and min(col_index_list) >= 0:
                    new_table = []
                    # Create new table with selected columns
                    for each_row in data_list[table_index]:
                        new_row = []
                        for each_col_index in col_index_list:
                            new_row.append(each_row[each_col_index])
                        new_table.append(new_row)
                    data_list.append(new_table)  # Append the new table to the data list
                    break
                else:
                    print("Incorrect column index. Try again.")  # Error message for invalid column indices
            else:
                raise ValueError  # Raise error if index is out of range or table is empty
        except ValueError:
            print("Incorrect table index. Try again.")  # Error message for invalid index

def delete_table():
    """
    Prompts the user to choose a table index and deletes the selected table from the data list.
    """
    while True:
        try:
            table_index = int(input("Choose a table index (for table deletion):\n"))  # Get the table index from user
            if table_index >= 0 and table_index < len(data_list) and data_list[table_index] != []:
                trash_table[table_index] = data_list[table_index]  # Save the table to trash before deletion
                data_list[table_index] = []  # Clear the selected table
                break
            else:
                raise ValueError  # Raise error if index is out of range or table is empty
        except ValueError:
            print("Incorrect table index. Try again.")  # Error message for invalid index

def delete_column():
    """
    Prompts the user to choose a table index and delete a specific column from the selected table.
    """
    while True:
        try:
            table_index = int(input("Choose a table index (for column deletion):\n"))  # Get the table index from user
            if table_index >= 0 and table_index < len(data_list) and data_list[table_index] != []:
                col_index = int(input("Enter the index of the column to delete:\n"))  # Get the column index from user
                if col_index < len(data_list[table_index][0]) and col_index >= 0:
                    col_deleted_table = []
                    # Create a new table with the specified column removed
                    for each_row in data_list[table_index]:
                        new_row = []
                        for index, each_col in enumerate(each_row):
                            if index != col_index:
                                new_row.append(each_row[index])
                        col_deleted_table.append(new_row)
                    data_list[table_index] = col_deleted_table  # Update the table with the column removed
                    break
                else:
                    print("Incorrect column index. Try again.")  # Error message for invalid column index
            else:
                raise ValueError  # Raise error if index is out of range or table is empty
        except ValueError:
            print("Incorrect table index. Try again.")  # Error message for invalid index

def restore_table():
    """
    Prompts the user to choose a table index and restores the previously deleted table from the trash.
    """
    while True:
        try:
            table_index = int(input("Choose a table index (for restoration):\n"))  # Get the table index from user
            if table_index in trash_table:
                data_list[table_index] = trash_table.pop(table_index)  # Restore the table from trash
                break
            else:
                raise ValueError  # Raise error if index is not in trash
        except ValueError:
            print("Incorrect table index. Try again.")  # Error message for invalid index

# List of file paths to read data from
file_list = ['grades.csv', 'class_students.csv', 'rabbytes_club_students.csv', 'rabbytes_data.csv']
data_list = read_data(file_list)  # Read data from the files
trash_table = {}  # Dictionary to hold deleted tables

# Main menu loop to interact with the user
while True:
    choice = input("==================================\n\
Enter your choice:\n\
1. List tables.\n\
2. Display table.\n\
3. Duplicate table.\n\
4. Create table.\n\
5. Delete table.\n\
6. Delete column.\n\
7. Restore table.\n\
0. Quit.\n\
==================================\n")
    
    # Perform actions based on user's choice
    if choice == "1":
        list_tables()
    elif choice == "2":
        display_table() 
    elif choice == "3":
        duplicate_table()
    elif choice == "4":
        create_table()
    elif choice == "5":
        delete_table()
    elif choice == "6":
        delete_column() 
    elif choice == "7":
        restore_table() 
    elif choice == "0":
        break  # Exit the loop and end the program