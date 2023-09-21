import datetime

class Person:
    def __init__(self, name, country, dob):
        self.name = name
        self.country = country
        self.dob = dob

    def calculate_age(self):
        today = datetime.date.today()
        dob = datetime.datetime.strptime(self.dob, "%Y-%m-%d").date()
        age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
        return age

# Create an empty list to store person objects
people_list = []

# Input loop
while True:
    name = input("Enter the person's name (or 'exit' to quit): ")
    if name.lower() == 'exit':
        break
    country = input("Enter the person's country: ")
    dob = input("Enter the person's date of birth (YYYY-MM-DD): ")

    # Create a Person object and append it to the list
    person = Person(name, country, dob)
    people_list.append(person)

# Display the details and age of each person in the list
print('Person details are as follows:')
for person in people_list:
    age = person.calculate_age()
    print(f"Name: {person.name}")
    print(f"Country: {person.country}")
    print(f"Date of Birth: {person.dob}")
    print(f"Age: {age} years\n")