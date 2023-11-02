class calculator():
    def addition(a,b):
        add=a+b
        return add
    def subtraction(a,b):
        sub=a-b
        return sub
    def Multiplication(a,b):
        mul=a*b
        return mul
result1=calculator.addition(2,3)
print("Addition: ",result1)
result2=calculator.subtraction(2,3)
print("Subtraction: ",result2)
result3=calculator.Multiplication(2,3)
print("Multiplication: ",result3)