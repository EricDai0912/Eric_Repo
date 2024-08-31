from tabulate import tabulate

def read_data(file_list):
    data_list = []
    for each_file in file_list:
        with open(each_file, "r") as f:
            data = []
            for each_line in f.readlines():
                data.append(each_line.split(","))
            data[0][-1] = data[0][-1].replace("\n", "")
            data_list.append(data)
    return data_list

def list_tables():
    table_info = []
    for table_index, each_file_data in enumerate(data_list):
        row = len(each_file_data)
        if row > 0:
            col = len(each_file_data[0])
            table_info.append([table_index, col, row])            
    header = ["Index", "Columns", "Rows"]
    print(tabulate(table_info, headers= header))
    
def display_table():
    while True:
        try:
            table_index = int(input("Choose a table index (to display):\n"))
            if table_index >= 0 and table_index < len(data_list) and data_list[table_index] != []:
                data = data_list[table_index]
                header = data[0]
                print(tabulate(data[1:], headers= header))
                break
            else:
                raise ValueError
        except ValueError:
            print("Incorrect table index. Try again.")
            continue

def duplicate_table():
    while True:
        try:
            table_index = int(input("Choose a table index (to duplicate):\n"))
            if table_index >= 0 and table_index < len(data_list) and data_list[table_index] != []:
                data_list.append(data_list[table_index])
                break
            else:
                raise ValueError
        except ValueError:
            print("Incorrect table index. Try again.")

def create_table():
    while True:
        try:
            table_index = int(input("Choose a table index (to create from):\n"))
            if table_index >= 0 and table_index < len(data_list) and data_list[table_index] != []:
                col_index_list = input("Enter the comma-separated indices of the columns to keep:\n").split(",")
                for i, each_index in enumerate(col_index_list):
                    col_index_list[i] = int(each_index)
                if max(col_index_list) < len(data_list[table_index][0]) and min(col_index_list) >= 0:
                    new_table = []
                    for each_row in data_list[table_index]:
                        new_row = []
                        for each_col_index in col_index_list:
                            new_row.append(each_row[each_col_index])
                        new_table.append(new_row)
                    data_list.append(new_table)
                    break
                else:
                    print("Incorrect column index. Try again.")
            else:
                raise ValueError
        except ValueError:
            print("Incorrect table index. Try again.")

def delete_table():
    while True:
        try:
            table_index = int(input("Choose a table index (for table deletion):\n"))
            if table_index >= 0 and table_index < len(data_list) and data_list[table_index] != []:
                trash_table[table_index] = data_list[table_index]
                data_list[table_index] = []
                break
            else:
                raise ValueError
        except ValueError:
            print("Incorrect table index. Try again.")

def delete_column():
    while True:
        try:
            table_index = int(input("Choose a table index (for column deletion):\n"))
            if table_index >= 0 and table_index < len(data_list) and data_list[table_index] != []:
                col_index = int(input("Enter the index of the column to delete:\n"))
                if col_index < len(data_list[table_index][0]) and col_index >= 0:
                    col_deleted_table = []
                    for each_row in data_list[table_index]:
                        new_row = []
                        for index, each_col in enumerate(each_row):
                            if index != col_index:
                                new_row.append(each_row[index])
                        col_deleted_table.append(new_row)
                    data_list[table_index] = col_deleted_table
                    break
                else:
                    print("Incorrect column index. Try again.")
            else:
                raise ValueError
        except ValueError:
            print("Incorrect table index. Try again.")

def restore_table():
    while True:
        try:
            table_index = int(input("Choose a table index (for restoration):\n"))
            if trash_table.get(table_index):
                data_list[table_index] = trash_table.pop(table_index)
                break
            else:
                raise ValueError
        except ValueError:
            print("Incorrect table index. Try again.")


file_list = ['grades.csv', 'class_students.csv', 'rabbytes_club_students.csv', 'rabbytes_data.csv']
data_list = read_data(file_list)
trash_table = {}
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
        break