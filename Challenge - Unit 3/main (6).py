class Student:
  
    def __init__(self, name, roll_number, cgpa):
        self.name = name
        self.roll_number = roll_number
        self.cgpa = cgpa


def sort_students(student_list):
    # Sort the students by CGPA in descending order
    sorted_students = sorted(student_list, 
                             key=lambda student: student.cgpa, 
                             reverse=True)
    # Return the sorted list of students
    return sorted_students
# Test the function with different input lists of students
students = [
    Student("Tae", "BT21", 3.8),
    Student("Jimin", "BT22", 3.6),
    Student("Jungkook", "BT23", 3.4),
]

sorted_students = sort_students(students)

#print the sorted list of students
for student in sorted_students:
  print("Name: {}, Roll Number: {}, CGPA: {}". format(student.name, student.roll_number,
                                                     student.cgpa))

