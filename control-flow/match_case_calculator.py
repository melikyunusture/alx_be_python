''' 

num1 = int(input("enter the first number: "))
num2 = int(input("enter the second number: "))
operation = input("Choose the operation (+, -, *, /): ")

Match operation:
    case "+":  
     result = num1 + num2
        print("the result is:",result)
    case "-":
result = num1 - num2
        print("the result is:",result)
    case "*":
result = num1 * num2
        print("the result is:",result)
 case "/":  
if num2 != 0 
result = num1 / num2  
 print("the result is:", result)
case_:      
 print("cannot divide by zero" )

'''



# Prompt the user for inputs
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operation = input("Choose the operation (+, -, *, /): ")

# Perform calculation using match case
match operation:
    case "+":
        result = num1 + num2
        print("The result is ", result,".")
    case "-":
        result = num1 - num2
        print("The result is ", result,".")
    case "*":
        result = num1 * num2
        print("The result is ", result,".")
    case "/":
        if num2 != 0:
            result = num1 / num2
            print("The result is ", result,".")
        else:
            print("Cannot divide by zero..")
    case _:
        print("Invalid operation selected.")