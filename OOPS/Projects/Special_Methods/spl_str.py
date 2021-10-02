class Student:
    """
        This is class for all the Students. This is implemented to understand the
        concepts of special methods and the concepts of method overloading   
    """
    
    def __init__(self, student_id, student_name, student_age, student_gpa):
        """
        This is the constructor of the class where it initializes the all the
        required variables
        """
        self.student_id = student_id
        self.student_name = student_name
        self.student_age = student_age
        self.student_gpa = student_gpa
        
    def __str__(self):
        """
        This  Method basically overloads the print functionality. Since the print method
        basically uses __str__() method indirectlty
        """
        return f"Student Identification Number : {self.student_id} " \
               f"Student Name : {self.student_name} " \
               f"Student Age : {self.student_age} " \
               f"Student GPA : {self.student_gpa}"
            
            
student = Student("12004385", "Sujeeth Kurapati", 26, 3.10) 

print(student) #operator overloading
help(Student) #implementation of doc strings  