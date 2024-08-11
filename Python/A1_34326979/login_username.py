"""
This a program that asks the user to enter a username. A successful login occurs when the user enters one of the valid usernames.  
"""

# Initialize the username manually
userName_list = ["Ava", "Leo","Raj","Zoe","Max","Sam","Eli","Mia","Ian","Kim"]

# While True loop make sure program keeping asking the user for the correct username
while True:
    user = input("Enter username: ")
    
    # use in to check if username exist in the list
    if user in userName_list:
        print(f"Login successful. Welcome {user} !")
        # once match then break the loop
        break
    else:
        print("Login incorrect.")