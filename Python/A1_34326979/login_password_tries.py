"""
This is a program that asks the user to enter a valid username and a valid password. 
A successful login occurs when the user enters one of the correct usernames and one of the correct passwords. 
If, after 3 tries, the user did not provide a correct login, the program terminates.  
"""

# Initialize the username and password manually
userName_list = ["Ava", "Leo","Raj","Zoe","Max","Sam","Eli","Mia","Ian","Kim"]
pass_list = ["12345","abcde","pass1","qwert","aaaaa","zzzzz","11111","apple","hello","admin"]

# set the for loop to 3 times
for i in range(3):
    user = input("Enter username: ")
    passwd = input("Enter password: ")
    # use in to check if username and password both exist in the list
    if user in userName_list and passwd in pass_list:
        print(f"Login successful. Welcome {user} !")
        # once match then break the loop
        break
    else:
        print(f"Login incorrect. Tries left: {2-i}")