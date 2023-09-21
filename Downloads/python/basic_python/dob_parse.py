import datetime

def get_valid_date_of_birth():
    while True:
        dob_str = input("Please enter your date of birth (YYYY-MM-DD): ")

        try:
            # Attempt to parse the input string into a datetime object
            dob = datetime.datetime.strptime(dob_str, '%Y-%m-%d')

            # Check if the entered date is in the past (assuming current date is today)
            if dob > datetime.datetime.now():
                print("Please enter a valid date of birth in the past.")
            else:
                return dob.date()  # Return the date part (without time)
        except ValueError:
            print("Invalid date format. Please use YYYY-MM-DD.")

# Get the date of birth from the user
date_of_birth = get_valid_date_of_birth()

print("Your date of birth is:", date_of_birth)