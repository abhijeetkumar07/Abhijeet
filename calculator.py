# # def add(x,y):
# #     return x + y
# # def subtract(x,y):
# #     return x - y
# # def multiply(x,y):
# #     return x * y
# # def divide(x,y):
# #     return x / y
# # def percentage(x,y):
# #     return x % y

# # print("Select Operation.")
# # print("1.Add")
# # print("2.Subtract")
# # print("3.Multiply")
# # print("4.Divide")
# # print("5.Percentage")

# # while True:
# #     choice = input("Enter choice(1/2/3/4/5): ")
# #     if choice in ('1', '2', '3', '4', '5'):
# #         try:
# #             num1 = int(input ("Enter first number: "))
# #             num2 = int(input("Enter second number: "))
# #         except ValueError:
# #             print("Invalid input. Please enter a number.")
# #             continue
# #         if choice == '1':
# #             print(num1, "+", num2, "=", add(num1, num2))
# #         elif choice == '2':
# #             print(num1, '-', num2, "=", subtract(num1, num2))
# #         elif choice == '3':
# #             print(num1, '*', num2, "=", multiply(num1, num2))
# #         elif choice == '4':
# #             print(num1, '/', num2, "=", divide(num1, num2))
# #         elif choice == '5':
# #             print(num1, '%', num2, "=", percentage(num1, num2))

# #         else:
# #             print("Invalid Input")
# class cal():
#     def __init__(self,a,b):
#         self.a=a
#         self.b=b
#     def add(self):
#         return self.a+self.b
#     def sub(self):
#         return self.a-self.b
#     def mul(self):
#         return self.a*self.b
#     def div(self):
#         return self.a/self.b

# a=(input("Enter a first number: "))
# b=(input("Enter a second number: "))
# obj=cal(a,b)
# choice=1
# while choice!=o:
#     print("0. Exit")
#     print("1. Add")
#     print("2. subtract")
#     print("3. Multiply")
#     print("4. Divide")
#     choice=int(input("Enter choice: "))
#     if choice==1:
#         print("Result: ",obj.add())
#     elif choice==2:
#         print("Result: ",obj.sub())
#     elif choice==3:
#         print("Result: ",obj.mul())
#     elif choice==4:
#         print("Result: ",obj.div())
class rectangle():
    def __init__(self,breadth,lenght):
        self.breadth=breadth
        self.lenght=lenght
    def area(self):
        return self.lenght*self.breadth
    a=int(input("Enter length of rectangle: "))
    b=int(input("Enter breadth of rectangle: "))
    obj=rectangle(a,b)
    print("Area of rectangle:",obj.area())
    
    print()