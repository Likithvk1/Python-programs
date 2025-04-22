class Student:
    id = int(input("Enter ID ="))
    name = input("Enter name =")
    marks = int(input("Enter marks ="))

    def __init__(self,id,name,marks):
        self.id = id
        self.name = name
        self.marks = marks


    def show_data(self):
        print(f"ID = {self.id}")
        print(f"Name = {self.name}")
        print(f"Marks = {self.marks}")
    
    
    
s1 = Student(111,'ABC',55)
s1.show_data()

s2 = Student(222,'XYZ', 99)
s2.show_data()

