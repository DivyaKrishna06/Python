from datetime import datetime

# Input dates in the format: YYYY-MM-DD
date1_str = input("Enter the first date (YYYY-MM-DD): ")
date2_str = input("Enter the second date (YYYY-MM-DD): ")

# Convert the input strings to datetime objects
date1 = datetime.strptime(date1_str, "%Y-%m-%d")
date2 = datetime.strptime(date2_str, "%Y-%m-%d")

# Calculate the difference between the two dates
delta = date2 - date1

# Extract the number of days from the difference
num_days = delta.days

print(f"The number of days between {date1_str} and {date2_str} is {num_days} days.")