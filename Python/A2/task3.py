"""
This is a program that allows a user to create and store new rabbytes. Each rabbit is identified by a unique name, allows the user to enter a rabbit's age and allows the user to specify a parent/kitten relationship also list all the cousins of a rabbit.
"""

class Rabbit:
    """
    The Rabbit class represent a rabbit with a name and an age
    """
    
    def __init__(self, name, age = "Unknown", parent = None, kitten = None):
        """
        The constructor of Class Rabbit, Initialize the Rabbit object with a name and the optional age, parenta and kitten
        """
        
        self.name = name
        self.age = age

        # It will be a shared collection if initialise with a empty set in the parameters
        if parent is not None:
            self.parent = parent
        else:
            self.parent = set()
            
        if kitten is not None:
            self.kitten = kitten
        else:
            self.kitten = set()
 
 
def is_name_in_dic(name):
    """
    This method check if a name is existed in the rabytes dictionary
    """
    
    # check if the get() return None
    if rabytes.get(name):
        return True
    else:
        return False
    
def create_rabbit():
    """
    This method is to create a Rabbit object based on the given name and store it in the dictionary
    """

    while True:
        name = input("Input the new rabbit's name:\n")
        result = is_name_in_dic(name)
        
        # create and store only if the rabbit haven't been created
        if result:
            print("That name is already in the database.")
        else:
            rabytes[name] = Rabbit(name)
            break
    
def set_age():
    """
    This method is to set the age of a rabbit
    """

    while True:
        name = input("Input the rabbit's name:\n")
        result = is_name_in_dic(name)
        if result:
            age = int(input(f"Input {name}'s age:\n"))

            # set the age of the choosen rabbit in the dictionary
            rabytes[name].age = age
            break
        else:
            print("That name is not in the database.")

def list_rabbytes():
    """
    This method is to list all the rabbits created
    """
    
    print("Rabbytes:")

    # listing all the values(rabbit objects) in the dictionary
    for rabbit in rabytes.values():
        print(f"{rabbit.name} ({rabbit.age})")

def create_parent_relationship():
    """
    This method is for create a parent relationship in both parent and kitten rabbit objects
    """

    parent_name = input("Input the parent's name:\n")

    # create a new rabbit if not exist
    if not is_name_in_dic(parent_name):
        rabytes[parent_name] = Rabbit(parent_name)

    kitten_name = input("Input the kitten's name:\n")
    if not is_name_in_dic(kitten_name):
        rabytes[kitten_name] = Rabbit(kitten_name)
    
    # store both parent and kitten info into each rabbits
    rabytes[parent_name].kitten.add(kitten_name)
    rabytes[kitten_name].parent.add(parent_name)



def list_parent_relationship():
    """
    This method is for list the parents and kittens of a rabbit
    """

    while True:
        name = input("Input the rabbit's name:\n")

        if is_name_in_dic(name):

            # list all the parents of the rabbit in alphabetical order
            print(f"Parents of {name}:")
            for each_parent in sorted(rabytes[name].parent):
                print(each_parent)

            # list all the Kittens of the rabbit in alphabetical order
            print(f"Kittens of {name}:")
            for each_kitten in sorted(rabytes[name].kitten):
                print(each_kitten)

            break
        else:
            print("That name is not in the database.")

def list_cousin_relationship():
    """
    This method is for list all the cousins of a rabbit
    """

    while True:
        name = input("Input the rabbit's name:\n")

        if is_name_in_dic(name):

            # get all the parents of the rabbit
            parent_list = rabytes[name].parent

            # store all the siblings of the parents in parent_sibling_list
            parent_sibling_list = []

            # store all the cousins in the cousin_list
            cousin_list = []

            # loop each of the parents first
            for each_parent in parent_list:

                # then finds out the grandparents
                for each_grand_parent in rabytes[each_parent].parent:

                    # finally finds out all the kittens of grandparents(parents' siblings)
                    for each_sibling in rabytes[each_grand_parent].kitten:

                        # exclude the parents of the rabbit
                        if each_sibling != each_parent:
                            parent_sibling_list.append(each_sibling)
            # loop the parents' siblings               
            for each_sibling in parent_sibling_list:

                # store every kittens of parents' siblings(cousins)
                for each_cousin in rabytes[each_sibling].kitten:
                    cousin_list.append(each_cousin)
            
            # list all the cousins in alphabetical order
            print(f"Cousins of {name}:")
            for each_cousin in sorted(cousin_list):
                print(each_cousin)

            break
        else:
            print("That name is not in the database.")
  
# use a dictionary to store all the rabbit objects with its name as key                             
rabytes = {}

while True:
    choice = input("==================================\nEnter your choice:\n1. Create a Rabbit.\n2. Input Age of a Rabbit.\n3. List Rabbytes.\n4. Create a Parental Relationship.\n5. List Direct Family of a Rabbit.\n6. Find Cousins of a Rabbit.\n0. Quit.\n==================================\n")
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
    elif choice == "6":
        list_cousin_relationship()
    elif choice == "0":
        break