#class A:

#    def __init__(self,roll_no,name,age,branch,city):
    
#     self.student_roll_no = roll_no
#     self.student_name = name
#     self.student_age = age
#     self.student_branch = branch
#     self.student_city = city

#    def Output(self):
#       print(self.student_roll_no,self.student_name,self.student_age,
#             self.student_branch,self.student_city)
#    #def Output(self):
    #    print(self.my_id,self.name,self.age,self.city)
#o1 = A(1001,"bhavik",23,"MBA","jaipur")

#o1.Output()

#o2 = A(1002,"bhavya",23,"MBA","jaipur")
#o2.Output()
class car:

    def __init__(self,desine,colour,type,model,company):

     self.car_desine = desine
     self.car_colour = colour
     self.car_type = type
     self.car_model = model
     self.car_company = company

    def Output(self):
       print(self.car_desine,self.car_colour,self.car_type,self.car_model,self.car_company)

#o1 = car("hatchback","rad","family",2021,"hyundai")
#o1.Output()
#o2 = car("sadan","white","mini_suv",2024,"tata")
#o2.Output()
num = int(input("how many object do you want to create :"))

l = []

for i in range(0,num):
   
   car_desine = input("Enter your car desine :")
   car_colour = input("Enter your car colour :")
   car_type = input("Enter your car type :")
   car_model = input("Enter your car model :")
   car_company = input("Enter your car company :")
   
   obj = car(car_desine,car_colour,car_type,car_model,car_company)
   l.append(obj)

for i in l:
   i.Output()