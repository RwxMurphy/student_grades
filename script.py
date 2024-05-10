class Student:
    def __init__(self, name, year):
        self.name = name
        self.year = year

class Grade:
    minimum_passing = 60
    def __init__(self, score):
        self.score = score
    



# create 3 student instances
roger = Student("Roger van der Weyden", 10)        
sandro = Student("Sandro Botticelli", 12)
pieter = Student("Pieter Bruegel the Elder", 8)

