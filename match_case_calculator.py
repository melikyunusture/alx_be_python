num1 = int(input("the first number"))
num2 = int(input("the second number"))

if num2==0:
    print("cannot divide by zero")

sum = num1 + num2
subtract = num1 - num2
div = num1/num2
   
multiply = num1 * num2

chooseOperation = input("Choose the operation (+, -, *, /)")

match chooseOperation:
    case '+':
        print("the result is, ", sum )
    case '/':
        if (num2 == 0):
            print("cannot divided by zero")

        else:
            print("the result is ", div)
    case "*":
        print("the result is ", multiply)
    case "-":
        print("the result is: ", subtract)    





