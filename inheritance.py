#super class(father):
class person():
    def __init__(self,name,age,gander):
        self.name=name
        self.age=age
        self.gender=gander

    def printall(self):
        print('name = ', self.name) 
        print('age = ', self.age) 
        print('gander = ', self.gender)

#وراثة خصائص الاب ل كلاس اخر 
#اضافة خصائص جديدة وهي salary
class employee(person):
    def __init__(self,name,age,gander,salary):
        self.salary=salary            
        person.__init__(self,name,age,gander)

    def printall(self):
        print('name = ', self.name) 
        print('age = ', self.age) 
        print('gander = ', self.gender)
#اضافة نسخة معادلة من الدالة
        print('salary = ' ,self.salary)    
class manager():
    def __init__(self,name,id,location):
        self.name=name
        self.id=id
        self.location=location
    def printall(self):
        print('name = ' ,self.name) 
        print('id = ' ,self.id) 
        print('location = ' ,self.location) 
class ceo(employee,manager):
    def __init__(self,name,age,gander,id,location,salary):
        manager.__init__(self,name,id,location)
        employee.__init__(self,name,age,gander,salary)
    def printall(self):
        print('name = ', self.name) 
        print('age = ', self.age) 
        print('gander = ', self.gender) 
        print('salary = ' ,self.salary)  
        print('id = ' ,self.id) 
        print('location = ' ,self.location) 




emp1 = ceo('ahmed',25,'male',2500,1234,'Asyut')

emp1.printall()        