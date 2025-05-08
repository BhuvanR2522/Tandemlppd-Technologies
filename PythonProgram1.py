class Calculator:
    def add(self,a,b):
        return a + b
    def subtract(self,a,b):
        return a - b
    def multiply(self,a,b):
        return a * b
    def divide(self,a,b):
        if b == 0 :
            print("Error : B value cannot be Zero.")
        return a / b

calculator = Calculator()

a = float(input())
b = float(input())
operations = input()

if operations == "add":
    print("Result : " ,calculator.add(a ,b))
elif operations == "subtract":
    print("Result : " ,calculator.subtract(a ,b))
elif operations == "divide":
    print("Result : " ,calculator.divide(a ,b))
elif operations == "multiply":
    print("Result : " ,calculator.multiply(a ,b))
else:
    print("Invalid Operations")
