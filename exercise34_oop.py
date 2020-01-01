#student = {"name": "Rolf", "grades":(89,90,93,78,90)}

#def average(sequence):
#    return sum(sequence) / len(sequence)

#print(average(student["grades"]))

#print(student.average())

class Student:
    def __init__(self,name,grades):
        self.name = name
        self.grades = grades

    def average(self):
        return sum(self.grades) /len(self.grades)

student = Student("Bob",(90,90,93,78,90))
student1 = Student("Rolf",(89,96,95,80,90))
print(student.name)
print(student.grades)
print(student.average())

print(student1.name)
print(student1.grades)
print(student1.average())