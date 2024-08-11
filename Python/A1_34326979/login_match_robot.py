"""
This program asks the users to login with username and paired password.
After 3 unsuccessful tries, the user is asked to confirm that they are not a robot so they can try to log in again.
"""

# Initialize the paired login information using lists inside the list
login_list = [["Ava","12345"],["Leo","abcde"],["Raj","pass1"],["Zoe","qwert"], \
["Max","aaaaa"],["Sam","zzzzz"],["Eli","11111"],["Mia","apple"],["Ian","hello"],["Kim","admin"]]

# set a boolean variable terminal defalutly as false so we can break the while loop by set this to True later
terminate = False

while not terminate:
    # set a boolean login_status to avoid the robot question if login successful
    login_status = False
    for i in range(3):
        username = input("Enter username: ")
        passwd = input("Enter password: ")

        # use the list to store the username and password just like the initial login_list
        user_enter = [username,passwd]

        # use in to check if username and password both exist in the list
        if user_enter in login_list:
            print(f"Login successful. Welcome {username} !")

            # set login_status and terminate True to avoid robot check and break the while loop 
            login_status = True
            terminate = True

            # once match then break the loop
            break
        else:
            print(f"Login incorrect. Tries left: {2-i}")
            
    # use while loop for keep asking the question
    while not login_status:
        robot_answer = input("Are you a robot (Y/n)? ")
        if robot_answer == "n":
            break
        elif robot_answer == "" or robot_answer == "Y":
            terminate = True
            break
        else:
            # keep looping if answer is unexpected
            continue