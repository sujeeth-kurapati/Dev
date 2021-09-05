class MusicSchool:
    students = {"Gino":   [15, "653-235-345", ["Piano", "Guitar"]],
		    "Talina": [28, "555-765-452", ["Cello"]],
		    "Eric":   [12, "583-356-223", ["Singing"]]}
    
    def __init__(self, working_hours, revenue):
        self.working_hours = working_hours
        self.revenue = revenue
 
	# Add your methods below this line
    def print_students_data(self):
        for name in MusicSchool.students.keys():
            self.print_student(name)

    def print_student(self, student_name):
        if student_name in MusicSchool.students.keys():
            attr = MusicSchool.students[student_name]
            print(f"Student: {student_name} who is {attr[0]} years old and is taking {attr[2]}")
        else:
            print("The mentioned student is not present in the database")

    def add_student(self, new_student, student_details):
        if new_student not in MusicSchool.students.keys():
            if isinstance(new_student, str) and isinstance(student_details, list):
                MusicSchool.students[new_student] = student_details
            else:
                print("Please enter the details of the student properly")
        else:
            print("The student is already present in the database")
 
# Create the instance
my_music = MusicSchool(40, 800)

# Call the method
my_music.print_students_data()
my_music.print_student("Gino")
my_music.add_student("Jack", [60, "562-234-234", ["Piano"]])