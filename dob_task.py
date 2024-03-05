# ========= Task 1 ===========
# Writing a program to read in the file DOB.txt

# Creating the two lists to hold names and birthrates:
names = []
birthdates = []

# Open file and read in the data (r) 
with open('DOB.txt', 'r') as file: 
    for line in file:
        # Split the line by spaces:
        parts = line.strip().split()
        # The name is the first two parts, birthdate is the rest:
        name = ' '.join(parts[:2]) # Join with a space to separate the list string
        birthdate = ' '.join(parts[2:])

        # Append to the relevant initialised lists:
        names.append(name) 
        birthdates.append(birthdate)

# Print out the Names:
print("Name:")
for name in names:
    print (name)

# Print out the Birthdates:
print("\nBirthdate:")
for birthdate in birthdates:
    print (birthdate)