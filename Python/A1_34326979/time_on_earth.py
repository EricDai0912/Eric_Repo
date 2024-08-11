"""
This program converts a number of seconds that user entered into seconds, minutes and hours.
"""

seconds = int(input("TIME ON EARTH\nInput a time in seconds:\n"))

# Firstly calculate the hours and remaining minutes
hours = seconds // (60 ** 2)
remaining_minutes = seconds % (60 ** 2)

# Then calculate the minutes and remaining_seconds
minutes = remaining_minutes // 60
remaining_seconds = remaining_minutes % 60

# use the f-string to output the variables
print(f"\nThe time on Earth is {hours} hours {minutes} minutes and {remaining_seconds} seconds.")