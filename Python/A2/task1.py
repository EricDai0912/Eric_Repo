"""
This is a program that allows a user to create and store new rabbytes. Each rabbit is identified by a unique name. The program also allows the user to enter a rabbit's age.
"""

class Rabbit:
    """
    The Rabbit class represent a rabbit with a name and an age
    """

    def __init__(self, name, age = "Unknown"):
        """
        The constructor of Class Rabbit, Initialize the Rabbit object with a name and an optional age
        """

        self.name = name
        self.age = age
 
# use a dictionary to store all the rabbit objects with its name as key
rabytes = {}

def is_name_in_dic(name):
    """
    This method check if a name is existed in the rabytes dictionary
    """

    # check if the get() return None
    if rabytes.get(name):
        return True
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
    

while True:
    choice = input("==================================\nEnter your choice:\n1. Create a Rabbit.\n2. Input Age of a Rabbit.\n3. List Rabbytes.\n0. Quit.\n==================================\n")
    if choice.isalnum():
        if int(choice) == 1:
            create_rabbit()
        elif int(choice) == 2:
            set_age()
        elif int(choice) == 3:
            list_rabbytes()
        elif int(choice) == 0:
            break
    else:
        continue