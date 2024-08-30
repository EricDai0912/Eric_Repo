from tabulate import tabulate

def read_data(file_list):
    data_list = []
    for each_file in file_list:
        with open(each_file, "r") as f:
            data = []
            for i, each_line in enumerate(f.readlines()):
                data.append(each_line.split(","))
            data[0][-1] = data[0][-1].replace("\n", "")
            data_list.append(data)
    return data_list

def list_tables(data_list):
    table_info = []
    for index, each_file_data in enumerate(data_list):
        col = len(each_file_data[0])
        row = len(each_file_data)
        table_info.append([index, col, row])
    header = ["Index", "Columns", "Rows"]
    print(tabulate(table_info, headers= header))
    
def display_table():
    while True:
        try:
            index = int(input("Choose a table index (to display):\n"))
            if index >= 0 and index < len(data_list):
                data = data_list[index]
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
            index = int(input("Choose a table index (to duplicate):\n"))
            if index >= 0 and index < len(data_list):
                data_list.append(data_list[index])
                break
            else:
                raise ValueError
        except ValueError:
            print("Incorrect table index. Try again.")

def create_table():
    while True:
        try:
            table_index = int(input("Choose a table index (to create from):\n"))
            if table_index >= 0 and table_index < len(data_list):
                new_table = [data_list[table_index][0]]
                col_index_list = input("Enter the comma-separated indices of the columns to keep:").split(",")
                for each_col_inedx in col_index_list:
                    new_table.append(data_list[table_index][each_col_inedx])
                data_list.append(new_table)
                break
            else:
                raise ValueError
        except ValueError:
            print("Incorrect table index. Try again.")

file_list = ['grades.csv', 'class_students.csv', 'rabbytes_club_students.csv', 'rabbytes_data.csv']
data_list = read_data(file_list)
while True:
    choice = input("==================================\n\
Enter your choice:\n\
1. List tables.\n\
2. Display table.\n\
3. Duplicate table.\n\
4. Create table.\n\
5. Delete table.\n\
0. Quit.\n\
==================================\n")
    if choice == "1":
        list_tables(data_list)
    elif choice == "2":
        display_table()
    elif choice == "3":
        duplicate_table()
    elif choice == "4":
        create_table()
    # elif choice == "5":
    #     delete_table()
    elif choice == "0":
        break