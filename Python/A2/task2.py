class Rabbit:
 
    def __init__(self, name, age = "Unknown", parent = None, kitten = None):
            self.name = name
            self.age = age
            if parent is not None:
                self.parent = parent
            else:
                self.parent = set()
            if kitten is not None:
                self.kitten = kitten
            else:
                self.kitten = set()
 
 
def is_name_in_dic(name):
    result = rabytes.get(name)
    if result:
        return True
    else:
        return False
    
def create_rabbit():
    while True:
        name = input("Input the new rabbit's name:\n")
        result = is_name_in_dic(name)
        if result:
            print("That name is already in the database.")
        else:
            rabytes[name] = Rabbit(name)
            break
    
def set_age():
    while True:
        name = input("Input the rabbit's name:\n")
        result = is_name_in_dic(name)
        if result:
            age = int(input(f"Input {name}'s age:\n"))
            rabytes[name].age = age
            break
        else:
            print("That name is not in the database.")

def list_rabbytes():
    print("Rabbytes:")
    for rabbit in rabytes.values():
        print(f"{rabbit.name} ({rabbit.age})")

def create_parent_relationship():
    parent_name = input("Input the parent's name:\n")
    if not is_name_in_dic(parent_name):
        rabytes[parent_name] = Rabbit(parent_name)
    kitten_name = input("Input the kitten's name:\n")
    if not is_name_in_dic(kitten_name):
        rabytes[kitten_name] = Rabbit(kitten_name)
    rabytes[parent_name].kitten.add(kitten_name)
    rabytes[kitten_name].parent.add(parent_name)



def list_parent_relationship():
    while True:
        name = input("Input the rabbit's name:\n")
        if is_name_in_dic(name):
            print(f"Parents of {name}:")
            for each_parent in sorted(rabytes[name].parent):
                print(each_parent)
            print(f"Kittens of {name}:")
            for each_kitten in sorted(rabytes[name].kitten):
                print(each_kitten)
            break
        else:
            print("That name is not in the database.")
                            
rabytes = {}

while True:
    choice = input("==================================\nEnter your choice:\n1. Create a Rabbit.\n2. Input Age of a Rabbit.\n3. List Rabbytes.\n4. Create a Parental Relationship.\n5. List Direct Family of a Rabbit.\n0. Quit.\n==================================\n")
    if choice == "1":
        create_rabbit()
    elif choice == "2":
        set_age()
    elif choice == "3":
        list_rabbytes()
    elif choice == "4":
        create_parent_relationship()
    elif choice == "5":
        list_parent_relationship()
    elif choice == "0":
        break
    else:
        continue