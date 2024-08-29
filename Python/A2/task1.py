class Rabbit:
 
    def __init__(self, name, age = "Unknown"):
            self.name = name
            self.age = age
 
if __name__ == "__main__":
 
    rabytes = []
 
    def is_name_in_list(name):
        for rabbit in rabytes:
            if rabbit.name == name:
                return True
        return False
    
    def create_rabbit():
        while True:
            name = input("Input the new rabbit's name:\n")
            result = is_name_in_list(name)
            if result:
                print("That name is already in the database.")
            else:
                rabytes.append(Rabbit(name))
                break
    
    def set_age():
        while True:
            name = input("Input the rabbit's name:\n")
            result = is_name_in_list(name)
            if result:
                age = int(input(f"Input {name}'s age:\n"))
                for rabbit in rabytes:
                    if rabbit.name == name:
                        rabbit.age = age
                break
            else:
                print("That name is not in the database.")
    
    def list_rabbytes():
        print("Rabbytes:")
        for rabbit in rabytes:
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