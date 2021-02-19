def addition(a,b):
    return a + b

def subtraction(a,b):
    return a - b

def multiplication(a,b):
    return a * b

def division(a,b):
    return a / b        

print("Select the operation: ")
print("Press 1 for add")
print("Press 2 for subtract")
print("Press 3 for multiply")
print("Press 4 for divide")

choose_number = input("Enter the choice:(1 or 2 or 3 or 4) ")

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))


if choose_number == "1":
    print(num1, "+" ,num2, "=", addition(num1, num2))

elif choose_number == "2":
    print(num1, "-" ,num2, "=", subtraction(num1, num2))

elif choose_number == "3":
    print(num1, "*" ,num2, "=", multiplication(num1, num2))

elif choose_number == "4":
    print(num1, "/" ,num2, "=", division(num1, num2))    

else :
    print("Invalid Choice of Operation")    