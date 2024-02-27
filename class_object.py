class A:

    def __init__(self,roll_no,name,age,branch,city):
    
     self.student_roll_no = roll_no
     self.student_name = name
     self.student_age = age
     self.student_branch = branch
     self.student_city = city

    def Output(self):
       print(self.student_roll_no,self.student_name,self.student_age,
             self.student_branch,self.student_city)
    #def Output(self):
    #    print(self.my_id,self.name,self.age,self.city)
o1 = A(1001,"bhavik",23,"MBA","jaipur")

o1.Output()

o2 = A(1002,"bhavya",23,"MBA","jaipur")
o2.Output()

