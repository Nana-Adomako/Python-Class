
# ------------------------------------------------------------------------------------------ #
# Title: Assignment05
# Desc: This assignment demonstrates error handling , and data management with Python
# Change Log: (Who, When, What)
# Nana Adomako,11/13/2023,Created Script
# ------------------------------------------------------------------------------------------ #

# Constants
MENU = """
---- Course Registration Program ----
  Select from the following menu:  
    1. Register a Student for a Course
    2. Show current data  
    3. Save data to a file
    4. Exit the program
-----------------------------------------
"""

FILE_NAME = "Enrollments.txt"

# Variables
student_first_name = ""
student_last_name = ""
course_name = ""
students = []

# Read data from file
try:
    with open(FILE_NAME, 'r') as file:
        lines = file.readlines()
        for line in lines[1:]:  # Skip header line
            data = line.strip().split(',')
            students.append({"First Name": data[0], "Last Name": data[1], "Course": data[2]})
except FileNotFoundError:
    print("File not found. Please make sure to add some data to the file.")
except Exception as e:
    print(f"An error occurred while reading the file: {e}")

# Main Program
menu_choice = ""

while menu_choice != "4":
    print(MENU)
    menu_choice = input("Enter your choice (1-4): ")

    try:
        if menu_choice == "1":
            student_first_name = input("Enter the student's first name: ")
            if not student_first_name:
                raise ValueError("First name cannot be empty.")

            student_last_name = input("Enter the student's last name: ")
            if not student_last_name:
                raise ValueError("Last name cannot be empty.")

            course_name = input("Enter the course name: ")

            students.append({"First Name": student_first_name, "Last Name": student_last_name, "Course": course_name})
            print("Student registered successfully.")

        elif menu_choice == "2":
            for data in students:
                print(f"First Name: {data['First Name']}, Last Name: {data['Last Name']}, Course: {data['Course']}")

        elif menu_choice == "3":
            with open(FILE_NAME, 'w') as file:
                file.write("First Name,Last Name,Course\n")
                for data in students:
                    file.write(f"{data['First Name']},{data['Last Name']},{data['Course']}\n")
            print("Data saved to file.")

        elif menu_choice == "4":
            print("Exiting the program.")

        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

    except ValueError as ve:
        print(f"Error: {ve}")

    except Exception as e:
        print(f"An unexpected error occurred: {e}")
