class Student:
    def __init__(self, name, year):
        self.name = name
        self.year = year
        self.grades = []
        self.attendance = {}
    
    def add_grade(self, grade):
        if type(grade) is Grade:
            self.grades.append(grade)

    def get_average(self):
        total_grade = 0
        num_of_grades = len(self.grades)
        
        for grade in self.grades:
            total_grade += grade

        average = total_grade / num_of_grades
        return average
    
    def get_attendance(self, student_attendance):
        if type(student_attendance) is Attendance:
            self.attendance[student_attendance.day] = student_attendance.is_present 
        return self.attendance

        
    # Add an instance variable to Student that is a dictionary called .attendance, 
    # with dates as keys and booleans as values that indicate whether the student attended school that day.


class Grade:
    minimum_passing = 65

    def __init__(self, score):
        self.score = score
    
    def is_passing(self):
        return self.score >= self.minimum_passing
        

class Attendance:
    def __init__(self, day, is_present):
        self.day = day
        self.is_present = is_present

    

# create 3 student instances
roger = Student("Roger van der Weyden", 10)        
sandro = Student("Sandro Botticelli", 12)
pieter = Student("Pieter Bruegel the Elder", 8)

#add new grade for Pieter
pieter_math_grade = Grade(100)
pieter.add_grade(pieter_math_grade)



