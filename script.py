class Student:
    def __init__(self, name, year):
        self.name = name
        self.year = year
        self.grades = []
    
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


class Grade:
    minimum_passing = 65

    def __init__(self, score):
        self.score = score
    
    def is_passing(self):
        return self.score >= self.minimum_passing
        


# create 3 student instances
roger = Student("Roger van der Weyden", 10)        
sandro = Student("Sandro Botticelli", 12)
pieter = Student("Pieter Bruegel the Elder", 8)

#add new grade for Pieter
pieter_math_grade = Grade(100)
pieter.add_grade(pieter_math_grade)



