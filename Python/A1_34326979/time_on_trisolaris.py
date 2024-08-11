"""
This program converts a number of seconds that user entered into seconds, minutes and hours.
And also where the conversion from one unit to the other is defined during the program, rather than being fixed.
"""

seconds = int(input("TIME ON EARTH\nInput a time in seconds:\n"))

# Firstly calculate the hours and remaining minutes
hours = seconds // (60 ** 2)
remaining_minutes = seconds % (60 ** 2)

# Then calculate the minutes and remaining_seconds
minutes = remaining_minutes // 60
remaining_seconds = remaining_minutes % 60

# use the f-string to output the variables
print(f"\nThe time on Earth is {hours} hours {minutes} minutes and {remaining_seconds} seconds.\n")

sec_in_min = int(input("TIME ON TRISOLARIS\nInput the number of seconds in a minute on Trisolaris:\n"))
min_in_hour = int(input("Input the number of minutes in an hour on Trisolaris:\n"))

# calculate the hours, minutes and seconds using given units
tri_hours = seconds // (min_in_hour * sec_in_min)
tri_remaining_minutes = seconds % (min_in_hour * sec_in_min)
tri_minutes = tri_remaining_minutes // sec_in_min
tri_remianing_seconds = tri_remaining_minutes % sec_in_min

# use the f-string to output the variables
print(f"\nThe time on Trisolaris is {tri_hours} hours {tri_minutes} minutes and {tri_remianing_seconds} seconds.")