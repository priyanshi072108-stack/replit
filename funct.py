# Function to display student details
def student_info():

    # Dictionary storing student data
    students = {
        1: ("Rahul", 85),
        2: ("Anita", 90),
        3: ("Ravi", 78)
    }

    # Display student information
    print("Student Details:\n")

    for key, value in students.items():
        name, marks = value   # tuple unpacking
        print("Roll No:", key)
        print("Name:", name)
        print("Marks:", marks)
        print()

# Calling the function
student_info()
