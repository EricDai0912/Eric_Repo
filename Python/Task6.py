"""
This program asks the users to login with username and paired password.
After 3 unsuccessful tries, the user is asked to confirm that they are not a robot so they can try to log in again.
"""

# Initialize the paired login information using lists inside the list
login_list = [["Ava","12345"],["Leo","abcde"],["Raj","pass1"],["Zoe","qwert"], \
["Max","aaaaa"],["Sam","zzzzz"],["Eli","11111"],["Mia","apple"],["Ian","hello"],["Kim","admin"]]

# set a boolean variable terminal defalutly as false so we can break the while loop by set this to True later
enter_correct = True
while enter_correct:
    username = input("Enter username: ")
    password = input("Enter password: ")

    user_enter = [username,password]

    

