class Box:
    def __init__(self,nameofStudent,rollno):
        self.name = nameofStudent
        self.rollno = rollno

class student:
    def __init__(self,fees):
        self.fees=fees
    
class Box2(Box , student):
    def __init__(self,name,rollno,marks,fees):
        self.marks= marks
        student.__init__(self,fees)
        Box.__init__(self,name,rollno)

class Box3(Box2):
    def __init__(self,sem):
        self.sem = sem
        Box2.__init__(self,"shivaraj",12,23,20000)  


obj = Box3("2-1")
print(obj.sem)
print(obj.name)

obj2 = Box2("shiv",12,23,20000)
print(obj2.fees)
print(obj2.marks)
print(obj2.name)
print(obj2.rollno)

obj3 = Box2("raj",45,234,10000)
print(obj3.name)
print(obj3.rollno)
print(obj3.marks)
print(obj3.fees)
